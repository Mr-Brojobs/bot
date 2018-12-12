import RPi.GPIO as GPIO
 
IRTrackingPin = 18

GPIO.setmode(GPIO.BCM) # Set the GPIO pins as numbering
GPIO.setup(IRTrackingPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

 
def loop():
        if GPIO.input(IRTrackingPin) == GPIO.HIGH:
            return "white"
 
        else:
            return "black"
 
 