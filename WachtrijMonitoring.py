from machine import Pin, time_pulse_us
import time

# Ingang pins -> sensor en led
trig_in = Pin(42, Pin.OUT)
echo_in = Pin(41, Pin.IN)
led_in = Pin(40, Pin.OUT)

# Uitgang pins -> sensor en led
trig_uit = Pin(36, Pin.OUT)
echo_uit = Pin(37, Pin.IN)
led_uit = Pin(38, Pin.OUT)

# Tellers
totaal_ingang = 0
totaal_uitgang = 0

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

        if afstand_in < 20:
            totaal_ingang += 1
            print(f"Ingang: {totaal_ingang}")
            led_in.on()
        else:
            led_in.off()

        # Uitgang afstand meten
        afstand_uit = meet_afstand(trig_uit, echo_uit)

        if afstand_uit < 20:
            totaal_uitgang -= 1
            print(f"Uitgang: {totaal_uitgang}")
            led_uit.on()
        else:
            led_uit.off()

        time.sleep(0.2)

# Als de code stopt dan gaat alles uit.
finally:
    led_in.off()
    led_uit.off()
    trig_in.off()
    trig_uit.off()