from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import login
import cashier
import pymysql
import buyer
import administrator
import connectlib

# 主界面
root = Tk()
root.title('欢迎来到商品管理系统')  # 主界面名称
root.geometry('800x400+100+100')

tab_main = ttk.Notebook()  # 创建分页栏
tab_main.place(relx=0.02, rely=0.02, relwidth=0.887, relheight=0.876)
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
def showAllSale(odr, goods_type=-1, start_time='0000-00-00 00:00:00', end_time='2200-00-00 23:59:59'):
    x = tv.get_children()
    for item in x:
        tv.delete(item)
    start_time = '\'' + start_time + '\''
    end_time = '\'' + end_time + '\''
    db = pymysql.connect(user='root', password='', database='b1', charset='utf8')
    cursor = db.cursor()
    tp = ''
    if goods_type != -1:
        tp = 'and goods_type={}'.format(goods_type)
    # 两张表的quantity重名了。。。
    sql = "select goods_id, goods_name,sum(purchase.quantity) sum_quantity, sum(payment) sum_payment, sum(profit) " \
          f"sum_profit from purchase join goods using(goods_id) where time > {start_time} and time < {end_time} {tp} group " \
          f"by goods_id, goods_name  "
    cursor.execute(sql)
    res = cursor.fetchall()
    for item in res:
        tv.insert("", 1, text="line1", values=item)
        count = 0
        feedback = ''

        sum_all_payment = 0
        sum_all_profit = 0
        # feedback = count sum_all_payment sum_all_profit goods_id1, goods_name1, sum_quantity1, sum_payment1, sum_profit1 .
        for row in res:
            print(
                "goods_id={}\tgoods_name={}\tsum_quantity={}\tsum_payment={}\tsum_profit={}".format(row[0], row[1],
                                                                                                    row[2],
                                                                                                    row[3], row[4]))
            feedback = feedback + "{} {} {} {} {} ".format(row[0], row[1], row[2], row[3], row[4])
            count = count + 1
            sum_all_payment = sum_all_payment + row[3]
            sum_all_profit = sum_all_profit + row[4]

    db.close()

tab1 = Frame(tab_main)  # 创建收银员界面
tab1.place(x=30, y=30)
tab_main.add(tab1, text='修改密码')  # 将第一页插入分页栏中

tk.Label(tab1, text='排列方式:', font=('Arial', 13)).place(x=50, y=10)
odr = tk.StringVar()
enter_odr = tk.Entry(tab1, textvariable=odr, font=('Arial', 14))
enter_odr.place(x=200, y=10)
tk.Label(tab1, text='起始时间:', font=('Arial', 13)).place(x=50, y=40)
stime = tk.StringVar()
enter_stime = tk.Entry(tab1, textvariable=stime, font=('Arial', 14))
enter_stime.place(x=200, y=40)
tk.Label(tab1, text='结束时间:', font=('Arial', 13)).place(x=50, y=70)
etime = tk.StringVar()
enter_etime = tk.Entry(tab1, textvariable=etime, font=('Arial', 14))
enter_etime.place(x=200, y=70)

btn = ttk.Button(tab1, text="显示所有商品", command=lambda: showAllSale(enter_odr.get(), enter_stime.get(), enter_etime.get())).place(x=270, y=100, width=80)


tv = ttk.Treeview(tab1, show='headings', column=('goods_id', 'goods_name', 'sum_quantity', 'sum_payment', 'sum_profit'))
tv.column('goods_id', width=150, anchor="center")
tv.column('goods_name', width=150, anchor="center")
tv.column('sum_quantity', width=150, anchor="center")
tv.column('sum_payment', width=150, anchor="center")
tv.column('sum_profit', width=150, anchor="center")

tv.heading('goods_id', text='商品号')
tv.heading('goods_name', text='商品名称')
tv.heading('sum_quantity', text='总数')
tv.heading('sum_payment', text='总售价')
tv.heading('sum_profit', text='利润')
tv.place(rely=0.5, relwidth=1, relheight=0.8)

root.mainloop()

