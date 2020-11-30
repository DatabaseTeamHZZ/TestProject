import administrator
import buyer
import cashier
import login


id = int(input("账号： "))
password = input("密码： ")
user_type = login.login_check(id, password)
# 0：登陆失败
if user_type == 0:
    print("登陆失败")

# 2：收银员
elif user_type == 2:
    action = int(input("行为代号："))

    if action == 1:  # 1.修改密码
        old_password = input("输入原密码：")
        new_password1 = input("输入新密码：")
        new_password2 = input("再次输入新密码：")
        if new_password1 != new_password2:
            print("两次输入的新密码不同")
        else:
            cashier.change_password(id, old_password, new_password1)

    elif action == 2:  # 2.修改个人身份信息
        new_name = input("输入姓名：")
        new_phone = input("输入联系方式：")
        cashier.change_info(id, new_name, new_phone)

    elif action == 3:  # 3.注册顾客信息
        name = input("顾客姓名：")
        phone = input("顾客联系方式：")
        customer_id = cashier.new_customer(name, phone)

    elif action == 4:  # 4.交易
        customer_id = int(input("顾客id："))
        goods_id = int(input("商品id："))
        quantity = int(input("购买数量："))
        cashier.purchase(customer_id, goods_id, quantity)

    elif action == 5:  # 5.购买VIP点数
        customer_id = int(input("顾客id："))
        get_point = int(input("购买vip点数："))
        cashier.buy_point(customer_id, get_point)

# 3：进货员
elif user_type == 3:
    action = int(input("行为代号："))

    if action == 1:  # 1.修改密码
        old_password = input("输入原密码：")
        new_password1 = input("输入新密码：")
        new_password2 = input("再次输入新密码：")
        if new_password1 != new_password2:
            print("两次输入的新密码不同")
        else:
            buyer.change_password(id, old_password, new_password1)

    elif action == 2:  # 2.修改个人身份信息
        new_name = input("输入姓名：")
        new_phone = input("输入联系方式：")
        buyer.change_info(id, new_name, new_phone)

    elif action == 3:  # 3.创建商品信息
        goods_name = input("商品名称：")
        price = float(input("商品售价："))
        cost = float(input("商品成本："))
        goods_type = int(input("商品类型："))
        if goods_type > 5 or goods_type < 0:
            print("商品类型不存在！")
        else:
            goods_id = buyer.new_goods(goods_name, price, cost, goods_type)

    elif action == 4:  # 4.进货
        goods_id = int(input("商品id："))
        quantity = int(input("进货数量："))
        buyer.stock(goods_id, id, quantity)


# 1：管理员
elif user_type == 1:
    action = int(input("行为代号："))

    if action == 1:  # 1.注册
        password = input("初始密码：")
        type = int(input("用户类型："))
        if type < 1 or type > 3:
            print("用户种类不存在！")
        else:
            id = administrator.register(password, type)

    elif action == 2:  # 2.注销
        user_id = int(input("用户id："))
        administrator.logout(user_id)

    elif action == 3:  # 3.查看所有顾客信息（查询示例）
        administrator.get_customer()

    elif action == 4:  # 4.查看所有进货记录（查询示例）
        administrator.get_stock()
