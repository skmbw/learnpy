#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import redis


class RedisHelper:
    """redis 工具类"""

    def __init__(self):
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
        self.__conn = redis.StrictRedis(connection_pool=pool)
        # 创建频道
        self.subscribe_channel = 'redis_ros_msg'
        self.publish_channel = 'redis_ros_msg'

    def publish(self, info):
        """发布消息"""
        self.__conn.publish(self.publish_channel, info)
        return True

    def subscribe(self):
        """获取订阅者"""
        pubsub = self.__conn.pubsub()
        pubsub.subscribe(self.subscribe_channel)
        pubsub.parse_response()  # 消息队列的数量
        return pubsub

    def close(self):
        self.__conn.close()
