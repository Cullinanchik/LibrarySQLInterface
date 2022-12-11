from tkinter import *
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import credentials as cr
from adds import Add
from finds import Find
from selects import Select


class Management_User:
    def __init__(self, root):
        self.window = root
        self.window.title("Library Management System")
        self.window.geometry("1070x540")
        self.window.config(bg="white")

        # Left Frame
        self.frame_1 = Frame(self.window, bg="yellow")
        self.frame_1.place(x=0, y=0, width=650, relheight=1)

        label1 = Label(self.frame_1, text="SQL", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(
            x=100,
            y=200)
        label2 = Label(self.frame_1, text="Library", font=("times new roman", 40, "bold"), bg="yellow",
                       fg="RoyalBlue1").place(x=180, y=200)
        label3 = Label(self.frame_1, text="Интерфейс библиотеки", font=("times new roman", 13, "bold"), bg="yellow",
                       fg="brown4").place(x=100, y=250)

        # Right Frame
        self.frame_2 = Frame(self.window, bg="gray95")
        self.frame_2.place(x=650, y=0, relwidth=1, relheight=1)

        # A frame inside the right frame
        self.frame_3 = Frame(self.frame_2, bg=cs.color_2)
        self.frame_3.place(x=0, y=300, relwidth=1, relheight=1)

        label_admin = Label(self.frame_2, text="Вы вошли как пользователь", font=("times new roman", 13, "bold"),
                            bg="yellow",
                            fg="brown4").place(x=230, y=20)

        # All the Buttons in the frame 2
        self.exit = Button(self.frame_2, text='Добавить', font=(cs.font_1, 16), bd=2, command=self.addTransition, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=260, width=400, height=70)
        self.exit = Button(self.frame_2, text='Найти', font=(cs.font_1, 16), bd=2, command=self.findTransition, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=170, width=400, height=70)
        self.exit = Button(self.frame_2, text='Показать', font=(cs.font_1, 16), bd=2, command=self.selectTransition, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=80, width=400, height=70)
        self.exit = Button(self.frame_2, text='Выйти', font=(cs.font_1, 16), bd=2, command=self.Exit, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=350, width=400, height=70)

    def Exit(self):
        self.window.destroy()


    def addTransition(self):
        self.redirect_window_adds()

    def findTransition(self):
        self.redirect_window_finds()

    def selectTransition(self):
        self.redirect_window_selects()


    def redirect_window_adds(self):
        self.window.destroy()
        root = Tk()
        obj = Add(root)
        root.mainloop()
    def redirect_window_finds(self):
        self.window.destroy()
        root = Tk()
        obj = Find(root)
        root.mainloop()
    def redirect_window_selects(self):
        self.window.destroy()
        root = Tk()
        obj = Select(root)
        root.mainloop()



# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Management_User(root)
    root.mainloop()
