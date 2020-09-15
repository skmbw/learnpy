# Python Learning

# 安装依赖库
* 安装客户端依赖，支持python2或python3
```shell script
sudo pip3 install redis # redis不是rosbridge的依赖，只是项目中所使用
sudo pip3 install roslibpy
```

# 运行环境
* 安装rosbridge server端，是一个ROS package
```shell script
sudo apt-get install -y ros-kinetic-rosbridge-server
sudo apt-get install -y ros-kinetic-tf2-web-republisher
```
* 如果要运行rosbridge部分，需要启动server守护进程
```shell script
roslaunch rosbridge_server rosbridge_websocket.launch
rosrun tf2_web_republisher tf2_web_republisher # 如果需要tf2的话
```
* 如果要运行redis部分代码，需要启动redis
    + 安装redis，sudo apt install redis，会同时安装redis-server，redis-cli

# 测试结论
* rosbridge功能完善，可以和ros通信，获取ros的各种信息，适用于异构系统之间的交互。
* rosbridge提供了js，java，python三种客户端，客户端独立于ROS，但是rosbridge的server端是依赖ROS的，需要运行roscore（master节点）
* rosbridge使用json文本协议，所以传输图片或者视频，是一个问题。需要将图片压缩成字符串，性能损失较大
* redis的pubsub性能和rosbridge不相上下，是可以使用的，稳定性也是有保障的
* redis的pubsub也是传输的str，所以有和rosbridge json协议，相同的问题，不过如果使用opencv抓取数据，是否可以避免这个问题，待确认？
* rosbridge提供了png格式的图片压缩，只是减少了传输的数据量

# 一些问题
### 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
* 这个是因为字符编码不正确导致的，python读取文件，使用的是ISO-8859-1编码，so，使用ISO-8859-1就行了

### 字符串str和bytes转换
* bytes编码成base64和bytes直接转成str，对于python来说性能差距很小
* redis pubsub和rosbridge通信的性能比较高，瓶颈在编码成字符串，以及解码字符串上