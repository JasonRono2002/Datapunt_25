from machine import Pin, time_pulse_us
import time

trigIngang = Pin(42, Pin.OUT)
echoIngang = Pin(41, Pin.IN)
led = Pin(40, Pin.OUT)

IngangTeller = 0
aanwezig = False

while True:
    trigIngang.off()
    time.sleep_us(2)

    trigIngang.on()
    time.sleep_us(10)
    trigIngang.off()

    duur = time_pulse_us(echoIngang, 1, 30000)

    if duur > 0:
        afstand = round(duur / 58)
    else:
        afstand = 999

    if afstand < 50:
        led.on()

        if not aanwezig:
            IngangTeller += 1
            print("Iemand is binnen")
            print("Totaal personen binnen:", IngangTeller)
            aanwezig = True

    else:
        led.off()
        aanwezig = False

    time.sleep(0.2)