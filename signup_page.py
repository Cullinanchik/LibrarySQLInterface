from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import pymysql, os
import credentials as cr

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Log In LibrarySystem")
        # Set the window size
        # Here 0,0 represents the starting point of the window
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="white")

        # ============================================================================
        # ==============================DESIGN PART===================================
        # ============================================================================

        self.frame = Frame(self.window, bg="yellow")
        self.frame.place(x=0, y=0, width=450, relheight=1)

        label1 = Label(self.frame, text="SQL", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(
            x=100,
            y=300)
        label2 = Label(self.frame, text="Library", font=("times new roman", 40, "bold"), bg="yellow",
                       fg="RoyalBlue1").place(x=180, y=300)
        label3 = Label(self.frame, text="Интерфейс библиотеки", font=("times new roman", 13, "bold"), bg="yellow",
                       fg="brown4").place(x=100, y=360)

        # =============Entry Field & Buttons============

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=500)

        self.user_label = Label(self.frame3, text="Пользователь", font=("helvetica", 20, "bold"), bg="white",
                                 fg="gray").place(x=50, y=40)
        self.user_txt = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.user_txt.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3, text="Пароль", font=("helvetica", 20, "bold"), bg="white",
                                    fg="gray").place(x=50, y=120)
        self.password_txt = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*")
        self.password_txt.place(x=50, y=160, width=300)

        self.passport_label = Label(self.frame3, text="Паспорт", font=("helvetica", 20, "bold"), bg="white",
                                fg="gray").place(x=50, y=200)
        self.passport_txt = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.passport_txt.place(x=50, y=240, width=300)

        self.address_label = Label(self.frame3, text="Адрес", font=("helvetica", 20, "bold"), bg="white",
                                    fg="gray").place(x=50, y=280)
        self.address_txt = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.address_txt.place(x=50, y=320, width=300)

        self.phone_label = Label(self.frame3, text="Телефон", font=("helvetica", 20, "bold"), bg="white",
                                   fg="gray").place(x=50, y=360)
        self.phone_txt = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.phone_txt.place(x=50, y=400, width=300)

        # ================Buttons===================
        self.login_button = Button(self.frame3, text="Зарегистрироваться", command=self.signup_func,
                                   font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="black",
                                   fg="black").place(x=50, y=460, width=300)

    def signup_func(self):
        if self.user_txt.get()=="" or self.password_txt.get() == "" or self.passport_txt.get()=="" or self.address_txt.get()=="" or self.phone_txt.get()=="":
            messagebox.showerror("Error!","Извините!, Заполните все поля!",parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from readers where name=%s",self.user_txt.get())
                row=cur.fetchone()

                # Check if th entered email id is already exists or not.
                if row!=None:
                    messagebox.showerror("Error!","Пользователь уже зарегестрирован!",parent=self.window)
                else:
                    cur.execute("insert into readers (name, password, passport,address,phone) values(%s,%s,%s,%s,%s)",
                                    (
                                        self.user_txt.get(),
                                        self.password_txt.get(),
                                        self.passport_txt.get(),
                                        self.address_txt.get(),
                                        self.phone_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Поздравляю!","Регистрация прошла успешна!",parent=self.window)
                    self.reset_fields()
            except Exception as es:
                messagebox.showerror("Error!", f"Error due to {es}",parent=self.window)

    def reset_fields(self):
        self.user_txt.delete(0, END)
        self.password_txt.delete(0, END)
        self.passport_txt.delete(0, END)
        self.address_txt.delete(0, END)
        self.phone_txt.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
