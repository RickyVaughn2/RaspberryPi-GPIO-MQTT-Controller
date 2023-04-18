import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import socket

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set up MQTT client
mqtt_broker = "your_mqtt_broker_address"
mqtt_port = 1883
mqtt_client = mqtt.Client()

# Set up hostname
hostname = socket.gethostname()

# Set up GPIO pin list
gpio_pins = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

# Set up GPIO pins as output
for pin in gpio_pins:
    GPIO.setup(pin, GPIO.OUT)

# MQTT message callback
def on_message(client, userdata, msg):
    topic_parts = msg.topic.split("/")
    if len(topic_parts) == 3 and topic_parts[0] == hostname and topic_parts[1] == "GPIO":
        try:
            pin = int(topic_parts[2])
            if pin in gpio_pins:
                GPIO.output(pin, GPIO.HIGH if msg.payload.decode() == "1" else GPIO.LOW)
        except ValueError:
            pass

# Connect to MQTT broker
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker, mqtt_port, 60)

# Subscribe to GPIO topics
for pin in gpio_pins:
    mqtt_client.subscribe(f"{hostname}/GPIO/{pin}")

# Start MQTT client loop
mqtt_client.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

# Clean up
mqtt_client.loop_stop()
GPIO.cleanup()
