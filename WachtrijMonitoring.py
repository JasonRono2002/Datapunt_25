from machine import Pin, time_pulse_us
import time

# Ingang pins -> sensor en led
trig_in = Pin(42, Pin.OUT)
echo_in = Pin(41, Pin.IN)
led_in = Pin(13, Pin.OUT)

# Uitgang pins -> sensor en led
trig_uit = Pin(40, Pin.OUT)
echo_uit = Pin(39, Pin.IN)
led_uit = Pin(11, Pin.OUT)

# Tellers als voorbeeld
totaal_ingang = 0

# Functie voor het berekenen van de afstand.
def meet_afstand(trig, echo):
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    duur = time_pulse_us(echo, 1, 30000)

    if duur < 0:
        return 999  # geen meting

    return round(duur / 58)

try:
    while True:
        # Ingang afstand meten
        afstand_in = meet_afstand(trig_in, echo_in)

        if afstand_in < 40:
            totaal_ingang += 1
            print(f"Ingang ingelopen: {totaal_ingang}e persoon")
            led_in.on()
        else:
            led_in.off()

        # Uitgang afstand meten
        afstand_uit = meet_afstand(trig_uit, echo_uit)

        if afstand_uit < 40:
            totaal_ingang -= 1
            print(f"Persoon is de uitgang uitgelopen \n Totaal nog in de wachtrij: {totaal_ingang}")
            led_uit.on()
        else:
            led_uit.off()
        
        if totaal_ingang <= 0:
            totaal_ingang = 0


        time.sleep(1)

# Als de code stopt dan gaat alles uit.
finally:
    led_in.off()
    led_uit.off()
    trig_in.off()
    trig_uit.off()