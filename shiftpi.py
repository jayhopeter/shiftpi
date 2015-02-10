'''
A library that allows simple access to 74HC595 shift registers on a Raspberry
Pi using any digital I/O pins.
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

version = "0.2"
version_info = (0, 2)

# Define MODES
ALL = -1
HIGH = 1
LOW = 0


class Shiftpi:
    def __init__(self):
        # Define pins
        self._SER_pin = 25      # pin 14 on the 75HC595
        self._RCLK_pin = 24     # pin 12 on the 75HC595
        self._SRCLK_pin = 23    # pin 11 on the 75HC595

        # is used to store states of all pins
        self._registers = list()

        '''
        How many of the shift registers - you can change them with
        shiftRegisters method
        '''
        self._number_of_shiftregisters = 1
        self.pinsSetup()

    def pinsSetup(self, **kwargs):
        '''
        Allows the user to define custom pins
        '''
        custompins = 0
        serpin = self._SER_pin
        rclkpin = self._RCLK_pin
        srclkpin = self._SRCLK_pin

        if len(kwargs) > 0:
            custompins = 1

            self._SER_pin = kwargs.get('ser', self._SER_pin)
            self._RCLK_pin = kwargs.get('rclk', self._RCLK_pin)
            self._SRCLK_pin = kwargs.get('srclk', self._SRCLK_pin)

        if custompins:
            if ((self._SER_pin != serpin or
                 self._RCLK_pin != rclkpin or
                 self._SRCLK_pin != srclkpin)):
                GPIO.setwarnings(True)
        else:
            GPIO.setwarnings(False)

        GPIO.setup(self._SER_pin, GPIO.OUT)
        GPIO.setup(self._RCLK_pin, GPIO.OUT)
        GPIO.setup(self._SRCLK_pin, GPIO.OUT)

    def startupMode(self, mode, execute=False):
        '''
        Allows the user to change the default state of the shift registers
        outputs
        '''
        if isinstance(mode, int):
            if mode is HIGH or mode is LOW:
                self._all(mode, execute)
            else:
                raise ValueError('''The mode can be only HIGH or LOW or
                    Dictionary with specific pins and modes''')
        elif isinstance(mode, dict):
            for pin, mode in mode.iteritems():
                self._setPin(pin, mode)
            if execute:
                self._execute()
        else:
            raise ValueError('''The mode can be only HIGH or LOW or Dictionary
                with specific pins and modes''')

    def shiftRegisters(self, num):
        '''
        Allows the user to define the number of shift registers are connected
        '''
        self._number_of_shiftregisters = num
        self._all(LOW)

    def digitalWrite(self, pin, mode):
        '''
        Allows the user to set the state of a pin on the shift register
        '''
        if pin == ALL:
            self._all(mode)
        else:
            if len(self._registers) == 0:
                self._all(LOW)

            self._setPin(pin, mode)
        self._execute()

    def delay(self, millis):
        '''
        Used for creating a delay between commands
        '''
        millis_to_seconds = float(millis)/1000
        return sleep(millis_to_seconds)

    def _all_pins(self):
        return self._number_of_shiftregisters * 8

    def _all(self, mode, execute=True):
        all_shr = self._all_pins()

        for pin in range(0, all_shr):
            self._setPin(pin, mode)
        if execute:
            self._execute()

        return self._registers

    def _setPin(self, pin, mode):
        try:
            self._registers[pin] = mode
        except IndexError:
            self._registers.insert(pin, mode)

    def _execute(self):
        all_pins = self._all_pins()
        GPIO.output(self._RCLK_pin, GPIO.LOW)

        for pin in range(all_pins - 1, -1, -1):
            GPIO.output(self._SRCLK_pin, GPIO.LOW)

            pin_mode = self._registers[pin]

            GPIO.output(self._SER_pin, pin_mode)
            GPIO.output(self._SRCLK_pin, GPIO.HIGH)

        GPIO.output(self._RCLK_pin, GPIO.HIGH)
