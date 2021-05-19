import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

DO = 17
AO = 27

GPIO.setup(DO, GPIO.IN)
GPIO.setup(AO, GPIO.IN)

time.sleep(2)
print('Ready')

try:
	while True:
		if(GPIO.input(DO)==1):
			print('DO input 1')
		elif(GPIO.input(DO)==0):
			print('DO input 0')	
		if(GPIO.input(AO)==1):	
			print('AO input 1')
		elif(GPIO.input(AO)==0):
			print('AO input 0')	
		time.sleep(1)

except KeyboardInterrupt:	
	print('Bye')
	GPIO.cleanup()
	exit()
