from shiftpi import HIGH, LOW, digitalWrite, delay

while True:
    digitalWrite(1, HIGH)
    delay(1000)
    digitalWrite(1, LOW)
    delay(1000)