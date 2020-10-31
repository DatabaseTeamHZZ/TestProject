import socket
import time

import login
import cashier
import buyer
import administrator


def receive_from_server(sct):
    data_rx = sct.recv(1024)  # 消息的接收格式也应该是二进制
    print('接收到消息：%s' % (data_rx.decode('utf8')))  # 接收完成后需要转码并且打印
    string2 = '%s' % (data_rx.decode('utf8'))  # 将接受到转码后的字符串返回
    return string2


def send_to_server(sct, str1):
    data_txt = bytes(str1, encoding='utf8')  # 消息的发送格式应该是二进制
    sct.send(data_txt)


def login_to_server(username, password):  # 接受用户名，密码字符串，返回一个socket对象，但是，
    skt1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
    skt1.connect(('127.0.0.1', 19200))  # 建立连接:

    data_txt = bytes(0 + ' ' + username + ' ' + password, encoding='utf8')  # 消息的发送格式应该是二进制
    skt1.send(data_txt)

    # 接收消息:
    data_rx = skt1.recv(1024)  # 消息的接收格式也应该是二进制
    print('接收到消息：%s' % (data_rx.decode('utf8')))  # 接收完成后需要转码并且打印
    string2 = '%s' % (data_rx.decode('utf8'))  # 将接受到转码后的字符串返回
    if string2 == 0:
        return 0
    return skt1


def check_log(user_name, pwd):
    return login.login_check(user_name, pwd)


skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket连接的端口等待连接
skt.bind(('127.0.0.1', 19200))  # 绑定端口
skt.listen(100)  # 监听端口

while True:
    # 等待连接
    print('\n等待连接......')
    connect, address = skt.accept()  # 接收到信息后继续执行
    print('客户端地址：%s，建立连接' % str(address))
    print('connect实例: ', connect)

    while True:
        # 等待消息
        data = connect.recv(1024)  # 接受二进制编码
        msg = data.decode('utf8')  # 将二进制编码转码
        msg = msg.split()  # 分割为元组
        while len(msg) < 3:
            msg.append('0')
        if not data:  # 如果传回的对象不是数据就退出
            break

        try:
            if msg == '0':  # 0代表登陆失败，请检查用户名，密码，并确保用户名未被注销
                feedback = check_log(msg[1], msg[2])
                print('客户端地址：%s,消息内容：请求登录用户名： %s ；密码： %s \n' % (str(address), msg[1], msg[2]))  # 格式化输出到控制台

        except Exception:
            feedback = 0  # 用户不存在

        # 回显消息给客户端
        data_tx = bytes('%s' % feedback, encoding='utf8')  # 编码为二进制文件
        connect.send(data_tx)  # 发送
        time.sleep(0.5)  # 休眠的函数需要导入 import time

    # 关闭连接
    connect.close()
    print('客户端地址：%s，连接关闭' % str(address))
