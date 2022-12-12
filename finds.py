from tkinter import *
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import credentials as cr


class Find:
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

        self.search_book = Button(self.frame_2, text='Найти книгу', font=(cs.font_1, 16), bd=2,
                                  command=self.GetBookNametoSearch, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=10, y=20, width=400, height=40)
        self.search_reader = Button(self.frame_2, text='Найти читателя', font=(cs.font_1, 16), bd=2, command=self.GetReaderNametoSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=70, width=400, height=40)
        self.search_librarian = Button(self.frame_2, text='Найти библиотекаря', font=(cs.font_1, 16), bd=2,
                               command=self.GetLibrariantoSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=120, width=400, height=40)
        self.search_room = Button(self.frame_2, text='Найти читальный зал', font=(cs.font_1, 16), bd=2,
                               command=self.GetRoomtoSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=170, width=400, height=40)
        self.search_bookigng_card = Button(self.frame_2, text='Найти карточку выдачи книг', font=(cs.font_1, 16),
                                           bd=2,  command=self.GetBookingCardSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=220, width=400, height=40)
        self.search_issue_card = Button(self.frame_2, text='Найти карточку бронирования', font=(cs.font_1, 16), bd=2,
                               command=self.GetIssueCardSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=270, width=400, height=40)
        self.search_book_places = Button(self.frame_2, text='Найти место хранения книг', font=(cs.font_1, 16), bd=2,
                               command=self.GetBookPlacestoSearch,
                               cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=320, width=400, height=40)

        self.search_librarian_rooms = Button(self.frame_2, text='Найти работников читального зала', font=(cs.font_1, 16), bd=2,
                                         command=self.GetLibrarianRoomstoSearch,
                                         cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=370, width=400, height=40)
        self.search_administrator = Button(self.frame_2, text='Найти администратора',
                                             font=(cs.font_1, 16), bd=2,
                                             command=self.GetAdminToSearch,
                                             cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=420, width=400, height=45)

        self.clear = Button(self.frame_2, text='Очистить экран', font=(cs.font_1, 16), bd=2, command=self.ClearScreen,
                            cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=210, y=480, width=200, height=40)
        self.exit = Button(self.frame_2, text='Выйти', font=(cs.font_1, 16), bd=2, command=self.Exit, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=480, width=200, height=40)

    def GetBookNametoSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Найти книгу", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        book = Label(self.frame_1, text="Введите название книги", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.book_name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.book_name_entry.place(x=220, y=165, width=300)

        author = Label(self.frame_1, text="Введите название автора", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=210)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.place(x=220, y=235, width=300)

        isbn = Label(self.frame_1, text="Введите номер книги", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=280)
        self.isbn_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.isbn_entry.place(x=220, y=305, width=300)

        publication_year = Label(self.frame_1, text="Введите год публикации", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=340)
        self.publication_year_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publication_year_entry.place(x=220, y=370, width=300)

        publisher = Label(self.frame_1, text="Введите издательство", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=400)
        self.publihser_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.publihser_entry.place(x=220, y=420, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchBook,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchBook(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.book_name_entry.get() != "":
                    curs.execute("select * from books where name like %s", ("%" + self.book_name_entry.get()))
                    rows = curs.fetchall()
                if self.author_entry.get() != "":
                    curs.execute("select * from books where author like %s", ("%" + self.author_entry.get()))
                    rows = curs.fetchall()
                if self.isbn_entry.get() != "":
                    curs.execute("select * from books where isbn like %s", ("%" + self.isbn_entry.get()))
                    rows = curs.fetchall()
                if self.publication_year_entry.get() != "":
                    curs.execute("select * from books where publication_year like %s", ("%" + self.publication_year_entry.get()))
                    rows = curs.fetchall()
                if self.publihser_entry.get() != "":
                    curs.execute("select * from books where publisher like %s", ("%" + self.publihser_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.books, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='Book ID', anchor=W)
            self.tree.heading('author', text='Author', anchor=W)
            self.tree.heading('publication_year', text='Publication year', anchor=W)
            self.tree.heading('publisher', text='Publisher', anchor=W)
            self.tree.heading('name', text='name', anchor=W)
            self.tree.heading('isbn', text='isbn', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3], list[4], list[5]))


    def GetAdminToSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Найти администратора", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        adm_id = Label(self.frame_1, text="Введите ID администратора", font=(cs.font_2, 15, "bold"),
                          bg=cs.color_1).place(
            x=220, y=140)
        self.adm_id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.adm_id_entry.place(x=220, y=165, width=300)

        adm_login = Label(self.frame_1, text="Введите логин администратора", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=230)
        self.adm_login_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.adm_login_entry.place(x=220, y=250, width=300)

        booking_card_id_adm = Label(self.frame_1, text="Введите ID карточки выдачи книг", font=(cs.font_2, 15, "bold"),
                          bg=cs.color_1).place(
            x=220, y=320)
        self.booking_card_id_adm_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.booking_card_id_adm_entry.place(x=220, y=340, width=300)


        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchAdmin,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=400, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchAdmin(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.adm_id_entry.get() != "":
                    curs.execute("select * from administrators where id like %s", ("%" + self.adm_id_entry.get()))
                    rows = curs.fetchall()
                if self.adm_login_entry.get() != "":
                    curs.execute("select * from administrators where login like %s", ("%" + self.adm_login_entry.get()))
                    rows = curs.fetchall()
                if self.booking_card_id_adm_entry.get() != "":
                    curs.execute("select * from administrators where booking_cards_id like %s", ("%" + self.booking_card_id_adm_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.administrators, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='Admin ID', anchor=W)
            self.tree.heading('booking_cards_id', text='booking_cards_id', anchor=W)
            self.tree.heading('login', text='login', anchor=W)
            self.tree.heading('password', text='password', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3]))

    def GetReaderNametoSearch(self):
        self.ClearScreen()
        reader_name = Label(self.frame_1, text="Найти книгу", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        reader_name = Label(self.frame_1, text="Введите имя читателя", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.reader_name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.reader_name_entry.place(x=220, y=165, width=300)

        passport = Label(self.frame_1, text="Введите паспорт читателя", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=210)
        self.passport_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.passport_entry.place(x=220, y=235, width=300)

        address = Label(self.frame_1, text="Введите адрес", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=280)
        self.address_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.address_entry.place(x=220, y=305, width=300)

        phone = Label(self.frame_1, text="Введите мобилу", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=340)
        self.phone_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.phone_entry.place(x=220, y=370, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchReader,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchReader(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.reader_name_entry.get() != "":
                    curs.execute("select * from readers where name like %s", ("%" + self.reader_name_entry.get()))
                    rows = curs.fetchall()
                if self.passport_entry.get() != "":
                    curs.execute("select * from readers where passport like %s", ("%" + self.passport_entry.get()))
                    rows = curs.fetchall()
                if self.address_entry.get() != "":
                    curs.execute("select * from readers where address like %s", ("%" + self.address_entry.get()))
                    rows = curs.fetchall()
                if self.phone_entry.get() != "":
                    curs.execute("select * from readers where phone like %s", ("%" + self.phone_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.readers, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='Reader ID', anchor=W)
            self.tree.heading('name', text='name', anchor=W)
            self.tree.heading('password', text='password', anchor=W)
            self.tree.heading('passport', text='passport', anchor=W)
            self.tree.heading('address', text='address', anchor=W)
            self.tree.heading('phone', text='phone', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3], list[4], list[5]))


    def GetRoomtoSearch(self):
        self.ClearScreen()
        search_room = Label(self.frame_1, text="Найти комнату", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        room = Label(self.frame_1, text="Введите название комнаты", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.room_name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.room_name_entry.place(x=220, y=165, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchRoom,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchRoom(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.room_name_entry.get() != "":
                    curs.execute("select * from rooms where name like %s", ("%" + self.room_name_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.rooms, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='Room ID', anchor=W)
            self.tree.heading('name', text='Name', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1]))

    def GetBookingCardSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Найти карточку выдачи книг", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        id = Label(self.frame_1, text="Введите id карточки", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_entry.place(x=220, y=165, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchBookingCard,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchBookingCard(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.id_entry.get() != "":
                    curs.execute("select * from booking_cards where id like %s", ("%" + self.id_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.booking_cards, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='Booking_card ID', anchor=W)
            self.tree.heading('time', text='Time', anchor=W)
            self.tree.heading('period', text='Period', anchor=W)
            self.tree.heading('readers_id', text='Readers_id', anchor=W)
            self.tree.heading('librarians_id', text='Librarians_id', anchor=W)
            self.tree.heading('books_id', text='Books_id', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def GetIssueCardSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Найти карточку бронирования", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        id = Label(self.frame_1, text="Введите id карточки", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.id_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_entry.place(x=220, y=165, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchIssueCard,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchIssueCard(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.id_entry.get() != "":
                    curs.execute("select * from issue_cards where id like %s", ("%" + self.id_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.issue_cards, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='IssueCard ID', anchor=W)
            self.tree.heading('time', text='Time', anchor=W)
            self.tree.heading('period', text='Period', anchor=W)
            self.tree.heading('readers_id', text='Readers_id', anchor=W)
            self.tree.heading('books_id', text='Books_id', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3], list[4]))

    def GetBookPlacestoSearch(self):
        self.ClearScreen()
        search_book_place = Label(self.frame_1, text="Найти книгу на полке", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        shell_number = Label(self.frame_1, text="Введите номер полки", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.shell_number_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.shell_number_entry.place(x=220, y=165, width=300)

        id_book = Label(self.frame_1, text="Введите id книги", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=210)
        self.id_book_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_book_entry.place(x=220, y=235, width=300)

        id_room = Label(self.frame_1, text="Введите id читального зала", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=280)
        self.id_room_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_room_entry.place(x=220, y=305, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchBookPlace,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchBookPlace(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.shell_number_entry.get() != "":
                    curs.execute("select * from book_places where shell_number like %s", ("%" + self.shell_number_entry.get()))
                    rows = curs.fetchall()
                if self.id_book_entry.get() != "":
                    curs.execute("select * from book_places where books_id like %s", ("%" + self.id_book_entry.get()))
                    rows = curs.fetchall()
                if self.id_room_entry.get() != "":
                    curs.execute("select * from book_places where rooms_id like %s", ("%" + self.id_room_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.book_places, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('quantity', text='Quantity', anchor=W)
            self.tree.heading('shell_number', text='ShellNumber', anchor=W)
            self.tree.heading('books_id', text='BookID year', anchor=W)
            self.tree.heading('rooms_id', text='RoomID', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2], list[3]))

    def GetLibrarianRoomstoSearch(self):
        self.ClearScreen()
        search_book = Label(self.frame_1, text="Найти работника читального зала", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        id_rooms = Label(self.frame_1, text="Введите название комнаты", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.id_rooms_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_rooms_entry.place(x=220, y=165, width=300)

        id_librarian = Label(self.frame_1, text="Введите название библиотекаря", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=210)
        self.id_librarian_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.id_librarian_entry.place(x=220, y=235, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchLibrarianRoom,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchLibrarianRoom(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.id_rooms_entry.get() != "":
                    curs.execute("select * from librarian_rooms where rooms_id like %s", ("%" + self.id_rooms_entry.get()))
                    rows = curs.fetchall()
                if self.id_librarian_entry.get() != "":
                    curs.execute("select * from librarian_rooms where librarians_id like %s", ("%" + self.id_librarian_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.librarian_rooms, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('rooms_id', text='Room ID', anchor=W)
            self.tree.heading('librarians_id', text='Librarian ID', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1]))


    def GetLibrariantoSearch(self):
        self.ClearScreen()
        search_librarian = Label(self.frame_1, text="Найти библиотекаря", font=(cs.font_1, 30, "bold"), bg=cs.color_1).place(x=280, y=50)

        librarian = Label(self.frame_1, text="Введите логин библиотекаря", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(
            x=220, y=140)
        self.librarian_name_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.librarian_name_entry.place(x=220, y=165, width=300)

        self.search_bt = Button(self.frame_1, text='Поиск', font=(cs.font_1, 12), bd=2, command=self.SearchLibrarian,
                                cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=310, y=480, width=100)

    # Function 17: It gets call from 'Function 12' and search a book by the name
    def SearchLibrarian(self):
            try:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()
                if self.librarian_name_entry.get() != "":
                    curs.execute("select * from librarians where login like %s", ("%" + self.librarian_name_entry.get()))
                    rows = curs.fetchall()
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Defining two scrollbars
            scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
            self.tree = ttk.Treeview(self.frame_1, columns=cs.librarians, height=400, selectmode="extended",
                                     yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
            scroll_y.config(command=self.tree.yview)
            # vertical scrollbar: left side
            scroll_y.pack(side=LEFT, fill=Y)
            scroll_x.config(command=self.tree.xview)
            # Horizontal scrollbar: at bottom
            scroll_x.pack(side=BOTTOM, fill=X)

            # Table headings
            self.tree.heading('id', text='ID', anchor=W)
            self.tree.heading('login', text='Login', anchor=W)
            self.tree.heading('password', text='Password', anchor=W)
            self.tree.pack()

            for list in rows:
                self.tree.insert("", 'end', text=(rows.index(list) + 1),
                                 values=(list[0], list[1], list[2]))


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
    obj = Find(root)
    root.mainloop()