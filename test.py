from tkinter import *
root=Tk()
def jinru():
    root.destroy()
    global root1
    root1=Tk()
    root1.mainloop()
buff=Button(root,text="登录",command=jinru)
buff.pack()
root.mainloop()