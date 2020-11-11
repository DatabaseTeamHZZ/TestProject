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
host_password = "***"
database = "b1"

type_user = -1  # 用户类型

# 登陆界面
class MY_GUI():
    def __init__(self):  # 类似于构造器，将TK窗口作为成员对象初始化进来
        pass

    def click_login(self):
        name = self.entry_usr_name.get()
        password = self.entry_usr_pwd.get()
        self.user_type = connectlib.login_to_server(name, password)

    def login_window(self):
        self.window = tk.Tk()
        self.window.title('Wellcome to Shopping Manage System')
        self.window.geometry('400x200')
        # 用户信息
        tk.Label(self.window, text='User name:', font=('Arial', 14)).place(x=10, y=50)
        tk.Label(self.window, text='Password:', font=('Arial', 14)).place(x=10, y=100)
        # 用户名
        self.var_usr_name = tk.StringVar()
        self.entry_usr_name = tk.Entry(self.window, textvariable=self.var_usr_name, font=('Arial', 14))
        self.entry_usr_name.place(x=120, y=50)
        # 用户密码
        self.var_usr_pwd = tk.StringVar()
        self.entry_usr_pwd = tk.Entry(self.window, textvariable=self.var_usr_pwd, font=('Arial', 14), show='*')
        self.entry_usr_pwd.place(x=120, y=100)
        self.user_id = -1
        # login 按钮
        self.btn_login = tk.Button(self.window, text='Login', command=self.click_login)
        self.btn_login.place(x=170, y=150)
        # 主窗口循环显示
        self.window.mainloop()

def login_start():
    run = MY_GUI()  # 传入TK窗口
    run.login_window()  # 设置根窗口默认属性
    global type_user
    type_user = run.user_type

if __name__ == '__main__':  # 如果是命令行直接运行则开始运行，否则不执行
    login_start()
################################################

# 主界面
root = Tk()
root.title('欢迎来到商品管理系统')#主界面名称
root.geometry('600x900+100+100')

tab_main = ttk.Notebook()  # 创建分页栏
tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)

tab1 = Frame(tab_main)  # 创建收银员界面
tab1.place(x=30, y=30)
tab_main.add(tab1, text='收银员界面')  # 将第一页插入分页栏中

##########
# 收 银 员 界 面 #
##########

# 1，更改密码：
tk.Label(tab1, text='请输入 id:', font=('Arial', 13)).place(x=50, y=10)
cashier_id = tk.StringVar()
cashier_name = tk.Entry(tab1, textvariable=cashier_id, font=('Arial', 14))
cashier_name.place(x=200, y=10)
tk.Label(tab1, text='请输入旧密码:', font=('Arial', 13)).place(x=50, y=40)
cashier_old_pwd = tk.StringVar()
enter_old_pwd = tk.Entry(tab1, textvariable=cashier_old_pwd, font=('Arial', 14), show='*')
enter_old_pwd.place(x=200, y=40)
tk.Label(tab1, text='请输入新密码:', font=('Arial', 13)).place(x=50, y=70)
cashier_new_pwd = tk.StringVar()
enter_new_pwd = tk.Entry(tab1, textvariable=cashier_new_pwd, font=('Arial', 14), show='*')
enter_new_pwd.place(x=200, y=70)
change_pwd_btn = tk.Button(tab1, text='修改密码',
                           command=lambda: connectlib.modify_account_password(cashier_name.get(), enter_old_pwd.get(),
                                                                              enter_new_pwd.get()))
change_pwd_btn.place(x=270, y=100)

# 2，修改个人信息
tk.Label(tab1, text='请输入id:', font=('Arial', 13)).place(x=50, y=140)
cashier_cname = tk.StringVar()
enter_name = tk.Entry(tab1, textvariable=cashier_cname, font=('Arial', 14))
enter_name.place(x=200, y=140)
tk.Label(tab1, text='请输入新用户名:', font=('Arial', 13)).place(x=50, y=170)
cashier_new_name = tk.StringVar()
enter_new_name = tk.Entry(tab1, textvariable=cashier_new_name, font=('Arial', 14))
enter_new_name.place(x=200, y=170)
tk.Label(tab1, text='请输入新手机号码:', font=('Arial', 13)).place(x=50, y=210)
cashier_new_phone = tk.StringVar()
enter_new_phone = tk.Entry(tab1, textvariable=cashier_new_phone, font=('Arial', 14))
enter_new_phone.place(x=200, y=210)
change_info_btn = tk.Button(tab1, text='修改个人信息',
                            command=lambda: connectlib.modify_cashier_info(enter_name.get(), enter_new_name.get(),
                                                                           enter_new_phone.get()))
change_info_btn.place(x=255, y=240)

#3，交易：
tk.Label(tab1, text='请输入顾客id:', font=('Arial', 13)).place(x=50, y=280)
customer_id = tk.StringVar()
enter_customer_id = tk.Entry(tab1, textvariable=customer_id, font=('Arial', 14))
enter_customer_id.place(x=200, y=280)
tk.Label(tab1, text='请输入商品号:', font=('Arial', 13)).place(x=50, y=320)
goods_id = tk.StringVar()
enter_goods_id = tk.Entry(tab1, textvariable=goods_id, font=('Arial', 14))
enter_goods_id.place(x=200, y=320)
tk.Label(tab1, text='请输入交易数量:', font=('Arial', 13)).place(x=50, y=360)
quantity = tk.StringVar()
enter_quantity = tk.Entry(tab1, textvariable=quantity, font=('Arial', 14))
enter_quantity.place(x=200, y=360)
purchase_btn = tk.Button(tab1, text='交易',
                         command=lambda: connectlib.purchase(enter_customer_id.get(), enter_goods_id.get(),
                                                             enter_quantity.get()))
purchase_btn.place(x=280, y=390)

#4，购买点数
tk.Label(tab1, text='请输入顾客id:', font=('Arial', 13)).place(x=50, y=430)
customer_id2 = tk.StringVar()
enter_customer_id2 = tk.Entry(tab1, textvariable=customer_id2, font=('Arial', 14))
enter_customer_id2.place(x=200, y=430)
tk.Label(tab1, text='请输入购买点数:', font=('Arial', 13)).place(x=50, y=470)
point = tk.StringVar()
enter_point = tk.Entry(tab1, textvariable=point, font=('Arial', 14))
enter_point.place(x=200, y=470)
get_point = tk.Button(tab1, text='购买点数',
                      command=lambda: connectlib.buy_point(enter_customer_id2.get(), enter_point.get()))
get_point.place(x=270, y=500)

#5，添加顾客
tk.Label(tab1, text='请输入顾客名称:', font=('Arial', 13)).place(x=50, y=540)
customer_name = tk.StringVar()
enter_customer_name = tk.Entry(tab1, textvariable=customer_name, font=('Arial', 14))
enter_customer_name.place(x=200, y=540)
tk.Label(tab1, text='请输入顾客电话:', font=('Arial', 13)).place(x=50, y=580)
customer_phone = tk.StringVar()
enter_customer_phone = tk.Entry(tab1, textvariable=customer_phone, font=('Arial', 14))
enter_customer_phone.place(x=200, y=580)
register_customer = tk.Button(tab1, text='注册顾客',
                              command=lambda: connectlib.sign_up_new_customer(enter_customer_name.get(),
                                                                              enter_customer_phone.get()))
register_customer.place(x=270, y=610)

tab2 = Frame(tab_main)#收银员界面
tab2.place(x=50, y=130)
tab_main.add(tab2, text='进货员界面')

##########
# 进 货 员 界 面 #
##########

#1，修改密码
tk.Label(tab2, text='请输入 id:', font=('Arial', 13)).place(x=50, y=10)
buyer_id = tk.StringVar()
enter_buyer_id = tk.Entry(tab2, textvariable=buyer_id, font=('Arial', 14))
enter_buyer_id.place(x=200, y=10)
tk.Label(tab2, text='请输入旧密码:', font=('Arial', 13)).place(x=50, y=40)
buyer_old_pwd = tk.StringVar()
enter_buyer_old_pwd = tk.Entry(tab2, textvariable=buyer_old_pwd, font=('Arial', 14), show='*')
enter_buyer_old_pwd.place(x=200, y=40)
tk.Label(tab2, text='请输入新密码:', font=('Arial', 13)).place(x=50, y=70)
buyer_new_pwd = tk.StringVar()
enter_buyer_new_pwd = tk.Entry(tab2, textvariable=buyer_new_pwd, font=('Arial', 14), show='*')
enter_buyer_new_pwd.place(x=200, y=70)
change_buyer_pwd_btn = tk.Button(tab2, text='修改密码',
                                 command=lambda: connectlib.modify_account_password(enter_buyer_id.get(),
                                                                                    enter_buyer_old_pwd.get(),
                                                                                    enter_buyer_new_pwd.get()))
change_buyer_pwd_btn.place(x=270, y=100)

#2，修改个人信息
tk.Label(tab2, text='请输入id:', font=('Arial', 13)).place(x=50, y=140)
buyer_cname = tk.StringVar()
enter_buyer_name = tk.Entry(tab2, textvariable=buyer_cname, font=('Arial', 14))
enter_buyer_name.place(x=200, y=140)
tk.Label(tab2, text='请输入新用户名:', font=('Arial', 13)).place(x=50, y=170)
buyer_new_name = tk.StringVar()
enter_buyer_new_name = tk.Entry(tab2, textvariable=buyer_new_name, font=('Arial', 14))
enter_buyer_new_name.place(x=200, y=170)
tk.Label(tab2, text='请输入新手机号码:', font=('Arial', 13)).place(x=50, y=200)
buyer_new_phone = tk.StringVar()
enter_buyer_new_phone = tk.Entry(tab2, textvariable=buyer_new_phone, font=('Arial', 14))
enter_buyer_new_phone.place(x=200, y=200)
change_buyer_info_btn = tk.Button(tab2, text='修改个人信息',
                                  command=lambda: connectlib.modify_buyer_info(enter_buyer_name.get(),
                                                                               enter_buyer_new_name.get(),
                                                                               enter_buyer_new_phone.get()))
change_buyer_info_btn.place(x=255, y=230)

#3，添加商品
tk.Label(tab2, text='请输入商品名称:', font=('Arial', 13)).place(x=50, y=270)
goods_name = tk.StringVar()
enter_goods_name = tk.Entry(tab2, textvariable=goods_name, font=('Arial', 14))
enter_goods_name.place(x=200, y=270)
tk.Label(tab2, text='请输入商品售价:', font=('Arial', 13)).place(x=50, y=300)
goods_price = tk.StringVar()
enter_goods_price = tk.Entry(tab2, textvariable=goods_price, font=('Arial', 14))
enter_goods_price.place(x=200, y=300)
tk.Label(tab2, text='请输入商品成本:', font=('Arial', 13)).place(x=50, y=330)
goods_cost = tk.StringVar()
enter_goods_cost = tk.Entry(tab2, textvariable=goods_cost, font=('Arial', 14))
enter_goods_cost.place(x=200, y=330)
tk.Label(tab2, text='请输入商品类型:', font=('Arial', 13)).place(x=50, y=360)
goods_type = tk.StringVar()
enter_goods_type = tk.Entry(tab2, textvariable=goods_type, font=('Arial', 14))
enter_goods_type.place(x=200, y=360)
add_goods_btn = tk.Button(tab2, text='添加商品',
                          command=lambda: connectlib.create_new_goods(enter_goods_name.get(), enter_goods_price.get(),
                                                                      enter_goods_cost.get(), enter_goods_type.get()))
add_goods_btn.place(x=280, y=390)

#4，进货
tk.Label(tab2, text='请输入商品id:', font=('Arial', 13)).place(x=50, y=430)
goods_id2 = tk.StringVar()
enter_goods_id2 = tk.Entry(tab2, textvariable=goods_id2, font=('Arial', 14))
enter_goods_id2.place(x=200, y=430)
tk.Label(tab2, text='请输入id:', font=('Arial', 13)).place(x=50, y=460)
buyer_id2 = tk.StringVar()
enter_buyer_id2 = tk.Entry(tab2, textvariable=buyer_id2, font=('Arial', 14))
enter_buyer_id2.place(x=200, y=460)
tk.Label(tab2, text='请输入进货数量:', font=('Arial', 13)).place(x=50, y=490)
add_goods_quantity = tk.StringVar()
enter_add_goods_quantity = tk.Entry(tab2, textvariable=add_goods_quantity, font=('Arial', 14))
enter_add_goods_quantity.place(x=200, y=490)
add_goods_quantity_btn = tk.Button(tab2, text='添加商品',
                                   command=lambda: connectlib.stock(enter_goods_id2.get(), enter_buyer_id2.get(),
                                                                    enter_add_goods_quantity.get()))
add_goods_quantity_btn.place(x=280, y=520)


tab3 = Frame(tab_main)#管理员界面
tab3.place(x=50, y=130)
tab_main.add(tab3, text='管理员界面')

##########
# 管 理 员 界 面 #
##########

#1，修改密码
tk.Label(tab3, text='请输入密码:', font=('Arial', 13)).place(x=50, y=10)
user_pwd = tk.StringVar()
enter_user_pwd = tk.Entry(tab3, textvariable=user_pwd, font=('Arial', 14), show='*')
enter_user_pwd.place(x=200, y=10)
tk.Label(tab3, text='请输入用户类型:', font=('Arial', 13)).place(x=50, y=40)
new_user_type = tk.StringVar()
enter_new_user_type = tk.Entry(tab3, textvariable=new_user_type, font=('Arial', 14))
enter_new_user_type.place(x=200, y=40)
new_user_btn = tk.Button(tab3, text='新建用户',
                         command=lambda: connectlib.register(enter_user_pwd.get(), enter_new_user_type.get()))
new_user_btn.place(x=270, y=70)

#2，修改个人信息
tk.Label(tab3, text='注销id:', font=('Arial', 13)).place(x=50, y=110)
logout_id = tk.StringVar()
enter_logout_id = tk.Entry(tab3, textvariable=logout_id, font=('Arial', 14))
enter_logout_id.place(x=200, y=110)
logout_user_btn = tk.Button(tab3, text='注销用户', command=lambda: connectlib.logout(enter_logout_id.get()))
logout_user_btn.place(x=270, y=140)

#3，查看用户信息
get_customer_btn = tk.Button(tab3, text='用户信息', command=connectlib.get_customers_info)
get_customer_btn.place(x=200, y=180)

#4，查看进货信息
get_stock_btn = tk.Button(tab3, text='进货信息', command=connectlib.get_stock)
get_stock_btn.place(x=350, y=180)

#5，查询销售情况
tk.Label(tab3, text='排序方式:', font=('Arial', 13)).place(x=50, y=220)
odr = tk.StringVar()
enter_odr = tk.Entry(tab3, textvariable=odr, font=('Arial', 14))
enter_odr.place(x=200, y=220)
tk.Label(tab3, text='起始时间:', font=('Arial', 13)).place(x=50, y=250)
start_time = tk.StringVar()
enter_start_time = tk.Entry(tab3, textvariable=start_time, font=('Arial', 14))
enter_start_time.place(x=200, y=250)
tk.Label(tab3, text='截止时间:', font=('Arial', 13)).place(x=50, y=280)
end_time = tk.StringVar()
enter_end_time = tk.Entry(tab3, textvariable=end_time, font=('Arial', 14))
enter_end_time.place(x=200, y=280)
get_sale_btn = tk.Button(tab3, text='查询销售情况',
                         command=lambda: connectlib.get_sale_in_period(enter_odr.get(), enter_start_time.get(),
                                                                       enter_end_time.get()))
get_sale_btn.place(x=270, y=310)

#6，查询VIP交易
tk.Label(tab3, text='起始时间:', font=('Arial', 13)).place(x=50, y=350)
vip_start_time = tk.StringVar()
enter_vip_start_time = tk.Entry(tab3, textvariable=vip_start_time, font=('Arial', 14))
enter_vip_start_time.place(x=200, y=350)
tk.Label(tab3, text='截止时间:', font=('Arial', 13)).place(x=50, y=380)
vip_end_time = tk.StringVar()
enter_vip_end_time = tk.Entry(tab3, textvariable=vip_end_time, font=('Arial', 14))
enter_vip_end_time.place(x=200, y=380)
get_vip_purchase_btn = tk.Button(tab3, text='查询VIP交易情况',
                                 command=lambda: connectlib.get_vip_sale_in_period(enter_vip_start_time.get(),
                                                                                   enter_vip_end_time.get()))
get_vip_purchase_btn.place(x=270, y=410)

#7，查询商品信息
tk.Label(tab3, text='商品id:', font=('Arial', 13)).place(x=50, y=450)
goods_id3 = tk.StringVar()
enter_goods_id3 = tk.Entry(tab3, textvariable=goods_id3, font=('Arial', 14))
enter_goods_id3.place(x=200, y=450)
get_single_goods_info_btn = tk.Button(tab3, text='商品信息',
                                      command=lambda: connectlib.get_single_goods_info(enter_goods_id3.get()))
get_single_goods_info_btn.place(x=270, y=480)

#8，修改商品信息
tk.Label(tab3, text='商品id:', font=('Arial', 13)).place(x=50, y=520)
goods_id4 = tk.StringVar()
enter_goods_id4 = tk.Entry(tab3, textvariable=goods_id4, font=('Arial', 14))
enter_goods_id4.place(x=200, y=520)
tk.Label(tab3, text='商品新名称:', font=('Arial', 13)).place(x=50, y=550)
new_goods_name = tk.StringVar()
enter_new_goods_name = tk.Entry(tab3, textvariable=new_goods_name, font=('Arial', 14))
enter_new_goods_name.place(x=200, y=550)
tk.Label(tab3, text='商品新售价:', font=('Arial', 13)).place(x=50, y=580)
new_price = tk.StringVar()
enter_new_price = tk.Entry(tab3, textvariable=new_price, font=('Arial', 14))
enter_new_price.place(x=200, y=580)
tk.Label(tab3, text='商品新成本:', font=('Arial', 13)).place(x=50, y=610)
new_cost = tk.StringVar()
enter_new_cost = tk.Entry(tab3, textvariable=new_cost, font=('Arial', 14))
enter_new_cost.place(x=200, y=610)
tk.Label(tab3, text='商品新数量:', font=('Arial', 13)).place(x=50, y=640)
new_quantity = tk.StringVar()
enter_new_quantity = tk.Entry(tab3, textvariable=new_quantity, font=('Arial', 14))
enter_new_quantity.place(x=200, y=640)
modify_single_goods_info_btn = tk.Button(tab3, text='修改商品信息',
                                         command=lambda: connectlib.modify_single_goods_info(enter_goods_id4.get(),
                                                                                             enter_new_goods_name.get(),
                                                                                             enter_new_price.get(),
                                                                                             enter_new_cost.get(),
                                                                                             enter_new_quantity.get()))
modify_single_goods_info_btn.place(x=270, y=670)

print(type_user)
if type_user == 1:
    tab1.destroy()
    tab2.destroy()
elif type_user == 2:
    tab2.destroy()
    tab3.destroy()
elif type_user == 3:
    tab1.destroy()
    tab3.destroy()
root.mainloop()
