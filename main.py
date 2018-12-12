import RPi.GPIO as gpio
import dry_run
import wet_run
import signal
import time

gpio.set_mode(gpio.BCM)
gpio.setup(2,gpio.IN)

argument={}

i=0
while True:
if i==0:
	if gpio.input(2)==1:
		i+=1
		Thread(dry_run.move,args=[argument]).start()
		dry_run.thread_forward('right')
		
if i==1:
	if gpio.input(2)==0:
		if wet_run.run(argument[0],argument[1],argument[2],argument[3]):
			signal.end_signal()
			


