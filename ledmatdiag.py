#!/usr/bin/env python
NXT_TST_INTERVAL = 1
NEW_ROUND_INTERVAL = 2
TOGGLE_INTERVAL = 0.5   
from rpiledmatrix import switch_on, switch_off, turn_all_off, cleanup, blink_on, blink_off, LED_INDICES
import time as time

def blink_on_serial():
    for led in LED_INDICES:
        blink_on(led)
        time.sleep(TOGGLE_INTERVAL)
        blink_off(led)
        pass

def steady_on_serial():
    for led in LED_INDICES:
        switch_on(led)
        time.sleep(TOGGLE_INTERVAL)
        switch_off(led)
        pass
try:
    while True:
        steady_on_serial()
        time.sleep(NXT_TST_INTERVAL)
        blink_on_serial()
        time.sleep(NEW_ROUND_INTERVAL)
except KeyboardInterrupt:
    turn_all_off()
finally:
    cleanup()
