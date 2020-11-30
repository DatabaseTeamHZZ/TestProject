import socket
import time
import  tkinter


#   socket 连接库使用说明：
#   1 返回值为整数0则请求失败，成功则返回整数1或者是所需要的内容。
#   2 从大写 一、 标号开始，都是UI可以直接使用的函数，参数与返回均已标记清楚。
#   3 使用时将此文件导入即可调用。
#   4 函数如果对当前已登录账号进行操作会用到id，所以从登录向主界面跳转时需要传递当前账号id。
#   5 经过修改，不再需要传递socket对象，每次每次函数调用建立的socket对象都是一次性的。只需要直接调用函数即可。
#   6 参数类型可以是字符串也可以是数字任意即可。
#   7 返回参数，除了表示成功或失败的整数0、1 之外，均为有格式的字符串。
#
#   例如：print(modify_account_password(1000, 123, 1234)) 参数依次为id,旧密码，新密码
#        执行结果为 1 说明修改成功 如果执行结果为 0 说明不成功
#        直接调用此函数即可完成远程修改密码的数据库操作。


#   @receive_from_server
#   功   能：从服务器接受消息。得到字符串。
#   参   数：1.sct —— 已经建立连接的socket对象
#   返回参数：失败 —— 0
#           成功 —— 相应内容或1
import tkinter


def receive_from_server(sct):
    feedback = ''
    data_rx = sct.recv(1024)  # 消息的接收格式也应该是二进制

    string2 = '%s' % (data_rx.decode('utf8'))  # 将接受到转码后的字符串返回
    if string2 == '0':
        return 0

    while len(string2) == 566:
        feedback += string2

        data_rx = sct.recv(1024)  # 消息的接收格式也应该是二进制
        string2 = '%s' % (data_rx.decode('utf8'))  # 将接受到转码后的字符串返回

    feedback += string2
    print('接收到消息：%s' % feedback)  # 接收完成后需要转码并且打印
    return feedback


#   @send_to_server
#   功   能：向服务器发送消息，内容为单个字符串。
#   参   数：1.sct —— 已经建立连接的socket对象
#           2.str1 —— 所需要发送的字符串
#   返回参数：失败 —— 0
#           成功 —— 返回建立好连接的一次性socket对象
def send_to_server(str1):
    skt1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
    try:
        skt1.connect(('127.0.0.1', 19200))  # 建立连接:
        data_txt = bytes(str1, encoding='utf8')  # 消息的发送格式应该是二进制
        skt1.send(data_txt)
    except Exception:
        return 0
    return skt1


#   以下为UI可以直接使用的函数
#   一、登录
#   @login_to_server
#   功   能：向服务器发出登录请求。
#   参   数：1.username —— 用户名，字符串
#           2.password —— 密码，字符串
#   返回参数：失败 —— 0
#           成功返回 user_type 指明用户身份
#               1 —— 管理员
#               2 —— 收银员
#               3 —— 进货员
def login_to_server(username, password):  # 接受用户名，密码字符串，返回一个socket对象
    skt1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket实例
    try:
        skt1.connect(('127.0.0.1', 19200))  # 建立连接:
    except Exception:
        return 0

    data_txt = bytes('0' + ' ' + username + ' ' + password, encoding='utf8')  # 消息的发送格式应该是二进制
    skt1.send(data_txt)

    # 接收消息:
    data_rx = skt1.recv(1024)  # 消息的接收格式也应该是二进制
    print('接收到消息：%s' % (data_rx.decode('utf8')))  # 接收完成后需要转码并且打印
    string2 = '%s' % (data_rx.decode('utf8'))  # 将接受到转码后的字符串返回
    if string2 == '0':
        print(tkinter.messagebox.showerror(title='出错啦', message='密码或用户名不正确！'))  # 提出错误对话窗
        return 0
    return int(string2)


#   二、收银员
#   1.修改用户密码
#   @modify_account_password
#   功   能：修改用户密码
#   参   数：1.id1 —— 用户id
#           2.old_password —— 旧密码
#           3.new_password1 —— 新密码
#   返回参数：失败 —— 0
#           成功 —— 1
def modify_account_password(id1, old_password, new_password):
    feedback = send_to_server(f'2 1 {id1} {old_password} {new_password}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   2.修改收银员信息
#   @modify_cashier_info
#   功   能：修改收银员信息
#   参   数：1.id1 —— 用户id
#           2.new_name —— 新名字
#           3.new_phone —— 新电话
#   返回参数：失败 —— 0
#           成功 —— 1
def modify_cashier_info(id1, new_name, new_phone):
    feedback = send_to_server(f'2 2 {id1} {new_name} {new_phone}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   3.注册客户信息
#   @sign_up_new_customer
#   功   能：注册客户信息
#   参   数：1.name —— 新顾客名
#           2.phone —— 新顾客电话
#   返回参数：失败 —— 0
#           成功 —— 顾客id（一定不为0）
def sign_up_new_customer(name, phone):
    feedback = send_to_server(f'2 3 {name} {phone}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   4.交易
#   @purchase
#   功   能：交易
#   参   数：1.customer_id —— 顾客id
#           2.goods_id —— 商品id
#           3.quantity —— 数量
#   返回参数：失败 —— 0
#           成功 —— 顾客id（一定不为0）
def purchase(customer_id, goods_id, quantity):
    feedback = send_to_server(f'2 4 {customer_id} {goods_id} {quantity}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   5.购买VIP点数
#   @buy_point
#   功   能：购买VIP点数
#   参   数：1.customer_id —— 顾客id
#           2.get_point —— 顾客购买点数
#   返回参数：失败 —— 0
#           成功 —— 1
def buy_point(customer_id, get_point):
    feedback = send_to_server(f'2 4 {customer_id} {get_point}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   三、进货员
#   1.修改密码：
#   函数与第74行完全相同

#   2.修改进货员信息
#   @modify_buyer_info
#   功   能：修改进货员信息
#   参   数：1.id1 —— 用户id
#           2.new_name —— 新名字
#           3.new_phone —— 新电话
#   返回参数：失败 —— 0
#           成功 —— 1
def modify_buyer_info(id1, new_name, new_phone):
    feedback = send_to_server(f'3 2 {id1} {new_name} {new_phone}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   3.创建商品信息
#   @create_new_goods
#   功   能：创建商品信息
#   参   数：1.goods_name —— 用户id
#           2.price —— 价格
#           3.cost —— 成本
#           4.goods_type —— 商品类别
#   返回参数：失败 —— 0
#           成功 —— 商品id
def create_new_goods(goods_name, price, cost, goods_type):
    feedback = send_to_server(f'3 3 {goods_name} {price} {cost} {goods_type}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   4.进货（要求所进货物已经被创建）
#   @stock
#   功   能：进货
#   参   数：1.goods_id —— 商品id
#           2.id1 —— 进货员id
#           3.quantity —— 数量
#   返回参数：失败 —— 0
#           成功 —— 1
def stock(goods_id, id1, quantity):
    feedback = send_to_server(f'3 4 {goods_id} {id1} {quantity}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback



#   四、管理员
#   1.注册账号，不返回1/0，因为一定成功，返回id
#   @register
#   功   能：进货
#   参   数：1.password —— 账号密码
#           2.type1 —— 账号类型  1-管理员
#                              2-收银员
#                              3-进货员
#   返回参数：一定成功 —— 账号id
def register(password, type1):
    feedback = send_to_server(f'1 1 {password} {type1}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   2.注销账号
#   @logout
#   功   能：进货
#   参   数：1.user_id —— 用户id
#   返回参数：一定成功 —— 返回1
def logout(user_id):
    feedback = send_to_server(f'1 2 {user_id}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   3.获取顾客信息列表
#   @get_customers_info
#   功   能：获取顾客信息列表
#   参   数：无
#   返回参数：一个字符串，元素由空格分割：格式为
#               第一个元素为返回信息的总条数count
#               此有count组顾客信息，每组顾客信息由三条数据组成
#                   用户id 用户name 用户vip等级
#
#           例如：（以两条客户信息为例）
#               ‘2 id1 name1 VIP_level1 id2 name2 VIP_level2 ’
#
def get_customers_info():
    feedback = send_to_server('1 3')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   4.进货记录
#   @get_stock
#   功   能：获取所有进货记录
#   参   数：无
#   返回参数：一个字符串，元素由空格分割：格式为
#               第一个元素为返回信息的总条数count
#               此后有count组数据，每一组数据由四条数据组成
#                   商品name 商品id 商品数量 进货时间
#               失败 —— 0
#
#           例如：（以两条进货记录为例）
#               ‘2 good_name1 id1 quantity1 time1 good_name2 id2 quantity2 time2’
#
def get_stock():
    feedback = send_to_server('1 4')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   5.查询一段时间内的销售情况
#   @get_sale_in_period
#   功   能：查询一段时间内的销售情况    注——(start_time,end_time]
#   参   数：1.odr —— 排序方式 0-按每种商品的总销售额降序
#                           1-按每种商品的总利润降序
#           2.goods_type 商品类别
#                           -1  全部商品
#                           0	未定义类
#                           1	生活类
#                           2	办公类
#                           3	书籍类
#                           4	电器类
#                           5	饮食类
#
#           2.start_time —— 查询的起始时间 格式为字符串 'yyyy-mm-dd'
#           3.end_time —— 查询结束时间 格式同上
#   返回参数：一个字符串，元素由空格分割：格式为
#               第一个元素为返回销售信息的总条数count
#               第二个元素为总销售额
#               第三个元素为总利润
#               此后有count组数据,每组数据由五条数据组成
#                   商品id 商品name 商品销量 商品销售额 商品利润
#            失败 —— 0
# 
#           例如：（以两条销售记录为例）
#               '2 sum_all_payment sum_all_profit goods_id1 goods_name1 sum_quantity1 sum_payment1 sum_profit1\
#                goods_id2 goods_name2 sum_quantity2 sum_payment2 sum_profit2'
def get_sale_in_period(odr, goods_type, start_time, end_time):
    feedback = send_to_server(f'1 5 {odr} {goods_type} {start_time}-00:00:00 {end_time}-00:00:00')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   6.查询一段时间内各个VIP用户的交易情况
#   @get_vip_sale_in_period
#   功   能：查询一段时间内各个VIP用户的交易情况   注——(start_time,end_time]
#   参   数：1.start_time —— 查询的起始时间 格式为字符串 'yyyy-mm-dd'
#           2.end_time —— 查询结束时间 格式同上
#   返回参数：一个字符串，元素由空格分割：格式为
#               第一个元素为返回销售信息的总条数count
#               此后有count组数据,每组数据由八条数据组成
#                   顾客id 顾客name 顾客phone 商品id 购买数量 时间 交易金额 vip等级
#
#           例如：（以两条销售记录为例）
#               '2 customer_id1 customer_name1 phone1 goods_id1 quantity1 time1 payment1 vip1 \
#               customer_id2 customer_name2 phone2 goods_id2 quantity2 time2 payment2 vip2'
def get_vip_sale_in_period(start_time, end_time):
    feedback = send_to_server(f'1 6 {start_time}-00:00:00 {end_time}-00:00:00')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   7.查询特定商品的信息
#   @get_single_goods_info
#   功   能：通过goods_id查询单个商品的信息
#   参   数：1.goods_id —— 商品的id
#   返回参数：1.goods_name —— 商品名称
#           2.price —— 商品价格
#           3.cost —— 商品成本
#           4.quantity —— 商品存量
#
#           格式示例：
#               'goods_name price cost quantity'
def get_single_goods_info(goods_id):
    feedback = send_to_server(f'1 7 {goods_id}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   8.修改特定的商品信息
#   @modify_single_goods_info
#   功   能：通过goods_id修改商品的name,price,cost,quantity
#   参   数：1.goods_id  —— 商品id
#           2.new_goods_name —— 新的商品名
#           3.new_price —— 新的价格
#           4.new_cost —— 新的成本
#           5.new_quantity —— 新的存量
#   返回参数：1 —— 因为一定成功
def modify_single_goods_info(goods_id, new_goods_name, new_price, new_cost, new_quantity):
    feedback = send_to_server(f'1 8 {goods_id} {new_goods_name} {new_price} {new_cost} {new_quantity}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   9.查询各种商品类型的在一定时间内的总利润排名
#   @get_type_profit
#   功   能：查询一段时间内各种商品类型的总利润排名   注——(start_time,end_time]
#   参   数：1.start_time —— 查询的起始时间 格式为字符串 'yyyy-mm-dd'
#           2.end_time —— 查询结束时间 格式同上
#   返回参数：一个字符串，元素由空格分隔：格式为
#               第一个元素为总商品种类数count
#               此后共有count组数据每组数据由三条数据组成
#                   名次 类型名称 该类型的总利润
#
def get_type_profit(start_time, end_time):
    feedback = send_to_server(f'1 9 {start_time}-00:00:00 {end_time}-00:00:00')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   10.查询所有顾客的在一定时间内的总消费排名
#   @get_customer_consume_rank
#   功   能：查询一段时间所有顾客内总消费排名  注——(start_time,end_time]
#   参   数：1.start_time —— 查询的起始时间 格式为字符串 'yyyy-mm-dd'
#           2.end_time —— 查询结束时间 格式同上
#   返回参数：一个字符串，元素由空格分隔：格式为
#               第一个元素为顾客总数count
#               此后共有count组数据每组数据由三条数据组成
#                   名次 顾客姓名 顾客id 该顾客总消费
#
def get_customer_consume_rank(start_time, end_time):
    feedback = send_to_server(f'1 10 {start_time}-00:00:00 {end_time}-00:00:00')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   11.查询一个特定的顾客的vip点获得记录
#   @get_single_customer_point
#   功   能：查询一个特定的顾客的vip点获得记录
#   参   数：1.customer_id —— 顾客id
#   返回参数：一个字符串，元素由空格分隔：格式为
#               第一个元素为顾客记录总数count
#               此后共有count组数据每组数据由三条数据组成
#                   时间 获得点数 获得方式名称
#
def get_single_customer_point(customer_id):
    feedback = send_to_server(f'1 11 {customer_id}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback


#   12.查询某一未注销员工的个人信息
#   @get_single_staff_info
#   功   能：查询某一未注销员工的个人信息
#   参   数：1.id —— 工作人员id
#   返回参数：一个字符串，元素由空格分隔：格式为
#               第一个元素为员工记录总数count
#               此后共有count组数据每组数据由三条数据组成
#                   姓名 电话 身份名称
#
def get_single_staff_info(id):
    feedback = send_to_server(f'1 12 {id}')
    if feedback == 0:
        return 0
    else:
        feedback = receive_from_server(feedback)
        return feedback

# print(get_single_staff_info(1000))
