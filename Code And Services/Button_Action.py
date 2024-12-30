#!/bin/python

import subprocess
import pyinotify

gpio_pin = 479
button_path = f"/sys/class/gpio/gpio{gpio_pin}/value"
identifier = sys.argv[1]

try:
    with open("/sys/class/gpio/export", "w") as export_file:
        export_file.write(f"{gpio_pin}\n")
except IOError:
    pass

with open(f"/sys/class/gpio/gpio{gpio_pin}/direction", "w") as direction_file:
    direction_file.write("in")

subprocess.run(f"echo both > /sys/class/gpio/gpio{gpio_pin}/edge", shell=True)

class ButtonEventHandler(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        button_state = subprocess.getoutput(f"cat {button_path}")

        if button_state == "1":
            subprocess.run(f"systemctl restart catalis-poll@{identifier}.service", shell=True)

wm = pyinotify.WatchManager()
handler = ButtonEventHandler()
wm.add_watch(button_path, pyinotify.IN_MODIFY)

notifier = pyinotify.Notifier(wm, handler)
notifier.loop()
