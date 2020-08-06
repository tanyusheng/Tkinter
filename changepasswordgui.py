from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import os

class ChangePasswordWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title("修改密码")
        self.geometry("600x500+600+150")
        self.resizable(0,0) # 不能改变大小

        # 加载界面
        self.setup_UI()

    def setup_UI(self):
        # 设置style
        self.Style01 = Style()
        self.Style01.configure("title.TLabel", font=("微软雅黑", 25, "bold"), foreground="navy")
        self.Style01.configure("TLabel", font=("微软雅黑", 16, "bold"), foreground="navy")
        self.Style01.configure("TButton", font=("微软雅黑", 16, "bold"), foreground="navy")
        self.Style01.configure("TEntry", font=("微软雅黑", 16, "bold"), width=10)
        self.Style01.configure("TRadiobutton", font=("微软雅黑", 16, "bold"), foreground="navy")
        # 加载上面的banner
        self.Login_image = PhotoImage(file="." + os.sep + "img" + os.sep + "stu_detail_banner.png")
        self.Label_image = Label(self, image=self.Login_image)
        self.Label_image.pack()

        # 添加一个title
        self.Label_title = Label(self, text="==修改密码==", style="title.TLabel")
        self.Label_title.place(x=360, y=20)

        # 加载一个pane
        self.Pane_detail = PanedWindow(self, width=590, height=380)
        self.Pane_detail.place(x=5, y=88)

        # 放置两个按钮
        self.Button_save = Button(self, text="保存", style="TButton")
        self.Button_save.place(x=300, y=472)
        self.Button_exit = Button(self, text="关闭", style="TButton")
        self.Button_exit.place(x=450, y=472)
