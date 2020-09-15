import base64
import logging
import time
import datetime

import roslibpy

import time_utils

# Configure logging
fmt = '%(asctime)s %(levelname)8s: %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
log = logging.getLogger(__name__)

client = roslibpy.Ros(host='127.0.0.1', port=9090)

publisher = roslibpy.Topic(client, '/camera/image/compressed', 'sensor_msgs/CompressedImage')
publisher.advertise()


def publish_image():
    with open('robots.jpg', 'rb') as image_file:
        image_bytes = image_file.read()
        d = datetime.datetime.now()
        encoded = base64.b64encode(image_bytes).decode('ascii')

    publisher.publish(dict(format='jpeg', data=encoded))
    time_utils.millis(datetime.datetime.now(), d)


client.on_ready(publish_image)
client.run_forever()
