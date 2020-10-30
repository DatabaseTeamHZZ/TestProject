import pymysql
#↓请修改数据库基本信息↓
host="127.0.0.1"
host_name="root"
host_password="password"
database="b1"

#1.注册
def register(password,user_type):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql="insert into user(password,user_type) values ('{}','{}')".format(password,str(user_type))
    cursor.execute(sql)
    db.commit()
    #注册完成之后获取新用户id
    cursor.execute("select id from user order by id desc")
    res=cursor.fetchone()
    id=res[0]
    print("注册完成，新用户id为：{}".format(str(id)))
    db.close()
    return id

#2.注销
def logout(id):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql="update user set if_logout='1' where id='{}'".format(str(id))
    cursor.execute(sql)
    db.commit()
    print("已注销用户：id={}".format(str(id)))
    db.close()

#3.查看所有顾客信息（查询示例）
def get_customer():
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql="select customer_id,customer_name,vip from customer"
    cursor.execute(sql)
    res=cursor.fetchall()
    for row in res:
        print("id={}\t姓名={}\tvip等级={}".format(row[0],row[1],row[2]))
    db.close()

#4.查看所有进货记录（查询示例）
def get_stock():
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    #两张表的quantity重名了。。。
    sql="select goods_name,goods_id,stock.quantity,time from stock join goods using(goods_id)"
    cursor.execute(sql)
    res=cursor.fetchall()
    for row in res:
        print("商品：{}(id={})\t进货数量：{}\t进货时间：{}".format(row[0],row[1],row[2],row[3]))
    db.close()
