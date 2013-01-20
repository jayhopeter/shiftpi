import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

version = "0.1"
version_info = (0, 1)

# Define MODES
ALL  = -1
HIGH = 1
LOW  = 0

# Define pins
_SER_pin   = 7    #pin 14 on the 75HC595
_RCLK_pin  = 8    #pin 12 on the 75HC595
_SRCLK_pin = 25   #pin 11 on the 75HC595

# is used to store states of all pins
_registers = list()

#How many of the shift registers - change this
_number_of_shiftregisters = 1

def pinsSetup(**kwargs):
    global _SER_pin, _RCLK_pin, _SRCLK_pin

    custompins = 0
    serpin = _SER_pin
    rclkpin = _RCLK_pin
    srclkpin = _SRCLK_pin

    if len(kwargs) > 0:
        custompins = 1

        _SER_pin = kwargs.get('ser', _SER_pin)
        _RCLK_pin = kwargs.get('rclk', _RCLK_pin)
        _SRCLK_pin = kwargs.get('srclk', _SRCLK_pin)

    if custompins:
        if _SER_pin != serpin or _RCLK_pin != rclkpin or _SRCLK_pin != srclkpin:
            GPIO.setwarnings(True)
    else:
        GPIO.setwarnings(False)

    GPIO.setup(_SER_pin, GPIO.OUT)
    GPIO.setup(_RCLK_pin, GPIO.OUT)
    GPIO.setup(_SRCLK_pin, GPIO.OUT)

def startupMode(mode, execute = False):
    if isinstance(mode, int):
        if mode is HIGH or mode is LOW:
            _all(mode, execute)
        else:
            raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")
    elif isinstance(mode, dict):
        for pin, mode in mode.iteritems():
            _setPin(pin, mode)
        if execute:
            _execute()
    else:
        raise ValueError("The mode can be only HIGH or LOW or Dictionary with specific pins and modes")


def shiftRegisters(num):
    global _number_of_shiftregisters
    _number_of_shiftregisters = num
    _all(LOW)

def digitalWrite(pin, mode):
    if pin == ALL:
        _all(mode)
    else:
        if len(_registers) == 0:
            _all(LOW)

        _setPin(pin, mode)
    _execute()

def delay(millis):
    millis_to_seconds = millis/1000
    return sleep(millis_to_seconds)

def _all_pins():
    return _number_of_shiftregisters * 8

def _all(mode, execute = True):
    all_shr = _all_pins()

    for pin in range(0, all_shr):
        _setPin(pin, mode)
    if execute:
        _execute()

    return _registers

def _setPin(pin, mode):
    try:
        _registers[pin] = mode
    except IndexError:
        _registers.insert(pin, mode)

def _execute():
    all_pins = _all_pins()
    GPIO.output(_RCLK_pin, GPIO.LOW)

    for pin in range(all_pins -1, -1, -1):
        GPIO.output(_SRCLK_pin, GPIO.LOW)

        pin_mode = _registers[pin]

        GPIO.output(_SER_pin, pin_mode)
        GPIO.output(_SRCLK_pin, GPIO.HIGH)

    GPIO.output(_RCLK_pin, GPIO.HIGH)

pinsSetup()