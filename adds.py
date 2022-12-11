from tkinter import *
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import credentials as cr


class Add:
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


    # Removes all widgets from the frame 1 and frame 3
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

        for widget in self.frame_3.winfo_children():
            widget.destroy()

    '''Exit window'''

    def Exit(self):
        self.window.destroy()


# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Add(root)
    root.mainloop()