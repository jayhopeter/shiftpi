
import shiftpi

#shiftpi.pinsSetup({"ser": 16, "rclk": 20, "srclk": 21})
#shiftpi.startupMode({1: shiftpi.HIGH, 4: shiftpi.HIGH, 6: shiftpi.HIGH}, True)
shiftpi.delay(1000)
shiftpi.digitalWrite(shiftpi.ALL, shiftpi.LOW)
shiftpi.delay(1000)
for x in range(0, 9):
	shiftpi.digitalWrite(0, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(0, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(1, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(1, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(2, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(2, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(3, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(3, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(4, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(4, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(5, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(5, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(6, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(6, shiftpi.LOW)
	shiftpi.delay(500)
	shiftpi.digitalWrite(7, shiftpi.HIGH)
	shiftpi.delay(500)
	# turns shift register's pin 1 to LOW
	shiftpi.digitalWrite(7, shiftpi.LOW)
	shiftpi.delay(500)


