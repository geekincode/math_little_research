# from Hyperbola_draw import hyperbola

import tkinter as tk  

from tkinter import *

# def e1press1(self):
#     e1.config(bg='skyblue')
# def e1press2(self):
#     e1.config(bg='white')
# def e2press1(self):
#     e2.config(bg='skyblue')
# def e2press2(self):
#     e2.config(bg='white')
# def e3press1(self):
#     e3.config(bg='skyblue')
# def e3press2(self):
#     e3.config(bg='white')

# def draw():

#     global h
#     a = eval(e1.get())
#     b = eval(e2.get())
#     ax_range = eval(e4.get())
#     # line_range = eval(e5.get())
#     focus_ax = e3.get()
#     h = hyperbola(ax_range,ax_range*7)
#     h.hb_data(a,b,focus=focus_ax)
#     h.hb_draw()
#     h.asymptote()

# def show():
#     global h
#     h.display()

class GUI():
    # from tkinter import *
    def __init__(self):
        from Hyperbola_draw import hyperbola
        # import tkinter as tk
        from tkinter import Tk

        self.root = root =Tk()
        root.geometry('500x350')
        root.geometry('+400+300')
        root.title('双曲线')
        root.resizable(False, False)
        self.label_entry()
        self.button()
        self.show()
        ax_range = self.ax_range = 10
        # self.h = hyperbola(ax_range,ax_range*7)

    def label_entry(self):
        root = self.root
        self.l1 = l1 = tk.Label(root, text='a:', 
                        font=('Arial Black',12),
                        width=3, height=1)
        l1.place(relx=0.25, rely=0.03)

        self.l2 = l2 = tk.Label(root, text='b:', 
                        font=('Arial Black',12),
                        width=3, height=1)
        l2.place(relx=0.25, rely=0.13)

        self.l3 = l3 = tk.Label(root, text='焦点：', 
                        font=('楷体',13),
                        width=5, height=1)
        l3.place(relx=0.215, rely=0.23)

        self.l3_ = l3_ = tk.Label(root, text='x or y', 
                        font=('Arial',10),
                        width=5, height=1)
        l3_.place(relx=0.65, rely=0.23)

        self.l4 = l4 = tk.Label(root, text='坐标轴长度：', 
                        font=('楷体',13),
                        width=13, height=1)
        l4.place(relx=0.15, rely=0.33)


        self.e1 = e1 = tk.Entry(root, show = None, bg='white',font=('Arial',10))#显示成明文形式
        e1.place(relx=0.35,rely=0.05)


        self.e2 = e2 = tk.Entry(root, show = None, bg='white', font=('Arial',10))#显示成明文形式
        e2.place(relx=0.35, rely=0.15)

        # self.e3 = e3 = tk.Entry(root, show = None, bg='white', font=('Arial',10))#显示成明文形式
        # e3.place(relx=0.35, rely=0.25)
        self.b1 = b1 = Radiobutton(root,text='X轴', value='x', variable='x', command=self.Rb1_get)
        self.b2 = b2 = Radiobutton(root,text='Y轴', value='y', variable='x', command=self.Rb2_get)
        b1.place(relx=0.35, rely=0.25)
        b2.place(relx=0.50, rely=0.25)

        self.e4 = e4 = tk.Entry(root, show = None, bg='white', font=('Arial',10))#显示成明文形式
        e4.place(relx=0.35, rely=0.35)
    
    def Rb1_get(self):
        self.s = s = StringVar()
        s.set('x')

    def Rb2_get(self):
        self.s= s = StringVar()
        s.set('y')

    def button(self):
        root = self.root
        # e5 = tk.Entry(root, show = None, bg='white', font=('Arial',10))#显示成明文形式
        # e5.place(relx=0.35, rely=0.45)
        # 第5步，在窗口界面设置放置Button按键hyperbola.Kp
        b1 = tk.Button(root,
                        text='Add', 
                        font=('Arial', 12), 
                        width=15, height=1, 
                        bg='lightcoral',
                        command=self.draw)
        b1.place(relx=0.38, rely=0.5)

        b2 = tk.Button(root,
                        text='Show Hyperbola', 
                        font=('Arial', 12), 
                        width=15, height=1, 
                        bg='lightcoral',
                        command=self.display)
        b2.place(relx=0.38, rely=0.75)

    def draw(self):
        from Hyperbola_draw import hyperbola
        e1, e2, e4 = self.e1, self.e2, self.e4
        a = eval(e1.get())
        b = eval(e2.get())
        ax_range = eval(e4.get())
        self.ax_range = ax_range
        # line_range = eval(e5.get())
        # focus_ax = e3.get()
        self.h = h = hyperbola(self.ax_range,self.ax_range*7)
        # h = self.h
        h.hb_data(a,b,focus=self.s)
        h.hb_draw()
        h.asymptote()

    def display(self):
        self.h.display()


    def show(self):
        self.root.mainloop()

# class function(GUI):
#     def __init__(self):
#         G = GUI()

    
#     def draw(a):
#         print(a)

GUI()


