# Raspberry Pi GPIO MQTT Controller

This Python application for the Raspberry Pi allows you to control GPIO pins via an MQTT broker. It listens for MQTT messages on topics in the format `{hostname}/GPIO/{pin_number}` and sets the corresponding GPIO pin to either HIGH or LOW based on the received payload.

## Prerequisites

1. A Raspberry Pi with GPIO headers (e.g., Raspberry Pi 3, 4, or Zero)
2. Python 3.x installed on the Raspberry Pi
3. An MQTT broker accessible from the Raspberry Pi

## Installation

1. Clone the repository to your Raspberry Pi:

```
git clone https://github.com/yourusername/raspberry-pi-gpio-mqtt-controller.git
```

2. Change the directory to the cloned repository:

```
cd raspberry-pi-gpio-mqtt-controller
```

3. Install the required Python packages:

```
pip3 install -r requirements.txt
```

## Configuration

Edit the `gpio_mqtt_controller.py` file to configure the MQTT broker address and port:

```python
mqtt_broker = "your_mqtt_broker_address"
mqtt_port = 1883
```

Replace `your_mqtt_broker_address` with the address of your MQTT broker.

## Usage

Run the Python script on your Raspberry Pi:

```
python3 gpio_mqtt_controller.py
```

The script will now listen for MQTT messages on topics in the format `{hostname}/GPIO/{pin_number}`. To control the GPIO pins, publish messages to these topics with payloads "1" (for HIGH) or "0" (for LOW).

For example, to set GPIO pin 2 to HIGH, you can use an MQTT client to publish the message with payload "1" to the topic `{hostname}/GPIO/2`, where `{hostname}` is the hostname of your Raspberry Pi.

## Stopping the Script

To stop the script, press `Ctrl+C` in the terminal where the script is running. This will send a KeyboardInterrupt to the script, which will then stop the MQTT client loop and clean up the GPIO resources.

