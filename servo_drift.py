import RPi.GPIO as GPIO
import argparse
import sys
from time import sleep

PWM_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT)
GPIO.setwarnings(False)
pwm = GPIO.PWM(PWM_PIN, 500)


def setup():
	pwm.start(25)

def main():
	duty_cycle = 24
	setup()
	check = True
	while(check):
		pwm.ChangeDutyCycle(duty_cycle)
		duty_cycle = duty_cycle + 2
		sleep(.2)
		if(duty_cycle == 62):
			check = False

def reverse_main():
	duty_cycle = 62
	check = True
	sleep(.2)
	while(check):
		duty_cycle = duty_cycle - 2
		pwm.ChangeDutyCycle(duty_cycle)
		sleep(.2)
		if(duty_cycle == 24):
			check = False	

def servo_center():
	pwm.ChangeDutyCycle(45)
	sleep(.5)


main()
reverse_main()
#only uncomment if not using the two functions above
#setup()
servo_center()
GPIO.cleanup()
