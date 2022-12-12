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

        self.add_book = Button(self.frame_2, text='Добавить книгу', font=(cs.font_1, 16), bd=2, command=self.AddNewBook,
                           cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=20, width=400, height=40)

        self.add_librarian_rooms = Button(self.frame_2, text='Добавить работника читального зала', font=(cs.font_1, 16), bd=2, command=self.AddNewLibrarianRooms,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=70, width=400, height=40)

        self.add_rooms = Button(self.frame_2, text='Добавить читальный зал', font=(cs.font_1, 16), bd=2,
                                          command=self.AddNewRoom,
                                          cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=120, width=400, height=40)
        self.add_librarian = Button(self.frame_2, text='Добавить библиотекаря', font=(cs.font_1, 16), bd=2,
                                command=self.AddNewLibrarian,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=170, width=400, height=40)

        self.add_administrators = Button(self.frame_2, text='Добавить администратора', font=(cs.font_1, 16), bd=2,
                                    command=self.AddNewAdministrator,
                                    cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=220, width=400, height=40)

        self.add_booking_cards = Button(self.frame_2, text='Добавить карточку выдачи книг', font=(cs.font_1, 16), bd=2,
                                         command=self.AddNewBookingCard,
                                         cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=270, width=400, height=40)
        self.add_issue_card = Button(self.frame_2, text='Добавить карточку бронирования', font=(cs.font_1, 16), bd=2,
                                        command=self.AddNewIssueCard,
                                        cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=320, width=400, height=40)
        self.add_book_place = Button(self.frame_2, text='Добавить место хранения книг', font=(cs.font_1, 16), bd=2,
                                     command=self.AddNewBookPlace,
                                     cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=370, width=400, height=40)

    def AddNewBook(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_entry.place(x=220, y=60, width=300)

        author = Label(self.frame_1, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.place(x=220, y=200, width=300)

        publication_year = Label(self.frame_1, text="Publication_year", font=(cs.font_2, 15, "bold"),
                                 bg=cs.color_1).place(x=220, y=310)
        self.publication_year_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publication_year_entry.place(x=220, y=340, width=300)

        publisher = Label(self.frame_1, text="Publisher", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=240)
        self.publisher_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publisher_entry.place(x=220, y=270, width=300)

        name = Label(self.frame_1, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                        y=100)
        self.bookname_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.bookname_entry.place(x=220, y=130, width=300)

        isbn = Label(self.frame_1, text="ISBN", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
        self.isbn_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.isbn_entry.place(x=220, y=410, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SubmitBook,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SubmitBook(self):
        if self.id_entry.get() == "" or self.bookname_entry.get() == "" or self.author_entry.get() == "" or self.publication_year_entry.get() == "" or self.publisher_entry.get() == "" or self.isbn_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from books where id=%s", self.id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into books (id,author,publication_year,publisher,name,isbn) values(%s,%s,%s,%s,%s,%s)",
                        (
                            self.id_entry.get(),
                            self.author_entry.get(),
                            self.publication_year_entry.get(),
                            self.publisher_entry.get(),
                            self.bookname_entry.get(),
                            self.isbn_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)


    def AddNewRoom(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="RoomID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.room_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.room_id_entry.place(x=220, y=60, width=300)

        name = Label(self.frame_1, text="Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.roomname_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.roomname_entry.place(x=220, y=200, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SubmitRoom,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SubmitRoom(self):
        if self.room_id_entry.get() == "" or self.roomname_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from rooms where id=%s", self.room_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into rooms (id,name) values(%s,%s)",
                        (
                            self.room_id_entry.get(),
                            self.roomname_entry.get(),
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewLibrarian(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.lib_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.lib_id_entry.place(x=220, y=60, width=300)

        login = Label(self.frame_1, text="Login", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.login_lib_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.login_lib_entry.place(x=220, y=200, width=300)

        password = Label(self.frame_1, text="Password", font=(cs.font_2, 15, "bold"),
                                 bg=cs.color_1).place(x=220, y=310)
        self.password_lib_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.password_lib_entry.place(x=220, y=340, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SubmitLibrarian,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SubmitLibrarian(self):
        if self.lib_id_entry.get() == "" or self.login_lib_entry.get() == "" or self.password_lib_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from librarians where id=%s", self.lib_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into librarians (id,login,password) values(%s,%s,%s)",
                        (
                            self.lib_id_entry.get(),
                            self.login_lib_entry.get(),
                            self.password_lib_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewAdministrator(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.adm_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.adm_id_entry.place(x=220, y=60, width=300)

        booking_cards_id = Label(self.frame_1, text="Booking_card_ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=100)
        self.booking_cards_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.booking_cards_id_entry.place(x=220, y=130, width=300)

        login = Label(self.frame_1, text="Login", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.adm_login_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.adm_login_entry.place(x=220, y=200, width=300)

        password = Label(self.frame_1, text="Password", font=(cs.font_2, 15, "bold"),
                                 bg=cs.color_1).place(x=220, y=310)
        self.password_adm_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.password_adm_entry.place(x=220, y=340, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SubmitAdministrator,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SubmitAdministrator(self):
        if self.adm_id_entry.get() == "" or self.booking_cards_id_entry.get() == "" or self.adm_login_entry.get() == "" or self.password_adm_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from administrators where id=%s", self.adm_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into administrators (id,booking_cards_id,login,password) values(%s,%s,%s,%s)",
                        (
                            self.adm_id_entry.get(),
                            self.booking_cards_id_entry.get(),
                            self.adm_login_entry.get(),
                            self.password_adm_entry.get(),
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewBookPlace(self):
        self.ClearScreen()

        quantity = Label(self.frame_1, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.quantity_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.quantity_entry.place(x=220, y=60, width=300)

        shell_number = Label(self.frame_1, text="Shell Number", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.shell_number_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.shell_number_entry.place(x=220, y=200, width=300)

        books_id_place = Label(self.frame_1, text="Books ID", font=(cs.font_2, 15, "bold"),
                                 bg=cs.color_1).place(x=220, y=310)
        self.books_id_place_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_place_entry.place(x=220, y=340, width=300)

        rooms_id = Label(self.frame_1, text="Rooms ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=240)
        self.rooms_id_place_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.rooms_id_place_entry.place(x=220, y=270, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SumbitBookPlace,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SumbitBookPlace(self):
        if self.quantity_entry.get() == "" or self.shell_number_entry.get() == "" or self.books_id_place_entry.get() == "" or self.rooms_id_place_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from book_places where books_id=%s", self.books_id_place_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into book_places (quantity,shell_number,books_id,rooms_id) values(%s,%s,%s,%s)",
                        (
                            self.quantity_entry.get(),
                            self.shell_number_entry.get(),
                            self.books_id_place_entry.get(),
                            self.rooms_id_place_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewBookingCard(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.booking_card_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.booking_card_id_entry.place(x=220, y=60, width=300)

        time = Label(self.frame_1, text="Time", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.time_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.time_book_entry.place(x=220, y=200, width=300)

        period = Label(self.frame_1, text="Period", font=(cs.font_2, 15, "bold"),
                                 bg=cs.color_1).place(x=220, y=310)
        self.period_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.period_book_entry.place(x=220, y=340, width=300)

        readers_id = Label(self.frame_1, text="Readers ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=240)
        self.readers_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.readers_id_book_entry.place(x=220, y=270, width=300)

        librarians_id = Label(self.frame_1, text="Librararians_ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                        y=100)
        self.librarians_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.librarians_id_book_entry.place(x=220, y=130, width=300)

        books_id = Label(self.frame_1, text="Books ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
        self.books_id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_book_entry.place(x=220, y=410, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SumbitBookingCard,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SumbitBookingCard(self):
        if self.booking_card_id_entry.get() == "" or self.time_book_entry.get() == "" or self.period_book_entry.get() == "" or self.librarians_id_book_entry.get() == "" or self.books_id_book_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from booking_cards where id=%s", self.booking_card_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into booking_cards (id,time,period,readers_id,librarians_id,books_id) values(%s,%s,%s,%s,%s,%s)",
                        (
                            self.booking_card_id_entry.get(),
                            self.time_book_entry.get(),
                            self.period_book_entry.get(),
                            self.readers_id_book_entry.get(),
                            self.librarians_id_book_entry.get(),
                            self.books_id_book_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewIssueCard(self):
        self.ClearScreen()

        id = Label(self.frame_1, text="ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.issue_card_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.issue_card_id_entry.place(x=220, y=60, width=300)

        time = Label(self.frame_1, text="Time", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.time_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.time_issue_entry.place(x=220, y=200, width=300)

        period = Label(self.frame_1, text="Period", font=(cs.font_2, 15, "bold"),
                       bg=cs.color_1).place(x=220, y=100)
        self.period_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.period_issue_entry.place(x=220, y=130, width=300)

        readers_id = Label(self.frame_1, text="Readers ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                               y=240)
        self.readers_id_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.readers_id_issue_entry.place(x=220, y=270, width=300)

        books_id = Label(self.frame_1, text="Books ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
        self.books_id_issue_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.books_id_issue_entry.place(x=220, y=340, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=self.SumbitIssueCard,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SumbitIssueCard(self):
        if self.issue_card_id_entry.get() == "" or self.time_issue_entry.get() == "" or self.period_issue_entry.get() == "" or self.readers_id_issue_entry.get() == "" or self.books_id_issue_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from issue_cards where id=%s", self.issue_card_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into issue_cards (id,time,period,readers_id,books_id) values(%s,%s,%s,%s,%s)",
                        (
                            self.issue_card_id_entry.get(),
                            self.time_issue_entry.get(),
                            self.period_issue_entry.get(),
                            self.readers_id_issue_entry.get(),
                            self.books_id_issue_entry.get()
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def AddNewLibrarianRooms(self):
        self.ClearScreen()

        rooms_id = Label(self.frame_1, text="Rooms ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=30)
        self.rooms_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.rooms_id_entry.place(x=220, y=60, width=300)

        librarians_id = Label(self.frame_1, text="Librarians ID", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.librarians_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.librarians_id_entry.place(x=220, y=200, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2, command=self.SumbitLibrarianRooms,
                                  cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=459, width=100)

    def SumbitLibrarianRooms(self):
        if self.rooms_id_entry.get() == "" or self.librarians_id_entry.get() == "":
            messagebox.showerror("Error!", "Sorry!, All fields are required", parent=self.window)
        else:
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                curs.execute("select * from librarian_rooms where rooms_id=%s", self.rooms_id_entry.get())
                row = curs.fetchone()

                if row != None:
                    messagebox.showerror("Error!", "This book id is already exists, please try again with another one",
                                         parent=self.window)
                else:
                    curs.execute(
                        "insert into librarian_rooms (rooms_id, librarians_id) values(%s,%s)",
                        (
                            self.rooms_id_entry.get(),
                            self.librarians_id_entry.get(),
                        ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo('Test!')
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)


    # Removes all widgets from the frame 1 and frame 3
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

        for widget in self.frame_3.winfo_children():
            widget.destroy()

    def reset_fields_books(self):
        self.bookname_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.publication_year_entry.delete(0, END)
        self.publisher_entry.delete(0, END)
        self.isbn_entry.delete(0, END)

    def reset_fields_admins(self):
        self.adm_id_entry.delete(0, END)
        self.booking_cards_id_entry.delete(0, END)
        self.adm_login_entry.delete(0, END)
        self.password_adm_entry.delete(0, END)

    def reset_fields_rooms(self):
        self.room_id_entry.delete(0, END)
        self.roomname_entry.delete(0, END)

    def reset_fields_librarians(self):
        self.lib_id_entry.delete(0, END)
        self.login_lib_entry.delete(0, END)
        self.password_lib_entry.delete(0, END)

    def reset_fields_book_place(self):
        self.quantity_entry.delete(0, END)
        self.shell_number_entry.delete(0, END)
        self.books_id_place_entry.delete(0, END)
        self.rooms_id_place_entry.delete(0, END)

    def reset_fields_booking_card(self):
        self.booking_card_id_entry.delete(0, END)
        self.time_book_entry.delete(0, END)
        self.period_book_entry.delete(0, END)
        self.readers_id_book_entry.delete(0, END)
        self.librarians_id_book_entry.delete(0, END)
        self.books_id_book_entry.delete(0, END)

    def reset_fields_issue_card(self):
        self.issue_card_id_entry.delete(0, END)
        self.time_issue_entry.delete(0, END)
        self.period_issue_entry.delete(0, END)
        self.readers_id_issue_entry.delete(0, END)
        self.books_id_issue_entry.delete(0, END)

    def reset_fields_librarian_room(self):
        self.rooms_id_entry.delete(0, END)
        self.librarians_id_entry.delete(0, END)

    '''Exit window'''

    def Exit(self):
        self.window.destroy()


# The main function
if __name__ == "__main__":
    root = Tk()
    obj = Add(root)
    root.mainloop()