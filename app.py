import os
import random
import sys
import time
from pms5003 import PMS5003
from os.path import join, dirname
from dotenv import load_dotenv
from Adafruit_IO import MQTTClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

pms5003 = PMS5003(
    device=os.environ.get("PMS5003_DEVICE"),
    baudrate=os.environ.get("PMS5003_BAUDRATE"),
    pin_enable=int(os.environ.get("PMS5003_PIN_ENABLE")),
    pin_reset=int(os.environ.get("PMS5003_PIN_RESET"))
)


def connected(client):
    print('Listening for changes on ', os.environ.get("ADAFRUIT_GROUP_NAME"))
    client.subscribe_group(os.environ.get("ADAFRUIT_GROUP_NAME"))


def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, topic_id, payload):
    print('Topic {0} received new value: {1}'.format(topic_id, payload))


client = MQTTClient(os.environ.get("ADAFRUIT_IO_USERNAME"), os.environ.get("ADAFRUIT_IO_KEY"))

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()

client.loop_background()

while True:
    data = pms5003.read()
    print('Publishing {0} to {1}.{2}.'.format(data.pm_ug_per_m3(1.0), os.environ.get("ADAFRUIT_GROUP_NAME"),
                                              os.environ.get("ADAFRUIT_GROUP_FEED_PM1")))
    client.publish(os.environ.get("ADAFRUIT_GROUP_FEED_PM1"), data.pm_ug_per_m3(1.0),
                   os.environ.get("ADAFRUIT_GROUP_NAME"))

    print('Publishing {0} to {1}.{2}.'.format(data.pm_ug_per_m3(2.5), os.environ.get("ADAFRUIT_GROUP_NAME"),
                                              os.environ.get("ADAFRUIT_GROUP_FEED_PM2.5")))
    client.publish(os.environ.get("ADAFRUIT_GROUP_FEED_PM2.5"), data.pm_ug_per_m3(2.5),
                   os.environ.get("ADAFRUIT_GROUP_NAME"))

    print('Publishing {0} to {1}.{2}.'.format(data.pm_ug_per_m3(10), os.environ.get("ADAFRUIT_GROUP_NAME"),
                                              os.environ.get("ADAFRUIT_GROUP_FEED_PM10")))
    client.publish(os.environ.get("ADAFRUIT_GROUP_FEED_PM10"), data.pm_ug_per_m3(10),
                   os.environ.get("ADAFRUIT_GROUP_NAME"))
    time.sleep(10)
