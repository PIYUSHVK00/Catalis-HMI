#!/bin/python


import os
from time import sleep
import subprocess as sh

# Class representing an LED
class Led():
	offset = 454 # Offset value for GPIO pin

    # Constructor to initialize the LED object with a GPIO pin
	def __init__(self, pin:int):
		self.gpio = pin + 454  # Calculate GPIO pin number

        # Check if GPIO pin exists, if not, create it
		if not os.path.exists(f"/sys/class/gpio/gpio{self.gpio}"):
			sh.run(f"echo {self.gpio} > /sys/class/gpio/export", shell=True)
			sh.run(f"echo out > /sys/class/gpio/gpio{self.gpio}/direction", shell=True)

    # Method to turn the LED on
	def on(self):
		sh.run(f"echo '1' > /sys/class/gpio/gpio{self.gpio}/value", shell=True)
	
    # Method to turn the LED off
	def off(self):
		sh.run(f"echo '0' > /sys/class/gpio/gpio{self.gpio}/value", shell=True)

class Service():
	def __init__(self, name:str):
		self.name = f"{name}.service" 

    # Method to get the status of the service
	def status(self):
		return sh.getoutput(f"systemctl is-failed {self.name}")

def daemon():   
 # Configuration mapping of services and associated LEDs
	mapping = [
		{
			"service": Service("catalis-chmi@sda1"),
			"leds": {
				"green": Led(17),
				"red": Led(27)
			}
		},
		{
			"service": Service("catalis-init@sda1"),
			"leds": {
				"green": Led(5),
				"red": Led(6)
			}
		},
		{
			"service": Service("catalis-mount@sda1"),
			"leds": {
				"green": Led(19),
				"red": Led(26)
			}
		},
		{
			"service": Service("catalis-poll@sda1"),
			"leds": {
				"green": Led(20),
				"red": Led(21)
			}
		},
	]
# Continuously monitor and update LED statuses based on service status
	while True:
		for service in mapping:
            # Turn off all LEDs for the service
			for led in service["leds"].values(): led.off()

            # Set LED according to service status
			if service["service"].status() == "failed":	service["leds"]["red"].on()
			elif service["service"].status() == "active": service["leds"]["green"].on()

		sleep(1) # Sleep for 1 second

# Entry point of the script
if __name__ == "__main__":
	daemon()   # Start the daemon for monitoring services and controlling LEDs