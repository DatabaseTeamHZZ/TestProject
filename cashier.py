import pymysql

# ↓请修改数据库基本信息↓
host = "127.0.0.1"
host_name = "root"
host_password = ""
database = "b1"


# 1.修改密码
def change_password(id1, old_password, new_password):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql1 = "select password from user where id='{}'".format(str(id1))
    cursor.execute(sql1)
    res = cursor.fetchone()

    result = 0
    if old_password != res[0]:
        print(f"{id1}原密码输入错误!")
        return 0                # Modified

    else:
        sql2 = "update user set password='{}' where id='{}'".format(new_password, str(id1))
        try:
            cursor.execute(sql2)
            db.commit()
        except Exception:
            return result
        result = 1              # Modified
        print(f"{id1}修改密码成功!")
    db.close()
    return result               # Modified


# 2.修改个人身份信息
def change_info(id2, new_name, new_phone):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "update cashier set name='{}',phone='{}' where id='{}'".format(new_name, new_phone, id2)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        return 0
    print("个人信息修改成功！")
    db.close()
    return 1            # Modified


# 3.注册顾客信息
def new_customer(name, phone):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "insert into customer(customer_name,phone) values ('{}','{}')".format(name, phone)
    cursor.execute(sql)
    db.commit()
    # 注册完成之后获得新顾客的id
    cursor.execute("select customer_id from customer order by customer_id desc")
    res = cursor.fetchone()
    customer_id = res[0]
    print("顾客信息注册完成，顾客的id为：{}".format(str(customer_id)))
    db.close()
    return customer_id


# 4.交易
def purchase(customer_id, goods_id, quantity):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    # 先查询商品剩余数量
    sql1 = "select quantity from goods where goods_id='{}'".format(str(goods_id))
    cursor.execute(sql1)
    res1 = cursor.fetchone()
    if int(quantity) > res1[0]:  # 购买数量大于库存，无法实现交易
        print("商品数量过多，无法完成交易！")
        return 0            # Modified
    else:
        # 查询顾客折扣
        sql2 = "select discount from vip_discount natural join customer where customer_id='{}'".format(str(customer_id))
        cursor.execute(sql2)
        res2 = cursor.fetchone()
        discount = res2[0]
        # 查询商品售价、成本
        sql3 = "select price,cost from goods where goods_id='{}'".format(str(goods_id))
        cursor.execute(sql3)
        res3 = cursor.fetchone()
        price = res3[0]
        cost = res3[1]
        # 计算支付金额、交易利润
        payment = int(quantity) * discount * price
        profit = payment - int(quantity) * cost
        # 记录交易
        sql4 = "insert into purchase(customer_id,goods_id,quantity,payment,profit) values('{}','{}','{}','{}','{}')".format(
            str(customer_id), str(goods_id), str(quantity), str(payment), str(profit))
        cursor.execute(sql4)
        db.commit()
        print("交易完成！")
    db.close()
    return 1              # Modified


# 5.顾客直接购买vip点
def buy_point(customer_id, get_point):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "insert into customer_point(customer_id,get_point,way) values ('{}','{}','2')".format(str(customer_id),
                                                                                                str(get_point))
    cursor.execute(sql)
    db.commit()
    print("充值成功")
    db.close()
