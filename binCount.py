from shiftpi import HIGH, LOW, digitalWrite, delay

for x in range(0, 256):
	y = x
	print 'setting binary ' + str(y)
	if y >= 128:
		y -= 128
		digitalWrite(0, HIGH)
	else:
		digitalWrite(0, LOW)
	if y >= 64:
		y -= 64
		digitalWrite(1, HIGH)
	else:
		digitalWrite(1, LOW)
	if y >= 32:
		y -= 32
		digitalWrite(2, HIGH)
	else:
		digitalWrite(2, LOW)
	if y >= 16:
		y -= 16
		digitalWrite(3, HIGH)
	else:
		digitalWrite(3, LOW)
	if y >= 8:
		y -= 8
		digitalWrite(4, HIGH)
	else:
		digitalWrite(4, LOW)
	if y >= 4:
		y -= 4
		digitalWrite(5, HIGH)
	else:
		digitalWrite(5, LOW)
	if y >= 2:
		y -= 2
		digitalWrite(6, HIGH)
	else:
		digitalWrite(6, LOW)
	if y >= 1:
		y -= 1
		digitalWrite(7, HIGH)
	else:
		digitalWrite(7, LOW)
	delay(250)
		