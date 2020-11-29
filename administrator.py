import pymysql

# 改动内容：操作5：增加了一个参数
#        添加了4种操作：查询各种商品类型的在一定时间内的总利润排名
#                    查询所有顾客的在一定时间内的总消费排名
#                    查询一个特定的顾客的vip点获得记录
#                    查询某一未注销员工的个人信息


# ↓请修改数据库基本信息↓
host = "127.0.0.1"
host_name = "root"
host_password = "hanxu1125"
database = "b1"


# 1.注册
def register(password, user_type):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "insert into user(password,user_type) values ('{}','{}')".format(password, str(user_type))
    cursor.execute(sql)
    db.commit()
    # 注册完成之后获取新用户id
    cursor.execute("select id from user order by id desc")
    res = cursor.fetchone()
    id = res[0]
    print("注册完成，新用户id为：{}".format(str(id)))
    db.close()
    return id


# 2.注销
def logout(id):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "update user set if_logout='1' where id='{}'".format(str(id))
    cursor.execute(sql)
    db.commit()
    print("已注销用户：id={}".format(str(id)))
    db.close()


# 3.查看所有顾客信息（查询示例）
def get_customer():
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select customer_id,customer_name,vip from customer"
    cursor.execute(sql)
    res = cursor.fetchall()
    count = 0
    feedback = ''  # feedback = count id1 name1 VIP_level1 id2 name2 VIP_level2
    for row in res:  # Modified
        print("id={}\t姓名={}\tvip等级={}".format(row[0], row[1], row[2]))
        feedback = feedback + "{} {} {} ".format(row[0], row[1], row[2])  # id, name, VIP level
        count = count + 1
    if count == 0:
        db.close()
        return 0
    feedback = f"{count} " + feedback
    db.close()
    return feedback


# 4.查看所有进货记录（查询示例）
def get_stock():
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    # 两张表的quantity重名了。。。
    sql = "select goods_name,goods_id,stock.quantity,time from stock join goods using(goods_id) "
    cursor.execute(sql)
    res = cursor.fetchall()
    count = 0
    feedback = ''  # feedback = count good_name1, id1, quantity1, time1 ...
    for row in res:
        print("商品：{}(id={})\t进货数量：{}\t进货时间：{}".format(row[0], row[1], row[2], row[3]))
        feedback = feedback + "{} {} {} {} ".format(row[0], row[1], row[2], row[3])
        count = count + 1
    if count == 0:
        db.close()
        return 0
    feedback = f"{count} " + feedback
    db.close()
    return feedback


# 目前还待完善的功能有——1.查询一段时间内的销售情况                             √
#                   2.查询一段时间内的利润        最终决定,1,2合并           √
#                   3.查询各个VIP客户的销售记录                            √
#                   4.查询各种商品的销售量——以销售总销售额来排行  1,2,4全部合并 √

# 5.查询一段时间内的销售情况
# 补充：可以加入同一类型商品的内部销售排名
#      若参数goods_type=-1，则返回全部商品的销售排名
#      若goods_type=0,1,2,3,4,5...，则返回该类型下的所有商品排名
#      以上补充不会影响返回值格式,但是前端输入时要多增加一个int参数
def get_sale(odr, goods_type=-1, start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    start_time = '\'' + start_time + '\''
    end_time = '\'' + end_time + '\''

    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()

    order = ''
    if odr == 0 or odr == '0':
        order = 'order by sum_payment desc'
    else:
        order = 'order by sum_profit desc'

    tp = ''
    if goods_type != -1:
        tp = 'and goods_type={}'.format(goods_type)
    if goods_type == '-1':
        tp = ''

    # 两张表的quantity重名了。。。
    sql = "select goods_id, goods_name,sum(purchase.quantity) sum_quantity, sum(payment) sum_payment, sum(profit) " \
          f"sum_profit from purchase join goods using(goods_id) where time > {start_time} and time < {end_time} {tp} group " \
          f"by goods_id, goods_name {order} "
    cursor.execute(sql)
    res = cursor.fetchall()
    count = 0
    feedback = ''

    sum_all_payment = 0
    sum_all_profit = 0
    # feedback = count sum_all_payment sum_all_profit goods_id1, goods_name1, sum_quantity1, sum_payment1, sum_profit1 .
    for row in res:
        print(
            "goods_id={}\tgoods_name={}\tsum_quantity={}\tsum_payment={}\tsum_profit={}".format(row[0], row[1], row[2],
                                                                                                row[3], row[4]))
        feedback = feedback + "{} {} {} {} {} ".format(row[0], row[1], row[2], row[3], row[4])
        count = count + 1
        sum_all_payment = sum_all_payment + row[3]
        sum_all_profit = sum_all_profit + row[4]
    if count == 0:
        db.close()
        return 0
    feedback = f"{count} {sum_all_payment} {sum_all_profit} " + feedback
    db.close()
    return feedback


# 6.查询各个VIP 用户的交易记录
def get_vip_purchase(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    start_time = '\'' + start_time + '\''  # added!!
    end_time = '\'' + end_time + '\''
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    # 两张表的quantity重名了。。。
    sql = "select customer_id,customer_name,phone,goods_id,quantity,time,payment,vip from purchase join customer " \
          f"using(customer_id) where time > {start_time} and time < {end_time} order by vip,customer_id desc "
    cursor.execute(sql)
    res = cursor.fetchall()
    count = 0
    feedback = ''

    # feedback = count customer_id,customer_name,phone,goods_id,quantity,time,payment,vip ....
    for row in res:
        feedback = feedback + "{} {} {} {} {} {} {} {} ".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                                row[7])
        count = count + 1
    if count == 0:
        db.close()
        return 0
    feedback = f"{count} " + feedback
    # print(feedback)
    db.close()
    return feedback


#   7.查询一个特定的商品信息
def get_single_goods_info(goods_id):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = f"select goods_name,price,cost,quantity from goods where goods_id={goods_id}"
    cursor.execute(sql)
    res = cursor.fetchall()
    count = 0
    feedback = ''  # feedback = goods_name price cost quantity
    for row in res:
        print("goods_name={}\tprice={}\tcost={}\tquantity={}".format(row[0], row[1], row[2], row[3]))
        feedback = feedback + "{} {} {} {} ".format(row[0], row[1], row[2], row[3])  # goods_name,price,cost,quantity
        count = count + 1
    if count == 0:
        db.close()
        return 0
    db.close()
    return feedback


#   8.修改特定商品的信息
def modify_single_goods_info(goods_id, new_goods_name, new_price, new_cost, new_quantity):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = f"update goods set goods_name ='{new_goods_name}',price={new_price},cost={new_cost},quantity={new_quantity} \
        where goods_id='{goods_id}' "
    cursor.execute(sql)
    db.commit()
    print("已完成商品信息修改：goods_id={}".format(str(goods_id)))
    db.close()
    return 1


# 补充

#   9.查询各种商品类型的在一定时间内的总利润排名
def get_every_type_sum_profit(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select type_name,sum(profit)sum_profit from (goods natural join goods_type_name) join purchase using(goods_id)\
         where time>'{}' and time <'{}' group by goods_type order by sum_profit desc".format(start_time, end_time)
    cursor.execute(sql)
    res = cursor.fetchall()
    feedback = ''  # feedback = 名次 类型名称 该类型的总利润
    rank = 0
    for row in res:
        rank = rank + 1
        print("rank={}\tgoods_type={}\tsum_profit={}".format(rank, row[0], row[1]))
        feedback = feedback + "{} {} {} ".format(rank, row[0], row[1])
    feedback = f'{rank} {feedback}'
    db.close()
    if rank == 0:
        return 0
    return feedback


#   10.查询所有顾客的在一定时间内的总消费排名
def get_every_customer_sum_payment(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select customer_name,customer_id,sum(payment)sum_payment from customer natural join purchase \
        where time>'{}' and time<'{}' group by customer_id order by sum_payment desc".format(start_time, end_time)
    cursor.execute(sql)
    res = cursor.fetchall()
    feedback = ''  # feedback = 名次 顾客姓名 顾客id 该顾客总消费
    rank = 0
    for row in res:
        rank = rank + 1
        print("rank={}\tcustomer_name={}\tcustoer_id={}\tsum_payment={}".format(rank, row[0], row[1], row[2]))
        feedback = feedback + "{} {} {} ".format(rank, row[0], row[1], row[2])
    db.close()
    feedback = f'{rank} {feedback}'
    if rank == 0:
        return 0
    return feedback


#   11.查询一个特定的顾客的vip点获得记录
def get_single_customer_point(customer_id):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select time,get_point,way_name from customer_point natural join get_point_way where customer_id={}".format(
        customer_id)
    cursor.execute(sql)
    res = cursor.fetchall()
    feedback = ''  # feedback = 时间 获得点数 获得方式名称
    count = 0
    for row in res:
        print("time={}\tget_point={}\tway_name={}".format(row[0], row[1], row[2]))
        feedback = feedback + "{} {} {} ".format(row[0], row[1], row[2])
        count = count + 1
    db.close()
    feedback = f'{count} {feedback}'
    if count == 0:
        return 0
    return feedback


#   12.查询某一未注销员工的个人信息（可以将【注销】嵌入到该操作界面之中）
def get_single_staff_info(id):

    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select name,phone,user_type_name from user natural join user_type_name natural left outer join \
        (select *  from buyer union  select *  from cashier) as staff where if_logout=0 and id='{}'".format(id)
    cursor.execute(sql)
    res = cursor.fetchall()
    feedback = ''  # feedback = 姓名 电话 身份名称
    count = 0
    for row in res:
        print("name={}\tphone={}\ttype={}".format(row[0], row[1], row[2]))
        feedback = feedback + "{} {} {} ".format(row[0], row[1], row[2])
        count = count + 1
    db.close()
    feedback = f'{count} {feedback}'
    if count == 0:
        return 0
    return feedback
