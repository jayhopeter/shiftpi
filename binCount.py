#testing shiftpi 
#this program uses the outputs to a do a binary counter from 0 to the total number of bits

from shiftpi import HIGH, LOW, digitalWrite, delay

bits = 8  #hard coded to 8 (one chip) for now

#loop from 0 to the max value of the bits available
for x in range(0, 2 ** bits):
    temp = x
    print 'setting binary ' + str(temp)
    for b in range(bits - 1, -1,-1):
        if temp >= 2 ** b:
            y -= 2 ** b
            digitalWrite((bits-1)- b, HIGH)
        else:
            digitalWrite((bits-1)- b, LOW)
    delay(250)