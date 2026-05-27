from machine import Pin, time_pulse_us
import time

trig = Pin(42, Pin.OUT)
echo = Pin(41, Pin.IN)
led = Pin(40, Pin.OUT)

while True:
    trig.off()
    time.sleep_us(2)

    trig.on()
    time.sleep_us(10)
    trig.off()

    duur = time_pulse_us(echo, 1, 30000)

    afstand = round(duur / 58)

    if afstand < 20:
        led.on()      # LED aan als afstand kleiner is dan 5 cm
        print('Iemand is binnen,.')
    else:
        led.off()     # anders uit

    print(afstand)

    time.sleep(0.2)
