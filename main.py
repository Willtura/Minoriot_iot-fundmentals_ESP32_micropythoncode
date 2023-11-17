
# I2C Pin aansluiting
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

counter =0


def connect_and_subscribe():
    global client_id, mqtt_server, topic_sub
    client = MQTTClient(client_id, mqtt_server)
    client.connect()
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
    return client

def try_again():
    print('Failed to connect to MQTT broker. Reconnecting...')
    try:
        time.sleep(3)
        connect_and_subsribe()
    except:
        machine.reset()


try:
    time.sleep(2)
    client = connect_and_subscribe()
except OSError as e:
    try_again()

while True:
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    print('Temperature: ', temp
    print('Humidity: ', hum)
    print('Pressure: ', pres)

    msg = {
        "temperature": temp,
        "humidity": hum,
        "pressure": pres
    }
    json_msg = json.dumps(msg)
    client.publish(topic_pub, json_msg)
    time.sleep(2)



