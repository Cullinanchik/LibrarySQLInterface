from tkinter import *
from tkinter import ttk, messagebox
import pymysql
import os
from signup_page import SignUp
from main_user import Management_User
from main_admin import Management_Admin
import credentials as cr

class login_page:
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

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        label1 = Label(self.frame1, text="SQL", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place(x=100,
                                                                                                                  y=300)
        label2 = Label(self.frame1, text="Library", font=("times new roman", 40, "bold"), bg="yellow",
                       fg="RoyalBlue1").place(x=180, y=300)
        label3 = Label(self.frame1, text="Интерфейс библиотеки", font=("times new roman", 13, "bold"), bg="yellow",
                       fg="brown4").place(x=100, y=360)

        # =============Entry Field & Buttons============

        self.frame2 = Frame(self.window, bg="gray95")
        self.frame2.place(x=450, y=0, relwidth=1, relheight=1)

        self.frame3 = Frame(self.frame2, bg="white")
        self.frame3.place(x=140, y=150, width=500, height=450)

        self.username = Label(self.frame3, text="Пользователь", font=("helvetica", 20, "bold"), bg="white",
                                 fg="gray").place(x=50, y=40)
        self.username_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray")
        self.username_entry.place(x=50, y=80, width=300)

        self.password_label = Label(self.frame3, text="Пароль", font=("helvetica", 20, "bold"), bg="white",
                                    fg="gray").place(x=50, y=120)
        self.password_entry = Entry(self.frame3, font=("times new roman", 15, "bold"), bg="white", fg="gray", show="*")
        self.password_entry.place(x=50, y=160, width=300)

        #================Buttons===================
        self.login_button = Button(self.frame3,text="Авторизоваться",command=self.login_func,font=("times new roman",15, "bold"),bd=0,cursor="hand2",bg="black",fg="black").place(x=50,y=200,width=300)

        self.admin_button = Button(self.frame3, text="Авторизоваться как администратор", command=self.admin_func, font=("times new roman", 15, "bold"), bd=0, cursor="hand2", bg="black", fg="black").place(x=50, y=250, width=300)
        self.create_button = Button(self.frame3,text="Создать аккаунт",command=self.redirect_window,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="black",fg="black").place(x=80,y=320,width=250)


    def login_func(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Ошибка!","Заполните все поля",parent=self.window)
        else:
            try:
                connection=pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from readers where name=%s and password=%s",(self.username_entry.get(),self.password_entry.get()))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Ошибка!","Неверное имя или пароль",parent=self.window)
                else:
                    messagebox.showinfo("Успешно","Добро пожаловать!",parent=self.window)
                    # Clear all the entries
                    self.redirect_window_user()
                    self.reset_fields()
                    
                    connection.close()

            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def admin_func(self):
        if self.username_entry.get() == "" or self.password_entry.get() == "":
            messagebox.showerror("Ошибка!", "Заполните все поля", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                cur = connection.cursor()
                cur.execute("select * from administrators where login=%s and password=%s",
                            (self.username_entry.get(), self.password_entry.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Ошибка!", "Неверное имя или пароль", parent=self.window)
                else:
                    messagebox.showinfo("Успшено", "Добро пожаловать, админ!", parent=self.window)
                    # Clear all the entries
                    self.redirect_window_admin()
                    self.reset_fields()

                    connection.close()

            except Exception as e:
                messagebox.showerror("Ошибка!", f"Error due to {str(e)}", parent=self.window)
            

    def redirect_window(self):
        self.window.destroy()
        # Importing the signup window.
        # The page must be in the same directory
        root = Tk()
        obj = SignUp(root)
        root.mainloop()
    def redirect_window_user(self):
        self.window.destroy()
        root = Tk()
        obj = Management_User(root)
        root.mainloop()
    def redirect_window_admin(self):
        self.window.destroy()
        root = Tk()
        obj = Management_Admin(root)
        root.mainloop()
    def reset_fields(self):
        self.username_entry.delete(0,END)
        self.password_entry.delete(0,END)
# The main function
if __name__ == "__main__":
    root = Tk()
    obj = login_page(root)
    root.mainloop()
