from redis_helper import RedisHelper
import datetime
import base64
import time_utils

publish = RedisHelper()

# publish.publish('hello world.')

with open('robots.jpg', 'rb') as image_file:
    image_bytes = image_file.read()
    d = datetime.datetime.now()
    # encoded = base64.b64encode(image_bytes).decode('ascii')

# publish.publish(encoded)
# 读取的文件的编码居然是ISO-8859-1, 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
publish.publish(str(image_bytes, encoding='ISO-8859-1'))  # 字节数组转str？时间上跟b64encode差不多
time_utils.millis(datetime.datetime.now(), d)

