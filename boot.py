import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
import json
from machine import Pin, I2C
from time import sleep
import BME280

esp.osdebug(None)
import gc

gc.collect()

ssid = 'wifi ssid'
password = 'wachtwoord'
mqtt_server = 'IP ADRES RASPBERRY PI!!'
mqtt_username = "USERNAME"
mqtt_password = "PASSWORD"
mqtt_port = 1883
# !!LET OP!! gebruik NOOIT hetzelfde wachtwoord als de username, DIT IS EEN DEMO VOORBEELD!!#
# EXAMPLE IP ADDRESS
# mqtt_server = '192.168.2.14'
client_id = "esp32_1"
topic_sub = b'notification'
topic_pub = b'ESPdata'

last_message = 0
message_interval = 5
counter = 1999

station = network.WLAN(network.STA_IF)

station.active(True)
try:
    station.connect(ssid, password)

except:
    print("not connected to network #1")
    time.sleep(2)
    try:
        station.connect(ssid, password)
    except:
        time.sleep(2)
        machine.reset()

print("Connected")
print(station.ifconfig())



