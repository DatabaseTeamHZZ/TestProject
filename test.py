from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import login
import cashier
import pymysql
import buyer
import administrator
import connectlib

host = "127.0.0.1"
host_name = "root"
host_password = "hanxu1125"
database = "b1"

# 主界面
root = Tk()
root.title('欢迎来到商品管理系统')  # 主界面名称
root.geometry('800x400+100+100')

tab_main = ttk.Notebook()  # 创建分页栏
tab_main.place(relx=0, rely=0, relwidth=1, relheight=1)


# def showAllGoods():
#     x = tv.get_children()
#     for item in x:
#         tv.delete(item)
#     con = pymysql.connect(user='root', password='hanxu1125', database='b1', charset='utf8')
#     cur = con.cursor()
#     cur.execute("select * from goods")
#     lst = cur.fetchall()
#     # lst1 = cur.fetchall()
#     # treeview的插入方法
#     for item in lst:
#         tv.insert("", 1, text="line1", values=item)
#     cur.close()
#     con.close()

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

tab8 = Frame(tab_main)  # 创建收银员界面
tab8.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)
tab_main.add(tab8, text='修改密码')  # 将第一页插入分页栏中

tk.Label(tab8, text='请输入商品名称:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.2)
goods_name = tk.StringVar()
enter_goods_name = tk.Entry(tab8, textvariable=goods_name, font=('潮字社国风冉宋简-闪', 16))
enter_goods_name.place(relx=0.46, rely=0.2)
tk.Label(tab8, text='请输入商品售价:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.35)
goods_price = tk.StringVar()
enter_goods_price = tk.Entry(tab8, textvariable=goods_price, font=('潮字社国风冉宋简-闪', 16))
enter_goods_price.place(relx=0.46, rely=0.35)
tk.Label(tab8, text='请输入商品成本:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.5)
goods_cost = tk.StringVar()
enter_goods_cost = tk.Entry(tab8, textvariable=goods_cost, font=('潮字社国风冉宋简-闪', 16))
enter_goods_cost.place(relx=0.46, rely=0.5)
tk.Label(tab8, text='请输入商品类型:', font=('潮字社国风冉宋简-闪', 16)).place(relx=0.25, rely=0.65)
goods_type = tk.StringVar()
enter_goods_type = tk.Entry(tab8, textvariable=goods_type, font=('潮字社国风冉宋简-闪', 16))
enter_goods_type.place(relx=0.46, rely=0.65)
add_goods_btn = tk.Button(tab8, text='添加商品', font=('潮字社国风冉宋简-闪', 16),
                          command=lambda: connectlib.create_new_goods(enter_goods_name.get(), enter_goods_price.get(),
                                                                      enter_goods_cost.get(), enter_goods_type.get()))
add_goods_btn.place(relx=0.45, rely=0.8)
root.mainloop()
