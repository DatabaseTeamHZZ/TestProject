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
host_password = ""
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
        self.window.title('欢迎来到商品进销与人员管理系统')
        self.window.geometry('400x200')
        # 用户信息
        tk.Label(self.window, text='用户名:', font=('Arial', 14)).place(x=10, y=50)
        tk.Label(self.window, text='密码:', font=('Arial', 14)).place(x=10, y=100)
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
root.title('欢迎来到商品管理系统')  # 主界面名称
root.geometry('800x400+100+100')

tab_main = ttk.Notebook()  # 创建分页栏
tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)

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
tk.Label(tab1, text='请输入 id:', font=('Arial', 13)).place(x=50, y=40)
cashier_id = tk.StringVar()
cashier_name = tk.Entry(tab1, textvariable=cashier_id, font=('Arial', 14))
cashier_name.place(x=200, y=40)
tk.Label(tab1, text='请输入旧密码:', font=('Arial', 13)).place(x=50, y=90)
cashier_old_pwd = tk.StringVar()
enter_old_pwd = tk.Entry(tab1, textvariable=cashier_old_pwd, font=('Arial', 14), show='*')
enter_old_pwd.place(x=200, y=90)
tk.Label(tab1, text='请输入新密码:', font=('Arial', 13)).place(x=50, y=140)
cashier_new_pwd = tk.StringVar()
enter_new_pwd = tk.Entry(tab1, textvariable=cashier_new_pwd, font=('Arial', 14), show='*')
enter_new_pwd.place(x=200, y=140)
change_pwd_btn = tk.Button(tab1, text='修改密码',
                           command=lambda: connectlib.modify_account_password(cashier_name.get(), enter_old_pwd.get(),
                                                                              enter_new_pwd.get()))
change_pwd_btn.place(x=270, y=180)

# 2，修改个人信息
tk.Label(tab2, text='请输入id:', font=('Arial', 13)).place(x=50, y=40)
cashier_cname = tk.StringVar()
enter_name = tk.Entry(tab2, textvariable=cashier_cname, font=('Arial', 14))
enter_name.place(x=200, y=40)
tk.Label(tab2, text='请输入新用户名:', font=('Arial', 13)).place(x=50, y=90)
cashier_new_name = tk.StringVar()
enter_new_name = tk.Entry(tab2, textvariable=cashier_new_name, font=('Arial', 14))
enter_new_name.place(x=200, y=90)
tk.Label(tab2, text='请输入新手机号码:', font=('Arial', 13)).place(x=50, y=140)
cashier_new_phone = tk.StringVar()
enter_new_phone = tk.Entry(tab2, textvariable=cashier_new_phone, font=('Arial', 14))
enter_new_phone.place(x=200, y=140)
change_info_btn = tk.Button(tab2, text='修改个人信息',
                            command=lambda: connectlib.modify_cashier_info(enter_name.get(), enter_new_name.get(),
                                                                           enter_new_phone.get()))
change_info_btn.place(x=255, y=180)

# 3，交易：
tk.Label(tab3, text='请输入顾客id:', font=('Arial', 13)).place(x=50, y=40)
customer_id = tk.StringVar()
enter_customer_id = tk.Entry(tab3, textvariable=customer_id, font=('Arial', 14))
enter_customer_id.place(x=200, y=40)
tk.Label(tab3, text='请输入商品号:', font=('Arial', 13)).place(x=50, y=90)
goods_id = tk.StringVar()
enter_goods_id = tk.Entry(tab3, textvariable=goods_id, font=('Arial', 14))
enter_goods_id.place(x=200, y=90)
tk.Label(tab3, text='请输入交易数量:', font=('Arial', 13)).place(x=50, y=140)
quantity = tk.StringVar()
enter_quantity = tk.Entry(tab3, textvariable=quantity, font=('Arial', 14))
enter_quantity.place(x=200, y=140)
purchase_btn = tk.Button(tab3, text='交易',
                         command=lambda: connectlib.purchase(enter_customer_id.get(), enter_goods_id.get(),
                                                             enter_quantity.get()))
purchase_btn.place(x=280, y=180)

# 4，购买点数
tk.Label(tab4, text='请输入顾客id:', font=('Arial', 13)).place(x=50, y=40)
customer_id2 = tk.StringVar()
enter_customer_id2 = tk.Entry(tab4, textvariable=customer_id2, font=('Arial', 14))
enter_customer_id2.place(x=200, y=40)
tk.Label(tab4, text='请输入购买点数:', font=('Arial', 13)).place(x=50, y=90)
point = tk.StringVar()
enter_point = tk.Entry(tab4, textvariable=point, font=('Arial', 14))
enter_point.place(x=200, y=90)
get_point = tk.Button(tab4, text='购买点数',
                      command=lambda: connectlib.buy_point(enter_customer_id2.get(), enter_point.get()))
get_point.place(x=270, y=130)

# 5，添加顾客
tk.Label(tab5, text='请输入顾客名称:', font=('Arial', 13)).place(x=50, y=40)
customer_name = tk.StringVar()
enter_customer_name = tk.Entry(tab5, textvariable=customer_name, font=('Arial', 14))
enter_customer_name.place(x=200, y=40)
tk.Label(tab5, text='请输入顾客电话:', font=('Arial', 13)).place(x=50, y=90)
customer_phone = tk.StringVar()
enter_customer_phone = tk.Entry(tab5, textvariable=customer_phone, font=('Arial', 14))
enter_customer_phone.place(x=200, y=90)
register_customer = tk.Button(tab5, text='注册顾客',
                              command=lambda: connectlib.sign_up_new_customer(enter_customer_name.get(),
                                                                              enter_customer_phone.get()))
register_customer.place(x=270, y=130)

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

##########
# 进 货 员 界 面 #
##########

# 1，修改密码
tk.Label(tab6, text='请输入 id:', font=('Arial', 13)).place(x=50, y=40)
buyer_id = tk.StringVar()
enter_buyer_id = tk.Entry(tab6, textvariable=buyer_id, font=('Arial', 14))
enter_buyer_id.place(x=200, y=40)
tk.Label(tab6, text='请输入旧密码:', font=('Arial', 13)).place(x=50, y=90)
buyer_old_pwd = tk.StringVar()
enter_buyer_old_pwd = tk.Entry(tab6, textvariable=buyer_old_pwd, font=('Arial', 14), show='*')
enter_buyer_old_pwd.place(x=200, y=90)
tk.Label(tab6, text='请输入新密码:', font=('Arial', 13)).place(x=50, y=140)
buyer_new_pwd = tk.StringVar()
enter_buyer_new_pwd = tk.Entry(tab6, textvariable=buyer_new_pwd, font=('Arial', 14), show='*')
enter_buyer_new_pwd.place(x=200, y=140)
change_buyer_pwd_btn = tk.Button(tab6, text='修改密码',
                                 command=lambda: connectlib.modify_account_password(enter_buyer_id.get(),
                                                                                    enter_buyer_old_pwd.get(),
                                                                                    enter_buyer_new_pwd.get()))
change_buyer_pwd_btn.place(x=270, y=170)

# 2，修改个人信息
tk.Label(tab7, text='请输入id:', font=('Arial', 13)).place(x=50, y=40)
buyer_cname = tk.StringVar()
enter_buyer_name = tk.Entry(tab7, textvariable=buyer_cname, font=('Arial', 14))
enter_buyer_name.place(x=200, y=40)
tk.Label(tab7, text='请输入新用户名:', font=('Arial', 13)).place(x=50, y=90)
buyer_new_name = tk.StringVar()
enter_buyer_new_name = tk.Entry(tab7, textvariable=buyer_new_name, font=('Arial', 14))
enter_buyer_new_name.place(x=200, y=90)
tk.Label(tab7, text='请输入新手机号码:', font=('Arial', 13)).place(x=50, y=140)
buyer_new_phone = tk.StringVar()
enter_buyer_new_phone = tk.Entry(tab7, textvariable=buyer_new_phone, font=('Arial', 14))
enter_buyer_new_phone.place(x=200, y=140)
change_buyer_info_btn = tk.Button(tab7, text='修改个人信息',
                                  command=lambda: connectlib.modify_buyer_info(enter_buyer_name.get(),
                                                                               enter_buyer_new_name.get(),
                                                                               enter_buyer_new_phone.get()))
change_buyer_info_btn.place(x=255, y=170)

# 3，添加商品
tk.Label(tab8, text='请输入商品名称:', font=('Arial', 13)).place(x=50, y=40)
goods_name = tk.StringVar()
enter_goods_name = tk.Entry(tab8, textvariable=goods_name, font=('Arial', 14))
enter_goods_name.place(x=200, y=40)
tk.Label(tab8, text='请输入商品售价:', font=('Arial', 13)).place(x=50, y=90)
goods_price = tk.StringVar()
enter_goods_price = tk.Entry(tab8, textvariable=goods_price, font=('Arial', 14))
enter_goods_price.place(x=200, y=90)
tk.Label(tab8, text='请输入商品成本:', font=('Arial', 13)).place(x=50, y=140)
goods_cost = tk.StringVar()
enter_goods_cost = tk.Entry(tab8, textvariable=goods_cost, font=('Arial', 14))
enter_goods_cost.place(x=200, y=140)
tk.Label(tab8, text='请输入商品类型:', font=('Arial', 13)).place(x=50, y=190)
goods_type = tk.StringVar()
enter_goods_type = tk.Entry(tab8, textvariable=goods_type, font=('Arial', 14))
enter_goods_type.place(x=200, y=190)
add_goods_btn = tk.Button(tab8, text='添加商品',
                          command=lambda: connectlib.create_new_goods(enter_goods_name.get(), enter_goods_price.get(),
                                                                      enter_goods_cost.get(), enter_goods_type.get()))
add_goods_btn.place(x=280, y=230)

# 4，进货
tk.Label(tab9, text='请输入商品id:', font=('Arial', 13)).place(x=50, y=40)
goods_id2 = tk.StringVar()
enter_goods_id2 = tk.Entry(tab9, textvariable=goods_id2, font=('Arial', 14))
enter_goods_id2.place(x=200, y=40)
tk.Label(tab9, text='请输入id:', font=('Arial', 13)).place(x=50, y=90)
buyer_id2 = tk.StringVar()
enter_buyer_id2 = tk.Entry(tab9, textvariable=buyer_id2, font=('Arial', 14))
enter_buyer_id2.place(x=200, y=90)
tk.Label(tab9, text='请输入进货数量:', font=('Arial', 13)).place(x=50, y=140)
add_goods_quantity = tk.StringVar()
enter_add_goods_quantity = tk.Entry(tab9, textvariable=add_goods_quantity, font=('Arial', 14))
enter_add_goods_quantity.place(x=200, y=140)
add_goods_quantity_btn = tk.Button(tab9, text='添加商品',
                                   command=lambda: connectlib.stock(enter_goods_id2.get(), enter_buyer_id2.get(),
                                                                    enter_add_goods_quantity.get()))
add_goods_quantity_btn.place(x=280, y=180)

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
tk.Label(tab10, text='请输入密码:', font=('Arial', 13)).place(x=50, y=40)
user_pwd = tk.StringVar()
enter_user_pwd = tk.Entry(tab10, textvariable=user_pwd, font=('Arial', 14), show='*')
enter_user_pwd.place(x=200, y=40)
tk.Label(tab10, text='请输入用户类型:', font=('Arial', 13)).place(x=50, y=90)
new_user_type = tk.StringVar()
enter_new_user_type = tk.Entry(tab10, textvariable=new_user_type, font=('Arial', 14))
enter_new_user_type.place(x=200, y=90)
new_user_btn = tk.Button(tab10, text='新建用户',
                         command=lambda: connectlib.register(enter_user_pwd.get(), enter_new_user_type.get()))
new_user_btn.place(x=270, y=130)

# 2，注销用户
tk.Label(tab11, text='注销id:', font=('Arial', 13)).place(x=50, y=40)
logout_id = tk.StringVar()
enter_logout_id = tk.Entry(tab11, textvariable=logout_id, font=('Arial', 14))
enter_logout_id.place(x=200, y=40)
logout_user_btn = tk.Button(tab11, text='注销用户', command=lambda: connectlib.logout(enter_logout_id.get()))
logout_user_btn.place(x=270, y=80)

# 3，查看用户信息
get_customer_btn = tk.Button(tab12, text='用户信息', command=connectlib.get_customers_info)
get_customer_btn.place(x=200, y=100)

# 4，查看进货信息
get_stock_btn = tk.Button(tab13, text='进货信息', command=connectlib.get_stock)
get_stock_btn.place(x=350, y=100)

# 5，查询销售情况
tk.Label(tab14, text='排序方式:', font=('Arial', 13)).place(x=50, y=40)
odr = tk.StringVar()
enter_odr = tk.Entry(tab14, textvariable=odr, font=('Arial', 14))
enter_odr.place(x=200, y=40)
tk.Label(tab14, text='起始时间:', font=('Arial', 13)).place(x=50, y=90)
start_time = tk.StringVar()
enter_start_time = tk.Entry(tab14, textvariable=start_time, font=('Arial', 14))
enter_start_time.place(x=200, y=90)
tk.Label(tab14, text='截止时间:', font=('Arial', 13)).place(x=50, y=140)
end_time = tk.StringVar()
enter_end_time = tk.Entry(tab14, textvariable=end_time, font=('Arial', 14))
enter_end_time.place(x=200, y=140)
get_sale_btn = tk.Button(tab14, text='查询销售情况',
                         command=lambda: connectlib.get_sale_in_period(enter_odr.get(), enter_start_time.get(),
                                                                       enter_end_time.get()))
get_sale_btn.place(x=270, y=180)

# 6，查询VIP交易
tk.Label(tab15, text='起始时间:', font=('Arial', 13)).place(x=50, y=40)
vip_start_time = tk.StringVar()
enter_vip_start_time = tk.Entry(tab15, textvariable=vip_start_time, font=('Arial', 14))
enter_vip_start_time.place(x=200, y=40)
tk.Label(tab15, text='截止时间:', font=('Arial', 13)).place(x=50, y=90)
vip_end_time = tk.StringVar()
enter_vip_end_time = tk.Entry(tab15, textvariable=vip_end_time, font=('Arial', 14))
enter_vip_end_time.place(x=200, y=90)
get_vip_purchase_btn = tk.Button(tab15, text='查询VIP交易情况',
                                 command=lambda: connectlib.get_vip_sale_in_period(enter_vip_start_time.get(),
                                                                                   enter_vip_end_time.get()))
get_vip_purchase_btn.place(x=270, y=130)

# 7，查询商品信息
tk.Label(tab16, text='商品id:', font=('Arial', 13)).place(x=50, y=40)
goods_id3 = tk.StringVar()
enter_goods_id3 = tk.Entry(tab16, textvariable=goods_id3, font=('Arial', 14))
enter_goods_id3.place(x=200, y=40)
get_single_goods_info_btn = tk.Button(tab16, text='商品信息',
                                      command=lambda: connectlib.get_single_goods_info(enter_goods_id3.get()))
get_single_goods_info_btn.place(x=270, y=80)

# 8，修改商品信息
tk.Label(tab17, text='商品id:', font=('Arial', 13)).place(x=50, y=40)
goods_id4 = tk.StringVar()
enter_goods_id4 = tk.Entry(tab17, textvariable=goods_id4, font=('Arial', 14))
enter_goods_id4.place(x=200, y=40)
tk.Label(tab17, text='商品新名称:', font=('Arial', 13)).place(x=50, y=90)
new_goods_name = tk.StringVar()
enter_new_goods_name = tk.Entry(tab17, textvariable=new_goods_name, font=('Arial', 14))
enter_new_goods_name.place(x=200, y=90)
tk.Label(tab17, text='商品新售价:', font=('Arial', 13)).place(x=50, y=140)
new_price = tk.StringVar()
enter_new_price = tk.Entry(tab17, textvariable=new_price, font=('Arial', 14))
enter_new_price.place(x=200, y=140)
tk.Label(tab17, text='商品新成本:', font=('Arial', 13)).place(x=50, y=190)
new_cost = tk.StringVar()
enter_new_cost = tk.Entry(tab17, textvariable=new_cost, font=('Arial', 14))
enter_new_cost.place(x=200, y=190)
tk.Label(tab17, text='商品新数量:', font=('Arial', 13)).place(x=50, y=240)
new_quantity = tk.StringVar()
enter_new_quantity = tk.Entry(tab17, textvariable=new_quantity, font=('Arial', 14))
enter_new_quantity.place(x=200, y=240)
modify_single_goods_info_btn = tk.Button(tab17, text='修改商品信息',
                                         command=lambda: connectlib.modify_single_goods_info(enter_goods_id4.get(),
                                                                                             enter_new_goods_name.get(),
                                                                                             enter_new_price.get(),
                                                                                             enter_new_cost.get(),
                                                                                             enter_new_quantity.get()))
modify_single_goods_info_btn.place(x=270, y=280)

#   9.查询各种商品类型的在一定时间内的总利润排名
tk.Label(tab18, text='开始时间:', font=('Arial', 13)).place(x=50, y=40)
start_time1 = tk.StringVar()
enter_start_time1 = tk.Entry(tab18, textvariable=start_time1, font=('Arial', 14))
enter_start_time1.place(x=200, y=40)
tk.Label(tab18, text='结束时间:', font=('Arial', 13)).place(x=50, y=90)
end_time1 = tk.StringVar()
enter_end_time1 = tk.Entry(tab18, textvariable=end_time1, font=('Arial', 14))
enter_end_time1.place(x=200, y=90)
get_profit_rank_btn = tk.Button(tab18, text='利润排名',
                                command=lambda: connectlib.get_type_profit(enter_start_time1.get(),
                                                                           enter_end_time1.get()))
get_profit_rank_btn.place(x=270, y=130)

#   10.查询所有顾客的在一定时间内的总消费排名
tk.Label(tab19, text='开始时间:', font=('Arial', 13)).place(x=50, y=40)
start_time2 = tk.StringVar()
enter_start_time2 = tk.Entry(tab19, textvariable=start_time2, font=('Arial', 14))
enter_start_time2.place(x=200, y=40)
tk.Label(tab19, text='结束时间:', font=('Arial', 13)).place(x=50, y=90)
end_time2 = tk.StringVar()
enter_end_time2 = tk.Entry(tab19, textvariable=end_time2, font=('Arial', 14))
enter_end_time2.place(x=200, y=90)
get_buy_rank_btn = tk.Button(tab19, text='消费排名',
                             command=lambda: connectlib.get_customer_consume_rank(enter_start_time2.get(),
                                                                                  enter_end_time2.get()))
get_buy_rank_btn.place(x=270, y=130)

#   11.查询一个特定的顾客的vip点获得记录
tk.Label(tab20, text='用户id:', font=('Arial', 13)).place(x=50, y=40)
vip_id = tk.StringVar()
enter_vip_id = tk.Entry(tab20, textvariable=vip_id, font=('Arial', 14))
enter_vip_id.place(x=200, y=40)
vip_point_btn = tk.Button(tab20, text='查询vip点',
                          command=lambda: connectlib.get_single_customer_point(enter_vip_id.get()))
vip_point_btn.place(x=270, y=80)

#   12.查询某一未注销员工的个人信息
tk.Label(tab21, text='用户id:', font=('Arial', 13)).place(x=50, y=40)
customer_id3 = tk.StringVar()
enter_customer_id3 = tk.Entry(tab21, textvariable=customer_id3, font=('Arial', 14))
enter_customer_id3.place(x=200, y=40)
get_info_btn = tk.Button(tab21, text='查询vip点',
                         command=lambda: connectlib.get_single_staff_info(enter_customer_id3.get()))
get_info_btn.place(x=270, y=80)

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
elif type_user == 2:
    tab6.destroy()
    tab7.destroy()
    tab8.destroy()
    tab9.destroy()
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
