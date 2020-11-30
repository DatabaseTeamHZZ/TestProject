import random
from tkinter import ttk
from tkinter import *
import connectlib

root = Tk()  # 初始旷的声明
columns = ("a", "b", "c")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column('a', width=50, anchor='center')
treeview.column('b', width=100, anchor='center')
treeview.column('c', width=80, anchor='center')
treeview.heading('a', text='列1')
treeview.heading('b', text='列2')
treeview.heading('c', text='列3')
treeview.pack(side=LEFT, fill=BOTH)
str = connectlib.get_customers_info().split()
t = 0
while t+2 < len(str):
    if (t % 3 == 0):
        treeview.insert('', 'end', value=[str[t], str[t + 1], str[t + 2]])
    t = t + 3
root.mainloop()  # 进入消息循环
