#!/bin/bash

while true; do
    service_status=$(systemctl is-active catalis-chmi@sda1.service)

    if [ "$service_status" = "active" ]; then
        echo 1 > /sys/class/leds/PWR/brightness
    else
        echo 0 > /sys/class/leds/PWR/brightness
    fi

    sleep 1  
done
