from redis_helper import RedisHelper

import datetime
import time
import time_utils

helper = RedisHelper()

redis_sub = helper.subscribe()

while True:
    # 这是使用base64编码，和下面使用字符直接编码，性能差距很小
    # msg = redis_sub.parse_response()
    # d = datetime.datetime.now()
    # base64_bytes = msg[2].encode('ascii')
    # image_bytes = base64.b64decode(base64_bytes)
    # time_utils.millis(datetime.datetime.now(), d)
    # with open('received-image-{}.{}'.format(datetime.datetime.now(), 'jpg'), 'wb') as image_file:
    #     image_file.write(image_bytes)

    for item in redis_sub.listen():
        msg = bytes(item['data'], encoding='ISO-8859-1')
        d = datetime.datetime.now()
        time_utils.millis(datetime.datetime.now(), d)
        with open('received-image-{}.{}'.format(time.time(), 'jpg'), 'wb') as image_file:
            image_file.write(msg)

