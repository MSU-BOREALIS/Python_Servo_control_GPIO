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
	pwm.start(50)
	sleep(1)

def main():
	duty_cycle = 25
	setup()
	check = False
	while(check):
		duty_cycle = duty_cycle + 5
		pwm.ChangeDutyCycle(duty_cycle)
		sleep(.3)
		if(duty_cycle == 75):
			check = False


main()
GPIO.cleanup()
