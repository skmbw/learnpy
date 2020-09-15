# Python Learning

# 依赖库
* 安装依赖
```shell script
sudo pip3 install redis 
sudo pip3 install rosbridge_server
```

# 运行环境
* 如果要运行rosbridge部分，需要启动
```shell script
roslaunch rosbridge_server rosbridge_websocket.launch
```
* 如果要运行redis部分代码，需要启动redis

# 测试结论
* rosbridge功能完善，可以和ros通信，获取ros的各种信息，适用于异构系统之间的交互。
* rosbridge提供了js，java，python三种客户端，客户端独立于ROS，但是rosbridge的server端是依赖ROS的，需要运行roscore（master节点）
* rosbridge使用json文本协议，所以传输图片或者视频，是一个问题。需要将图片压缩成字符串，性能损失较大
* redis的pubsub性能和rosbridge不相上下，是可以使用的，稳定性也是有保障的
* redis的pubsub也是传输的str，所以有和rosbridge json协议，相同的问题，不过如果使用opencv抓取数据，是否可以避免这个问题，待确认？