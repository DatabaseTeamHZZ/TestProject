import pymysql
import tkinter as tk
import connectlib
import tkinter.messagebox
import pickle

# ↓请修改数据库基本信息↓
host = "127.0.0.1"
host_name = "root"
host_password = ""
database = "b1"


# 登录验证
def login_check(name, password):
    db = pymysql.connect(host, host_name, host_password, database)
    cursor = db.cursor()
    sql = "select password,user_type,if_logout from user where id='{}'".format(str(name))
    cursor.execute(sql)
    res = cursor.fetchone()
    user_type = 0  # 如果最终user_type仍然为0，说明登陆失败
    if res is None:
        # print(tkinter.messagebox.showerror(title='出错啦', message='无此用户！'))  # 提出错误对话窗
        print("无此用户！")
    elif res[0] != password:
        # print(tkinter.messagebox.showerror(title='出错啦', message='密码错误！'))  # 提出错误对话窗
        print("密码错误！")
    elif res[2] == 1:
        # print(tkinter.messagebox.showerror(title='出错啦', message='该用户已注销！'))  # 提出错误对话窗
        print("该用户已被注销！")
    else:
        user_type = res[1]  # 登陆成功后获取用户身份
        type_name = "未知身份"
        if user_type == 1:
            type_name = "管理员"
        elif user_type == 2:
            type_name = "收银员"
        elif user_type == 3:
            type_name = "进货员"
        print("{}id：{} ,登陆成功！".format(type_name, name))
    db.close()
    return user_type


