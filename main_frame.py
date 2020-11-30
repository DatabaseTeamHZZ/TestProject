from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import login
import cashier
import pymysql
import buyer
import administrator
import connectlib

# ↓请修改数据库基本信息↓

host = "127.0.0.1"
host_name = "root"
host_password = "hanxu1125"
database = "b1"

type_user = -1  # 用户类型
uid = ''


# 登陆界面
class MY_GUI():
    def __init__(self):  # 类似于构造器，将TK窗口作为成员对象初始化进来
        pass

    def click_login(self):
        name = self.entry_usr_name.get()
        password = self.entry_usr_pwd.get()
        self.userid = name
        self.user_type = connectlib.login_to_server(name, password)
        if (self.user_type != 0):
            self.window.destroy()

    def login_window(self):
        self.window = tk.Tk()
        self.window.title('欢迎来到商品进销与人员管理系统')
        self.window.geometry('400x200')
        # 用户信息
        tk.Label(self.window, text='用户名:', font=('潮字社国风冉宋简-闪', 14)).place(x=10, y=50)
        tk.Label(self.window, text='密码:', font=('潮字社国风冉宋简-闪', 14)).place(x=10, y=100)
        # 用户名
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name, font=('潮字社国风冉宋简-闪', 14))
        self.entry_usr_name.place(x=120, y=50)
        # 用户密码
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, font=('潮字社国风冉宋简-闪', 14), show='*')
        self.entry_usr_pwd.place(x=120, y=100)
        self.user_id = -1
        # login 按钮
        self.btn_login = tk.Button(self.window, text='登录', font='潮字社国风冉宋简-闪', command=self.click_login)
        self.btn_login.place(x=170, y=150)
        # 主窗口循环显示
        self.window.mainloop()


def login_start():
    run = MY_GUI()  # 传入TK窗口
    run.login_window()  # 设置根窗口默认属性
    global type_user
    global uid
    type_user = run.user_type
    uid = run.userid


if __name__ == '__main__':  # 如果是命令行直接运行则开始运行，否则不执行
    login_start()

################################################

# 主界面
root = Tk()
root.title('欢迎来到商品进销管理系统')  # 主界面名称
root.geometry('800x494')

tab_main = ttk.Notebook()  # 创建分页栏
tab_main.place(relx=0, rely=0, relwidth=1, relheight=1)

tab1 = Frame(tab_main)  # 创建收银员界面
tab1.place(x=30, y=30)
tab_main.add(tab1, text='修改密码')  # 将第一页插入分页栏中

tab2 = Frame(tab_main)  # 创建收银员界面
tab2.place(x=30, y=30)
tab_main.add(tab2, text='修改个人资料')  # 将第一页插入分页栏中

tab3 = Frame(tab_main)  # 创建收银员界面
tab3.place(x=30, y=30)
tab_main.add(tab3, text='交易')  # 将第一页插入分页栏中

tab4 = Frame(tab_main)  # 创建收银员界面
tab4.place(x=30, y=30)
tab_main.add(tab4, text='购买点数')  # 将第一页插入分页栏中

tab5 = Frame(tab_main)  # 创建收银员界面
tab5.place(x=30, y=30)
tab_main.add(tab5, text='添加顾客')  # 将第一页插入分页栏中

##########
# 收 银 员 界 面 #
##########

# 1，更改密码：
# tk.Label(tab1, text='请输入 id:', font=('Arial', 13)).place(x=50, y=40)
# cashier_id = tk.StringVar()
# cashier_name = tk.Entry(tab1, textvariable=cashier_id, font=('Arial', 14))
# cashier_name.place(x=200, y=40)
tk.Label(tab1, text='请输入旧密码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
cashier_old_pwd = tk.StringVar()
enter_old_pwd = tk.Entry(tab1, textvariable=cashier_old_pwd, font=('潮字社国风冉宋简-闪', 16), show='*')
enter_old_pwd.place(relx=0.46, rely=0.2)
tk.Label(tab1, text='请输入新密码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
cashier_new_pwd = tk.StringVar()
enter_new_pwd = tk.Entry(tab1, textvariable=cashier_new_pwd, font=('潮字社国风冉宋简-闪', 16), show='*')
enter_new_pwd.place(relx=0.46, rely=0.4)
change_pwd_btn = tk.Button(tab1, text='修改密码', font=('潮字社国风冉宋简-闪', 16),
                           command=lambda: connectlib.modify_account_password(uid, enter_old_pwd.get(),
                                                                              enter_new_pwd.get()))
change_pwd_btn.place(relx=0.45, rely=0.6)

# 2，修改个人信息
# tk.Label(tab2, text='请输入id:', font=('Arial', 13)).place(x=50, y=40)
# cashier_cname = tk.StringVar()
# enter_name = tk.Entry(tab2, textvariable=cashier_cname, font=('Arial', 14))
# enter_name.place(x=200, y=40)
tk.Label(tab2, text='请输入新用户名:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
cashier_new_name = tk.StringVar()
enter_new_name = tk.Entry(tab2, textvariable=cashier_new_name, font=('潮字社国风冉宋简-闪', 16))
enter_new_name.place(relx=0.46, rely=0.2)
tk.Label(tab2, text='请输入新手机号码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
cashier_new_phone = tk.StringVar()
enter_new_phone = tk.Entry(tab2, textvariable=cashier_new_phone, font=('潮字社国风冉宋简-闪', 16))
enter_new_phone.place(relx=0.46, rely=0.4)
change_info_btn = tk.Button(tab2, text='修改个人信息', font=('潮字社国风冉宋简-闪', 16),
                            command=lambda: connectlib.modify_cashier_info(uid, enter_new_name.get(),
                                                                           enter_new_phone.get()))
change_info_btn.place(relx=0.45, rely=0.6)

# 3，交易：
tk.Label(tab3, text='请输入顾客id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
customer_id = tk.StringVar()
enter_customer_id = tk.Entry(tab3, textvariable=customer_id, font=('潮字社国风冉宋简-闪', 16))
enter_customer_id.place(relx=0.46, rely=0.2)
tk.Label(tab3, text='请输入商品号:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
goods_id = tk.StringVar()
enter_goods_id = tk.Entry(tab3, textvariable=goods_id, font=('潮字社国风冉宋简-闪', 16))
enter_goods_id.place(relx=0.46, rely=0.35)
tk.Label(tab3, text='请输入交易数量:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.5)
quantity = tk.StringVar()
enter_quantity = tk.Entry(tab3, textvariable=quantity, font=('潮字社国风冉宋简-闪', 16))
enter_quantity.place(relx=0.46, rely=0.5)
purchase_btn = tk.Button(tab3, text='交易', font=('潮字社国风冉宋简-闪', 16),
                         command=lambda: connectlib.purchase(enter_customer_id.get(), enter_goods_id.get(),
                                                             enter_quantity.get()))
purchase_btn.place(relx=0.45, rely=0.65)

# 4，购买点数
tk.Label(tab4, text='请输入顾客id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
customer_id2 = tk.StringVar()
enter_customer_id2 = tk.Entry(tab4, textvariable=customer_id2, font=('潮字社国风冉宋简-闪', 16))
enter_customer_id2.place(relx=0.46, rely=0.2)
tk.Label(tab4, text='请输入购买点数:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
point = tk.StringVar()
enter_point = tk.Entry(tab4, textvariable=point, font=('潮字社国风冉宋简-闪', 16))
enter_point.place(relx=0.46, rely=0.4)
get_point = tk.Button(tab4, text='购买点数', font=('潮字社国风冉宋简-闪', 16),
                      command=lambda: connectlib.buy_point(enter_customer_id2.get(), enter_point.get()))
get_point.place(relx=0.45, rely=0.6)

# 5，添加顾客
tk.Label(tab5, text='请输入顾客名称:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
customer_name = tk.StringVar()
enter_customer_name = tk.Entry(tab5, textvariable=customer_name, font=('潮字社国风冉宋简-闪', 16))
enter_customer_name.place(relx=0.46, rely=0.2)
tk.Label(tab5, text='请输入顾客电话:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
customer_phone = tk.StringVar()
enter_customer_phone = tk.Entry(tab5, textvariable=customer_phone, font=('潮字社国风冉宋简-闪', 16))
enter_customer_phone.place(relx=0.46, rely=0.4)
register_customer = tk.Button(tab5, text='注册顾客', font=('潮字社国风冉宋简-闪', 16),
                              command=lambda: connectlib.sign_up_new_customer(enter_customer_name.get(),
                                                                              enter_customer_phone.get()))
register_customer.place(relx=0.45, rely=0.6)

tab6 = Frame(tab_main)
tab6.place(x=30, y=30)
tab_main.add(tab6, text='修改密码')
tab7 = Frame(tab_main)
tab7.place(x=30, y=30)
tab_main.add(tab7, text='修改个人资料')
tab8 = Frame(tab_main)
tab8.place(x=30, y=30)
tab_main.add(tab8, text='添加商品信息')
tab9 = Frame(tab_main)
tab9.place(x=30, y=30)
tab_main.add(tab9, text='进货')
tab22 = Frame(tab_main)
tab22.place(x=30, y=30)
tab_main.add(tab22, text='查看商品库存')

##########
# 进 货 员 界 面 #
##########

# 1，修改密码
# tk.Label(tab6, text='请输入 id:', font=('Arial', 13)).place(x=50, y=40)
# buyer_id = tk.StringVar()
# enter_buyer_id = tk.Entry(tab6, textvariable=buyer_id, font=('Arial', 14))
# enter_buyer_id.place(x=200, y=40)
tk.Label(tab6, text='请输入旧密码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
buyer_old_pwd = tk.StringVar()
enter_buyer_old_pwd = tk.Entry(tab6, textvariable=buyer_old_pwd, font=('潮字社国风冉宋简-闪', 16), show='*')
enter_buyer_old_pwd.place(relx=0.46, rely=0.2)
tk.Label(tab6, text='请输入新密码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
buyer_new_pwd = tk.StringVar()
enter_buyer_new_pwd = tk.Entry(tab6, textvariable=buyer_new_pwd, font=('潮字社国风冉宋简-闪', 16), show='*')
enter_buyer_new_pwd.place(relx=0.46, rely=0.4)
change_buyer_pwd_btn = tk.Button(tab6, text='修改密码', font=('潮字社国风冉宋简-闪', 16),
                                 command=lambda: connectlib.modify_account_password(uid,
                                                                                    enter_buyer_old_pwd.get(),
                                                                                    enter_buyer_new_pwd.get()))
change_buyer_pwd_btn.place(relx=0.45, rely=0.6)

# 2，修改个人信息
# tk.Label(tab7, text='请输入id:', font=('Arial', 13)).place(x=50, y=40)
# buyer_cname = tk.StringVar()
# enter_buyer_name = tk.Entry(tab7, textvariable=buyer_cname, font=('Arial', 14))
# enter_buyer_name.place(x=200, y=40)
tk.Label(tab7, text='请输入新用户名:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
buyer_new_name = tk.StringVar()
enter_buyer_new_name = tk.Entry(tab7, textvariable=buyer_new_name, font=('潮字社国风冉宋简-闪', 16))
enter_buyer_new_name.place(relx=0.46, rely=0.2)
tk.Label(tab7, text='请输入新手机号码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
buyer_new_phone = tk.StringVar()
enter_buyer_new_phone = tk.Entry(tab7, textvariable=buyer_new_phone, font=('潮字社国风冉宋简-闪', 16))
enter_buyer_new_phone.place(relx=0.46, rely=0.4)
change_buyer_info_btn = tk.Button(tab7, text='修改个人信息', font=('潮字社国风冉宋简-闪', 16),
                                  command=lambda: connectlib.modify_buyer_info(uid,
                                                                               enter_buyer_new_name.get(),
                                                                               enter_buyer_new_phone.get()))
change_buyer_info_btn.place(relx=0.45, rely=0.6)

# 3，添加商品
tk.Label(tab8, text='请输入商品名称:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
goods_name0 = tk.StringVar()
enter_goods_name0 = tk.Entry(tab8, textvariable=goods_name0, font=('潮字社国风冉宋简-闪', 16))
enter_goods_name0.place(relx=0.46, rely=0.2)
tk.Label(tab8, text='请输入商品售价:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
goods_price0 = tk.StringVar()
enter_goods_price0 = tk.Entry(tab8, textvariable=goods_price0, font=('潮字社国风冉宋简-闪', 16))
enter_goods_price0.place(relx=0.46, rely=0.35)
tk.Label(tab8, text='请输入商品成本:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.5)
goods_cost0 = tk.StringVar()
enter_goods_cost0 = tk.Entry(tab8, textvariable=goods_cost0, font=('潮字社国风冉宋简-闪', 16))
enter_goods_cost0.place(relx=0.46, rely=0.5)
tk.Label(tab8, text='请输入商品类型:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.65)
goods_type0 = tk.StringVar()
enter_goods_type0 = tk.Entry(tab8, textvariable=goods_type0, font=('潮字社国风冉宋简-闪', 16))
enter_goods_type0.place(relx=0.46, rely=0.65)
add_goods_btn0 = tk.Button(tab8, text='添加商品', font=('潮字社国风冉宋简-闪', 16),
                           command=lambda: connectlib.create_new_goods(enter_goods_name0.get(),
                                                                       enter_goods_price0.get(),
                                                                       enter_goods_cost0.get(),
                                                                       enter_goods_type0.get()))
add_goods_btn0.place(relx=0.45, rely=0.8)

# 4，进货
tk.Label(tab9, text='请输入商品id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
goods_id2 = tk.StringVar()
enter_goods_id2 = tk.Entry(tab9, textvariable=goods_id2, font=('潮字社国风冉宋简-闪', 16))
enter_goods_id2.place(relx=0.46, rely=0.2)
# tk.Label(tab9, text='请输入id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
# buyer_id2 = tk.StringVar()
# enter_buyer_id2 = tk.Entry(tab9, textvariable=buyer_id2, font=('潮字社国风冉宋简-闪', 16))
# enter_buyer_id2.place(relx=0.46, rely=0.35)
tk.Label(tab9, text='请输入进货数量:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
add_goods_quantity = tk.StringVar()
enter_add_goods_quantity = tk.Entry(tab9, textvariable=add_goods_quantity, font=('潮字社国风冉宋简-闪', 16))
enter_add_goods_quantity.place(relx=0.46, rely=0.4)
add_goods_quantity_btn = tk.Button(tab9, text='添加商品', font=('潮字社国风冉宋简-闪', 16),
                                   command=lambda: connectlib.stock(enter_goods_id2.get(), uid,
                                                                    enter_add_goods_quantity.get()))
add_goods_quantity_btn.place(relx=0.45, rely=0.6)


def showAllGoods():
    x = tv.get_children()
    for item in x:
        tv.delete(item)
    con = pymysql.connect(user='root', password='hanxu1125', database='b1', charset='utf8')
    cur = con.cursor()
    cur.execute("select * from goods")
    lst = cur.fetchall()
    for item in lst:
        tv.insert("", 1, text="line1", values=item)
    cur.close()
    con.close()


# 5，查看商品库存
# tk.Label(tab22, text='商品id:', font=('Arial', 13)).place(x=50, y=40)
# goods_id4 = tk.StringVar()
# enter_goods_id4 = tk.Entry(tab22, textvariable=goods_id4, font=('Arial', 14))
# enter_goods_id4.place(x=200, y=40)


tv = ttk.Treeview(tab22, show='headings', column=('goods_id', 'goods_name', 'cost', 'quantity'))
tv.column('goods_id', width=150, anchor="center")
tv.column('goods_name', width=150, anchor="center")
tv.column('cost', width=150, anchor="center")
tv.column('quantity', width=150, anchor="center")

tv.heading('goods_id', text='商品号')
tv.heading('goods_name', text='商品名称')
tv.heading('cost', text='成本')
tv.heading('quantity', text='库存')
tv.place(rely=0.2, relwidth=1, relheight=0.6)
btn = tk.Button(tab22, text="显示库存", font=('潮字社国风冉宋简-闪', 16), command=showAllGoods)
btn.place(relx=0.45, rely=0.1)

tab10 = Frame(tab_main)  # 管理员界面
tab10.place(x=30, y=30)
tab_main.add(tab10, text='注册')
tab11 = Frame(tab_main)  # 管理员界面
tab11.place(x=30, y=30)
tab_main.add(tab11, text='注销')
tab12 = Frame(tab_main)  # 管理员界面
tab12.place(x=30, y=30)
tab_main.add(tab12, text='顾客信息')
tab13 = Frame(tab_main)  # 管理员界面
tab13.place(x=30, y=30)
tab_main.add(tab13, text='进货记录')
tab14 = Frame(tab_main)  # 管理员界面
tab14.place(x=30, y=30)
tab_main.add(tab14, text='销售情况')
tab15 = Frame(tab_main)  # 管理员界面
tab15.place(x=30, y=30)
tab_main.add(tab15, text='VIP交易情况')
tab16 = Frame(tab_main)  # 管理员界面
tab16.place(x=30, y=30)
tab_main.add(tab16, text='商品信息')
tab17 = Frame(tab_main)  # 管理员界面
tab17.place(x=30, y=30)
tab_main.add(tab17, text='修改商品')
tab18 = Frame(tab_main)  # 管理员界面
tab18.place(x=30, y=30)
tab_main.add(tab18, text='利润排名')
tab19 = Frame(tab_main)  # 管理员界面
tab19.place(x=30, y=30)
tab_main.add(tab19, text='消费排名')
tab20 = Frame(tab_main)  # 管理员界面
tab20.place(x=30, y=30)
tab_main.add(tab20, text='vip记录')
tab21 = Frame(tab_main)  # 管理员界面
tab21.place(x=30, y=30)
tab_main.add(tab21, text='个人信息')

##########
# 管 理 员 界 面 #
##########

# 1，新建用户
tk.Label(tab10, text='请输入密码:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
user_pwd = tk.StringVar()
enter_user_pwd = tk.Entry(tab10, textvariable=user_pwd, font=('潮字社国风冉宋简-闪', 16), show='*')
enter_user_pwd.place(relx=0.46, rely=0.2)
tk.Label(tab10, text='请输入用户类型:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.4)
new_user_type = tk.StringVar()
enter_new_user_type = tk.Entry(tab10, textvariable=new_user_type, font=('潮字社国风冉宋简-闪', 16))
enter_new_user_type.place(relx=0.46, rely=0.4)
new_user_btn = tk.Button(tab10, text='新建用户', font=('潮字社国风冉宋简-闪', 16),
                         command=lambda: connectlib.register(enter_user_pwd.get(), enter_new_user_type.get()))
new_user_btn.place(relx=0.45, rely=0.6)

# 2，注销用户
tk.Label(tab11, text='注销id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
logout_id = tk.StringVar()
enter_logout_id = tk.Entry(tab11, textvariable=logout_id, font=('潮字社国风冉宋简-闪', 16))
enter_logout_id.place(relx=0.44, rely=0.35)
logout_user_btn = tk.Button(tab11, text='注销用户', font=('潮字社国风冉宋简-闪', 16),
                            command=lambda: connectlib.logout(enter_logout_id.get()))
logout_user_btn.place(relx=0.45, rely=0.55)


# 3，查看用户信息
def showAllCustomer():
    x1 = tv1.get_children()
    for item in x1:
        tv1.delete(item)
    con1 = pymysql.connect(host, host_name, host_password, database)
    cur1 = con1.cursor()
    cur1.execute("select * from customer")
    lst1 = cur1.fetchall()
    for item1 in lst1:
        tv1.insert("", 1, text="line1", values=item1)
    cur1.close()
    con1.close()


tv1 = ttk.Treeview(tab12, show='headings', column=('customer_id', 'customer_name', 'phone', 'point', 'vip'))
tv1.column('customer_id', width=150, anchor="center")
tv1.column('customer_name', width=150, anchor="center")
tv1.column('phone', width=150, anchor="center")
tv1.column('point', width=150, anchor="center")
tv1.column('vip', width=150, anchor="center")

tv1.heading('customer_id', text='客户id')
tv1.heading('customer_name', text='客户姓名')
tv1.heading('phone', text='手机')
tv1.heading('point', text='积分')
tv1.heading('vip', text='VIP')
tv1.place(rely=0.15, relwidth=1, relheight=0.8)
get_customer_btn = tk.Button(tab12, text='查看所有顾客信息', font=('潮字社国风冉宋简-闪', 16), command=showAllCustomer)
get_customer_btn.place(relx=0.4, rely=0.05, width=200)


# 4，查看进货信息
def showAllStock():
    x2 = tv2.get_children()
    for item2 in x2:
        tv2.delete(item2)
    con2 = pymysql.connect(host, host_name, host_password, database)
    cur2 = con2.cursor()
    cur2.execute("select * from stock")
    lst2 = cur2.fetchall()
    for item3 in lst2:
        tv2.insert("", 1, text="line1", values=item3)
    cur2.close()
    con2.close()


tv2 = ttk.Treeview(tab13, show='headings', column=('order', 'goods_id', 'id', 'quantity', 'time'))
tv2.column('order', width=150, anchor="center")
tv2.column('goods_id', width=150, anchor="center")
tv2.column('id', width=150, anchor="center")
tv2.column('quantity', width=150, anchor="center")
tv2.column('time', width=150, anchor="center")

tv2.heading('order', text='顺序')
tv2.heading('goods_id', text='商品id')
tv2.heading('id', text='进货员')
tv2.heading('quantity', text='数量')
tv2.heading('time', text='时间')
tv2.place(rely=0.15, relwidth=1, relheight=0.8)
get_stock_btn = tk.Button(tab13, text='查看进货信息', font=('潮字社国风冉宋简-闪', 16), command=showAllStock)
get_stock_btn.place(relx=0.4, rely=0.05, width=200)


# 5，查询销售情况
def showAllSale(odr, goods_type=-1, start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    x3 = tv3.get_children()
    for item3 in x3:
        tv3.delete(item3)
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
    for row in res:
        print(
            "goods_id={}\tgoods_name={}\tsum_quantity={}\tsum_payment={}\tsum_profit={}".format(row[0], row[1], row[2],
                                                                                                row[3], row[4]))
        li = [row[0], row[1], row[2], row[3], row[4]]
        tv3.insert("", 'end', text="line1", values=li)

    db.close()


tk.Label(tab14, text='排序方式:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.01)
# odr = tk.StringVar()
# enter_odr = tk.Entry(tab14, textvariable=odr, font=('潮字社国风冉宋简-闪', 16))
# enter_odr.place(relx=0.44, rely=0.05)

enter_odr = -1


def up():
    global enter_odr
    enter_odr = 1


def down():
    global enter_odr
    enter_odr = 0


# 第5步，创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(tab14, text='总利润降序', font=('潮字社国风冉宋简-闪', 10), variable=enter_odr, value=1, command=up)
r1.pack()
r2 = tk.Radiobutton(tab14, text='销售额降序', font=('潮字社国风冉宋简-闪', 10), variable=enter_odr, value=0, command=down)
r2.pack()
# r1.grid(relx=0.5,rela=0.05)
# r2.grid(row=2, column=1)

tk.Label(tab14, text='商品类型:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.1)

cmb = ttk.Combobox(tab14, width=10, font=('潮字社国风冉宋简-闪', 12))
# cmb.grid(row=3,column=1)
cmb.pack()
# 设置下拉菜单中的值
cmb['value'] = ("全部商品", "生活类", "办公类", "书籍类", "电器类", "饮食类", "其他")
t = -2


# 执行函数
def func(event):
    global t
    l = cmb.get()
    if (l == "全部商品"):
        t = -1
    elif (l == "生活类"):
        t = 1
    elif (l == "办公类"):
        t = 2
    elif (l == "书籍类"):
        t = 3
    elif (l == "电器类"):
        t = 4
    elif (l == "饮食类"):
        t = 5
    else:
        t = 0
    # print(t)


cmb.bind("<<ComboboxSelected>>", func)

# goods_type = tk.StringVar()
# enter_goods_type = tk.Entry(tab14, textvariable=goods_type, font=('潮字社国风冉宋简-闪', 16))
# enter_goods_type.place(relx=0.44, rely=0.15)
tk.Label(tab14, text='起始时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
start_time = tk.StringVar()
enter_start_time = tk.Entry(tab14, textvariable=start_time, font=('潮字社国风冉宋简-闪', 16))
enter_start_time.place(relx=0.42, rely=0.2)
tk.Label(tab14, text='截止时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.3)
end_time = tk.StringVar()
enter_end_time = tk.Entry(tab14, textvariable=end_time, font=('潮字社国风冉宋简-闪', 16))
enter_end_time.place(relx=0.42, rely=0.3)
tv3 = ttk.Treeview(tab14, show='headings',
                   column=('goods_id', 'goods_name', 'sum_quantity', 'sum_payment', 'sum_profit'))
tv3.column('goods_id', width=150, anchor="center")
tv3.column('goods_name', width=150, anchor="center")
tv3.column('sum_quantity', width=150, anchor="center")
tv3.column('sum_payment', width=150, anchor="center")
tv3.column('sum_profit', width=150, anchor="center")

# tv3.heading('goods_id', text='商品号')
# tv3.heading('goods_name', text='商品名称')
# tv3.heading('sum_quantity', text='总数')
# tv3.heading('sum_payment', text='总售价')
# tv3.heading('sum_profit', text='利润')
# tv3.place(rely=0.48, relwidth=1, relheight=0.8)

def treeview_sort_column(tv3, col, reverse):  # Treeview、列名、排列方式
    l = [(tv3.set(k, col), k) for k in tv3.get_children('')]
    print(tv3.get_children(''))
    l.sort(reverse=reverse)  # 排序方式
    # rearrange items in sorted positions
    for index, (val, k) in enumerate(l):  # 根据排序后索引移动
        tv3.move(k, '', index)
        print(k)
    tv3.heading(col, command=lambda: treeview_sort_column(tv3, col, not reverse))  # 重写标题，使之成为再点倒序的标题
columns = ["goods_id","sum_quantity","sum_payment","sum_profit"]
for col in columns:  # 给所有标题加（循环上边的“手工”）
    tv3.heading(col, text=col, command=lambda _col=col: treeview_sort_column(tv3, _col, False))
tv3.heading('goods_id', text='商品号')
tv3.heading('goods_name', text='商品名称')
tv3.heading('sum_quantity', text='总数')
tv3.heading('sum_payment', text='销售额')
tv3.heading('sum_profit', text='总利润')
tv3.place(rely=0.48, relwidth=1, relheight=0.8)
get_sale_btn = tk.Button(tab14, text='查询销售情况', font=('潮字社国风冉宋简-闪', 16),
                         command=lambda: showAllSale(enter_odr, t, enter_start_time.get(),
                                                     enter_end_time.get()))
get_sale_btn.place(relx=0.45, rely=0.38)


# 6，查询VIP交易
def show_vip_purchase(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    x = tv4.get_children()
    for item5 in x:
        tv4.delete(item5)
    start_time = '\'' + start_time + '\''  # added!!
    end_time = '\'' + end_time + '\''
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    # 两张表的quantity重名了。。。
    sql = "select customer_id,customer_name,phone,goods_id,quantity,time,payment,vip from purchase join customer " \
          f"using(customer_id) where time > {start_time} and time < {end_time} order by vip,customer_id desc "
    cursor.execute(sql)
    res = cursor.fetchall()
    for item6 in res:
        tv4.insert("", 1, text="line1", values=item6)
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
    # return feedback


tk.Label(tab15, text='起始时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
vip_start_time = tk.StringVar()
enter_vip_start_time = tk.Entry(tab15, textvariable=vip_start_time, font=('潮字社国风冉宋简-闪', 16))
enter_vip_start_time.place(relx=0.44, rely=0.05)
tk.Label(tab15, text='截止时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.15)
vip_end_time = tk.StringVar()
enter_vip_end_time = tk.Entry(tab15, textvariable=vip_end_time, font=('潮字社国风冉宋简-闪', 16))
enter_vip_end_time.place(relx=0.44, rely=0.15)
tv4 = ttk.Treeview(tab15, show='headings',
                   column=('customer_id', 'customer_name', 'phone', 'goods_id', 'quantity', 'time', 'payment', 'vip'))
tv4.column('customer_id', width=150, anchor="center")
tv4.column('customer_name', width=150, anchor="center")
tv4.column('phone', width=150, anchor="center")
tv4.column('goods_id', width=150, anchor="center")
tv4.column('quantity', width=150, anchor="center")
tv4.column('time', width=150, anchor="center")
tv4.column('payment', width=150, anchor="center")
tv4.column('vip', width=150, anchor="center")

tv4.heading('customer_id', text='顾客id')
tv4.heading('customer_name', text='顾客姓名')
tv4.heading('phone', text='电话')
tv4.heading('goods_id', text='商品号')
tv4.heading('quantity', text='数量')
tv4.heading('time', text='交易时间')
tv4.heading('payment', text='售价')
tv4.heading('vip', text='VIP点')
tv4.place(rely=0.35, relwidth=1, relheight=0.8)
get_vip_purchase_btn = tk.Button(tab15, text='查询VIP交易情况', font=('潮字社国风冉宋简-闪', 16),
                                 command=lambda: show_vip_purchase(enter_vip_start_time.get(),
                                                                   enter_vip_end_time.get()))
get_vip_purchase_btn.place(relx=0.45, rely=0.23)


# 7，查询商品信息
def show_single_goods_info(goods_id):
    x = tv5.get_children()
    for item in x:
        tv5.delete(item)
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = f"select goods_name,price,cost,quantity from goods where goods_id={goods_id}"
    cursor.execute(sql)
    res = cursor.fetchall()
    for item1 in res:
        tv5.insert("", 1, text="line1", values=item1)
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


tk.Label(tab16, text='商品id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
goods_id3 = tk.StringVar()
enter_goods_id3 = tk.Entry(tab16, textvariable=goods_id3, font=('潮字社国风冉宋简-闪', 16))
enter_goods_id3.place(relx=0.44, rely=0.05)
tv5 = ttk.Treeview(tab16, show='headings', column=('goods_name', 'price', 'cost', 'quantity'))
tv5.column('goods_name', width=150, anchor="center")
tv5.column('price', width=150, anchor="center")
tv5.column('cost', width=150, anchor="center")
tv5.column('quantity', width=150, anchor="center")

tv5.heading('goods_name', text='商品名称')
tv5.heading('price', text='售价')
tv5.heading('cost', text='成本')
tv5.heading('quantity', text='数量')
tv5.place(rely=0.25, relwidth=1, relheight=0.8)
get_single_goods_info_btn = tk.Button(tab16, text='商品信息', font=('潮字社国风冉宋简-闪', 16),
                                      command=lambda: show_single_goods_info(enter_goods_id3.get()))
get_single_goods_info_btn.place(relx=0.45, rely=0.13)

# 8，修改商品信息
tk.Label(tab17, text='商品id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
goods_id4 = tk.StringVar()
enter_goods_id4 = tk.Entry(tab17, textvariable=goods_id4, font=('潮字社国风冉宋简-闪', 16))
enter_goods_id4.place(relx=0.46, rely=0.05)
tk.Label(tab17, text='商品新名称:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.15)
new_goods_name = tk.StringVar()
enter_new_goods_name = tk.Entry(tab17, textvariable=new_goods_name, font=('潮字社国风冉宋简-闪', 16))
enter_new_goods_name.place(relx=0.46, rely=0.15)
tk.Label(tab17, text='商品新售价:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.25)
new_price = tk.StringVar()
enter_new_price = tk.Entry(tab17, textvariable=new_price, font=('潮字社国风冉宋简-闪', 16))
enter_new_price.place(relx=0.46, rely=0.25)
tk.Label(tab17, text='商品新成本:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
new_cost = tk.StringVar()
enter_new_cost = tk.Entry(tab17, textvariable=new_cost, font=('潮字社国风冉宋简-闪', 16))
enter_new_cost.place(relx=0.46, rely=0.35)
tk.Label(tab17, text='商品新数量:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.45)
new_quantity = tk.StringVar()
enter_new_quantity = tk.Entry(tab17, textvariable=new_quantity, font=('潮字社国风冉宋简-闪', 16))
enter_new_quantity.place(relx=0.46, rely=0.45)
modify_single_goods_info_btn = tk.Button(tab17, text='修改商品信息', font=('潮字社国风冉宋简-闪', 16),
                                         command=lambda: connectlib.modify_single_goods_info(enter_goods_id4.get(),
                                                                                             enter_new_goods_name.get(),
                                                                                             enter_new_price.get(),
                                                                                             enter_new_cost.get(),
                                                                                             enter_new_quantity.get()))
modify_single_goods_info_btn.place(relx=0.45, rely=0.55)


#   9.查询各种商品类型的在一定时间内的总利润排名
def show_every_type_sum_profit(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    x = tv6.get_children()
    for item in x:
        tv6.delete(item)
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
        li1 = [rank, row[0], row[1]]
        tv6.insert("", 1, text="line1", values=li1)
    feedback = f'{rank} {feedback}'
    db.close()


tk.Label(tab18, text='开始时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
start_time1 = tk.StringVar()
enter_start_time1 = tk.Entry(tab18, textvariable=start_time1, font=('潮字社国风冉宋简-闪', 16))
enter_start_time1.place(relx=0.44, rely=0.05)
tk.Label(tab18, text='结束时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.15)
end_time1 = tk.StringVar()
enter_end_time1 = tk.Entry(tab18, textvariable=end_time1, font=('潮字社国风冉宋简-闪', 16))
enter_end_time1.place(relx=0.44, rely=0.15)
tv6 = ttk.Treeview(tab18, show='headings', column=('rank', 'goods_type', 'sum_profit'))
tv6.column('rank', width=150, anchor="center")
tv6.column('goods_type', width=150, anchor="center")
tv6.column('sum_profit', width=150, anchor="center")

tv6.heading('rank', text='排名')
tv6.heading('goods_type', text='商品类型')
tv6.heading('sum_profit', text='利润')
tv6.place(rely=0.35, relwidth=1, relheight=0.8)
get_profit_rank_btn = tk.Button(tab18, text='利润排名', font=('潮字社国风冉宋简-闪', 16),
                                command=lambda: show_every_type_sum_profit(enter_start_time1.get(),
                                                                           enter_end_time1.get()))
get_profit_rank_btn.place(relx=0.45, rely=0.23)


#   10.查询所有顾客的在一定时间内的总消费排名
def show_every_customer_sum_payment(start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    x = tv7.get_children()
    for item in x:
        tv7.delete(item)
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
        li = [rank, row[0], row[1], row[2]]
        tv7.insert("", 1, text="line1", values=li)
    db.close()


tk.Label(tab19, text='开始时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
start_time2 = tk.StringVar()
enter_start_time2 = tk.Entry(tab19, textvariable=start_time2, font=('潮字社国风冉宋简-闪', 16))
enter_start_time2.place(relx=0.44, rely=0.05)
tk.Label(tab19, text='结束时间:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.15)
end_time2 = tk.StringVar()
enter_end_time2 = tk.Entry(tab19, textvariable=end_time2, font=('潮字社国风冉宋简-闪', 16))
enter_end_time2.place(relx=0.44, rely=0.15)
tv7 = ttk.Treeview(tab19, show='headings', column=('rank', 'customer_name', 'customer_id', 'sum_payment'))
tv7.column('rank', width=150, anchor="center")
tv7.column('customer_name', width=150, anchor="center")
tv7.column('customer_id', width=150, anchor="center")
tv7.column('sum_payment', width=150, anchor="center")

tv7.heading('rank', text='排名')
tv7.heading('customer_name', text='顾客姓名')
tv7.heading('customer_id', text='顾客id')
tv7.heading('sum_payment', text='总售价')
tv7.place(rely=0.35, relwidth=1, relheight=0.8)
get_buy_rank_btn = tk.Button(tab19, text='消费排名', font=('潮字社国风冉宋简-闪', 16),
                             command=lambda: show_every_customer_sum_payment(enter_start_time2.get(),
                                                                             enter_end_time2.get()))
get_buy_rank_btn.place(relx=0.45, rely=0.23)


#   11.查询一个特定的顾客的vip点获得记录
def show_single_customer_point(customer_id):
    x = tv8.get_children()
    for item in x:
        tv8.delete(item)
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
        li = [row[0], row[1], row[2]]
        tv8.insert("", 1, text="line1", values=li)
        count = count + 1
    db.close()


tk.Label(tab20, text='顾客id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
vip_id = tk.StringVar()
enter_vip_id = tk.Entry(tab20, textvariable=vip_id, font=('潮字社国风冉宋简-闪', 16))
enter_vip_id.place(relx=0.44, rely=0.05)
tv8 = ttk.Treeview(tab20, show='headings', column=('time', 'get_point', 'way_name'))
tv8.column('time', width=150, anchor="center")
tv8.column('get_point', width=150, anchor="center")
tv8.column('way_name', width=150, anchor="center")

tv8.heading('time', text='获得时间')
tv8.heading('get_point', text='获得点数')
tv8.heading('way_name', text='获得方式')

tv8.place(rely=0.25, relwidth=1, relheight=0.8)
vip_point_btn = tk.Button(tab20, text='查询vip点', font=('潮字社国风冉宋简-闪', 16),
                          command=lambda: show_single_customer_point(enter_vip_id.get()))
vip_point_btn.place(relx=0.45, rely=0.13)


#   12.查询某一未注销员工的个人信息
def show_single_staff_info(id):
    x = tv9.get_children()
    for item in x:
        tv9.delete(item)
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
        li = [row[0], row[1], row[2]]
        tv9.insert("", 1, text="line1", values=li)
        count = count + 1
    db.close()


tk.Label(tab21, text='用户id:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.05)
customer_id3 = tk.StringVar()
enter_customer_id3 = tk.Entry(tab21, textvariable=customer_id3, font=('潮字社国风冉宋简-闪', 16))
enter_customer_id3.place(relx=0.44, rely=0.05)
tv9 = ttk.Treeview(tab21, show='headings', column=('name', 'phone', 'type'))
tv9.column('name', width=150, anchor="center")
tv9.column('phone', width=150, anchor="center")
tv9.column('type', width=150, anchor="center")

tv9.heading('name', text='姓名')
tv9.heading('phone', text='手机')
tv9.heading('type', text='类型')
tv9.place(rely=0.25, relwidth=1, relheight=0.8)
get_info_btn = tk.Button(tab21, text='个人信息', font=('潮字社国风冉宋简-闪', 16),
                         command=lambda: show_single_staff_info(enter_customer_id3.get()))
get_info_btn.place(relx=0.45, rely=0.13)

print(type_user)
if type_user == 1:
    tab1.destroy()
    tab2.destroy()
    tab3.destroy()
    tab4.destroy()
    tab5.destroy()
    tab6.destroy()
    tab7.destroy()
    tab8.destroy()
    tab9.destroy()
    tab22.destroy()
elif type_user == 2:
    tab6.destroy()
    tab7.destroy()
    tab8.destroy()
    tab9.destroy()
    tab22.destroy()
    tab10.destroy()
    tab11.destroy()
    tab12.destroy()
    tab13.destroy()
    tab14.destroy()
    tab15.destroy()
    tab16.destroy()
    tab17.destroy()
    tab18.destroy()
    tab19.destroy()
    tab20.destroy()
    tab21.destroy()
elif type_user == 3:
    tab1.destroy()
    tab2.destroy()
    tab3.destroy()
    tab4.destroy()
    tab5.destroy()
    tab10.destroy()
    tab11.destroy()
    tab12.destroy()
    tab13.destroy()
    tab14.destroy()
    tab15.destroy()
    tab16.destroy()
    tab17.destroy()
    tab18.destroy()
    tab19.destroy()
    tab20.destroy()
    tab21.destroy()

root.mainloop()
