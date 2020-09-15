import time

import roslibpy

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

talker = roslibpy.Topic(client, '/chatter', 'std_msgs/String')

while client.is_connected:
    # d = int(time.time())
    talker.publish(roslibpy.Message({'data': 'Hello World!' + str(time.time())}))
    # print(int(time.time()) - d)
    print('Sending message...' + str(time.time()))
    time.sleep(1)

talker.unadvertise()

client.terminate()
