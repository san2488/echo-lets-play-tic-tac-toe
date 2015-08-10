PIN_LED_MAP = [23, 12, 25, 26, 22, 16, 13, 17, 24]
LED_INDICES = range(len(PIN_LED_MAP))
BLINK_INTERVAL = 0.05
threads = [None] * 9
pin_blink_interrupts = [True] * 9
import RPi.GPIO as GPIO
import time as time
import threading
GPIO.setmode(GPIO.BCM)
for pin in PIN_LED_MAP:
    GPIO.setup(pin, GPIO.OUT)
    pass

def switch_on(led):
    pin = PIN_LED_MAP[led]
    GPIO.output(pin, True)

def switch_off(led):
    pin = PIN_LED_MAP[led]
    GPIO.output(pin, False)

def blink_once(led):
    switch_on(led)
    time.sleep(BLINK_INTERVAL)
    switch_off(led)
    time.sleep(BLINK_INTERVAL)

def blink_until_interrupt(led):
    while not pin_blink_interrupts[led]:
        blink_once(led)
        pass

def turn_all_off():
    for led in LED_INDICES:
        blink_off(led)
        pass
    for led in LED_INDICES:
        switch_off(led)
        pass

def turn_all_on():
    for led in LED_INDICES:
        switch_on(led)
        pass

def blink_on(led):
    pin_blink_interrupts[led] = False
    threads[led] = threading.Thread(target=blink_until_interrupt, args=(led,))
    threads[led].start()

def blink_off(led):
    pin_blink_interrupts[led] = True
    threads[led] and threads[led].join()

def cleanup():
    GPIO.cleanup()