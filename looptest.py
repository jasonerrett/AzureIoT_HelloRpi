#!/usr/bin/python
import Adafruit_DHT
import datetime
import time

import iothub_client
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
CONNECTION_STRING = "HostName=[iothub_name].azure-devices.net;DeviceId=[devicename_from_iothub];SharedAccessKey=[device_key]"

# Using the MQTT protocol.
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000

# Define the JSON message to send to IoT Hub.
TEMPERATURE = 20.0
HUMIDITY = 60
MSG_TXT = "{\"datetime\":\"%s\",\"temperature\": %.2f,\"humidity\": %.2f}"

def send_confirmation_callback(message, result, user_context):
    print ( "IoT Hub responded to message with status: %s" % (result) )

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

sensor = Adafruit_DHT.DHT22
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
# humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!

def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
            curdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
            if humidity is not None and temperature is not None:
                msg_txt_formatted = MSG_TXT % (curdate, temperature, humidity)
                message = IoTHubMessage(msg_txt_formatted)

                # Add a custom application property to the message.
                # An IoT hub can filter on these properties without access to the message body.
                prop_map = message.properties()
                if temperature > 30:
                    prop_map.add("temperatureAlert", "true")
                else:
                    prop_map.add("temperatureAlert", "false")

                # Send the message.
                print("Sending message: %s" % message.get_string())

                client.send_event_async(message, send_confirmation_callback, None)
            else:
                print('Failed to get reading. Try again!')
            time.sleep(2)

    except IoTHubError as iothub_error:
        print("Unexpected error %s from IoTHub" % iothub_error)
        return
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped")

if __name__ == '__main__':
    print("IoT Hub Quickstart #1 - Simulated device")
    print("Press Ctrl-C to exit")
    iothub_client_telemetry_sample_run()
