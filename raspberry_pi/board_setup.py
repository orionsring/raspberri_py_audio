import RPi.GPIO as GPIO
channel = 7 #using BOARD numbering
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel,GPIO.OUT)
GPIO.output(channel,GPIO.HIGH)
GPIO.output(channel,GPIO.LOW)
GPIO.cleanup()
#gpio setup for raspberry pi using the Raspbian Python RPi.GPIO library
