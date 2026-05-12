import os
import paho.mqtt.client as mqtt
import time
import random

# Setting names and configuration
BROKER = "localhost"
PORT = 1883
USER = os.getenv("MQTT_USER", "default_user")
PASS = os.getenv("MQTT_PASS", "default_pass")
TOPIC = "home/livingroom/plug/power"

# Setup Connection
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(USER, PASS)

print(f"Connecting to {BROKER}...")
client.connect(BROKER, PORT)

client.loop_start()

# "Ghost ShellyPlug" simulation
try:
    while True:
        power_usage = round(random.uniform(70.0, 75.0), 2)

        client.publish(TOPIC, power_usage)
        print(f"Sent: {power_usage} Watts to {TOPIC}")

        time.sleep(5)

except KeyboardInterrupt:
    print("Ghost Plug stopping.")
    client.loop_stop()
    client.disconnect()