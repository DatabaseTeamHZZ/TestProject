import socket
import time

import buyer
import cashier
import login
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
        if not data:  # 如果传回的对象不是数据就退出
            break
        feedback = 0
        try:  # 一、登录
            if msg[0] == '0':  # 0——代表登陆失败，请检查用户名，密码，并确保用户名未被注销.1——成功
                feedback = login.login_check(msg[1], msg[2])
                print('客户端地址：%s,消息内容：请求登录用户名： %s ；密码： %s \n' % (str(address), msg[1], msg[2]))  # 格式化输出到控制台
        except Exception:
            feedback = 0  # 用户不存在
        try:  # 二、收银员 msg = [ 2, x, ...]
            if msg[0] == '2':  # 返回  0——失败 1——成功
                if msg[1] == '1':  # 修改用户密码
                    feedback = cashier.change_password(msg[2], msg[3], msg[4])  # x = 1——id, old_password, new_password1
                if msg[1] == '2':  # 修改收银员信息
                    feedback = cashier.change_info(msg[2], msg[3], msg[4])  # x = 2——id, new_name, new_phone
                if msg[1] == '3':  # 注册客户信息，不返回0/1，因为一定成功。返回用户id
                    feedback = cashier.new_customer(msg[2], msg[3])  # x = 3——name, phone
                if msg[1] == '4':  # 交易
                    feedback = cashier.purchase(msg[2], msg[3], msg[4])  # x = 4——customer_id, goods_id, quantity
                if msg[1] == '5':  # 购买VIP点数
                    feedback = cashier.buy_point(msg[2], msg[3])  # x = 5——customer_id, get_point
            if msg[0] == '3':  # 三、进货员 msg = [3, x, ...]
                if msg[1] == '1':  # 修改用户密码
                    feedback = buyer.change_password(msg[2], msg[3], msg[4])  # x = 1——id, old_password, new_password1
                if msg[1] == '2':  # 修改进货员信息
                    buyer.change_info(msg[2], msg[3], msg[4])  # x = 2——id, new_name, new_phone
                if msg[1] == '3':
                    if int(msg[5]) > 5 or int(msg[5]) < 0:  # 创建商品信息 ,返回商品id
                        feedback = 0  # 商品类别的合法性鉴定
                    else:  # x = 3——goods_name, price, cost, goods_type
                        feedback = buyer.new_goods(msg[2], msg[3], msg[4], msg[5])
                if msg[1] == '4':  # 进货（要求所进货物已经被创建）
                    buyer.stock(msg[2], msg[3], msg[4])  # x = 4——goods_id, id, quantity
                    feedback = 1
            if msg[0] == '1':  # 四、管理员 msg = [1, x, ...]
                if msg[1] == '1':
                    if int(msg[3]) < 1 or int(msg[3]) > 3:  # 注册账号，不返回1/0，因为一定成功，返回id
                        feedback = 0
                    else:  # x = 1——password, type
                        feedback = administrator.register(msg[2], msg[3])
                if msg[1] == '2':  # 注销账号，一定成功所以返回1
                    administrator.logout(msg[2])  # x = 2——user_id
                    feedback = 1
                if msg[1] == '3':
                    feedback = administrator.get_customer()
                if msg[1] == '4':
                    feedback = administrator.get_stock()
                if msg[1] == '5':  # 查询一段时间内的销售情况msg[2]=0,销售额降序,msg[2]=1,利润降序,3,4起止时间
                    feedback = administrator.get_sale(msg[2], msg[3], msg[4], msg[5])
                if msg[1] == '6':  # 查询一段时间内的VIP购物记录,msg[3],msg[4]起止时间。按用户VIP等级,id降序
                    feedback = administrator.get_vip_purchase(msg[2], msg[3])
                if msg[1] == '7':
                    feedback = administrator.get_single_goods_info(msg[2])
                if msg[1] == '8':
                    feedback = administrator.modify_single_goods_info(msg[2], msg[3], msg[4], msg[5], msg[6])
                if msg[1] == '9':
                    feedback = administrator.get_every_type_sum_profit(msg[2], msg[3])
                if msg[1] == '10':
                    feedback = administrator.get_every_customer_sum_payment(msg[2], msg[3])
                if msg[1] == '11':
                    feedback = administrator.get_single_customer_point(msg[2])
                if msg[1] == '12':
                    feedback = administrator.get_single_staff_info(msg[2])

        except Exception:
            feedback = 0

        # feedback = ''
        # for j in range(0, 1000):
        #     feedback += '1'
        feedback = str(feedback)
        # 回显消息给客户端
        temp = ''
        print(f'server give \n  {feedback} \n  back')
        lt = list(feedback)
        while len(feedback) > 566:
            for i in range(0, 566):
                temp += feedback[i]
            data_tx = bytes('%s' % temp, encoding='utf8')  # 编码为二进制文件
            connect.send(data_tx)  #

            temp = ''  # 重构 feedback 与 q
            q = ''
            for j in range(566, len(feedback)):
                q += feedback[j]
            feedback = q
            q = ''

        data_tx = bytes('%s' % feedback, encoding='utf8')  # 编码为二进制文件
        connect.send(data_tx)  # 发送
        time.sleep(0.5)  # 休眠的函数需要导入 import time

    # 关闭连接
    connect.close()
    print('客户端地址：%s，连接关闭' % str(address))
