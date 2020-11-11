import pymysql

# ↓请修改数据库基本信息↓
host = "127.0.0.1"
host_name = "root"
host_password = "hanxu1125"
database = "b1"


# 1.修改密码
def change_password(id, old_password, new_password):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql1 = "select password from user where id='{}'".format(str(id))
    cursor.execute(sql1)
    res = cursor.fetchone()
    if old_password != res[0]:
        print("原密码输入错误!")
        return 0        # Modified
    else:
        sql2 = "update user set password='{}' where id='{}'".format(new_password, str(id))
        cursor.execute(sql2)
        db.commit()
        print("修改密码成功!")
    db.close()
    return 1            # Modified


# 2.修改个人身份信息
def change_info(id, new_name, new_phone):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "update buyer set name='{}',phone='{}' where id='{}'".format(new_name, new_phone, id)
    cursor.execute(sql)
    db.commit()
    print("个人信息修改成功！")
    db.close()


# 3.创建商品信息
def new_goods(goods_name, price, cost, goods_type):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "insert into goods(goods_name,price,cost,goods_type) values ('{}','{}','{}','{}')".format(goods_name,
                                                                                                    str(price),
                                                                                                    str(cost),
                                                                                                    str(goods_type))
    try:
        cursor.execute(sql)
        db.commit()
    except Exception:
        db.close()
        return 0
    # 创建完成之后获得新商品id
    cursor.execute("select goods_id from goods order by goods_id desc")
    res = cursor.fetchone()
    goods_id = res[0]
    print("商品信息创建完成，商品id为：{}".format(str(goods_id)))
    db.close()
    return goods_id


# 4.进货
def stock(good_id, id, quantity):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "insert into stock(goods_id,id,quantity) values ('{}','{}','{}')".format(str(good_id), str(id), str(quantity))
    cursor.execute(sql)
    db.commit()
    print("进货员id={}进货成功".format(str(id)))
    db.close()
