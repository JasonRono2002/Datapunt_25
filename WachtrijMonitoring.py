from machine import Pin, time_pulse_us
import time

# Pins die verbonden zijn.
trigIngang = Pin(42, Pin.OUT)
echoIngang = Pin(41, Pin.IN)

trigUitgang = Pin(36, Pin.OUT)
echoUitgang = Pin(37, Pin.IN)

ledIngang = Pin(40, Pin.OUT)
ledUitgang = Pin(38, Pin.OUT)

# Tellers
in_teller = 0
uit_teller = 0

# Status
aanwezig_in = False
aanwezig_uit = False

# Functie voor het meten van de afstand.
def meet_afstand(trig, echo):
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duur = time_pulse_us(echo, 1, 30000)

    if duur > 0:
        return round(duur / 58)
    else:
        return 999


# Functie voor de ingang.
def check_ingang():
    global in_teller, aanwezig_in

    afstand = meet_afstand(trigIngang, echoIngang)

    if afstand < 50:
        ledIngang.on()

        if not aanwezig_in:
            in_teller += 1
            aanwezig_in = True
            print("Iemand is BINNEN gekomen")
            print("Totaal binnen:", in_teller)

    else:
        ledIngang.off()
        aanwezig_in = False


# Functie voor de uitgang
def check_uitgang():
    global in_teller, uit_teller, aanwezig_uit

    afstand = meet_afstand(trigUitgang, echoUitgang)

    if afstand < 50:
        ledUitgang.on()

        if not aanwezig_uit:
            uit_teller += 1
            in_teller -= 1
            aanwezig_uit = True

            print("Iemand is BUITEN gegaan")
            print("Totaal binnen:", in_teller)

    else:
        ledUitgang.off()
        aanwezig_uit = False


while True:
    check_ingang()
    check_uitgang()
    time.sleep(0.2)