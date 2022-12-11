from tkinter import *
from tkinter import ttk, messagebox
import customs as cs
from functools import partial
import pymysql
import credentials as cr


class Select:
    def __init__(self, root):
        self.window = root
        self.window.title("Library Management System")
        self.window.geometry("1070x720")
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


        self.all_book = Button(self.frame_2, text='Показать книги', font=(cs.font_1, 16), bd=2, command=self.ShowBooks,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=20, width=400, height=70)
        self.all_book = Button(self.frame_2, text='Показать Читальные залы', font=(cs.font_1, 16), bd=2, command=self.ShowRooms,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=110, width=400, height=70)
        self.all_book = Button(self.frame_2, text='Показать библиотекарей', font=(cs.font_1, 16), bd=2,
                       command=self.ShowLibrarians,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=200, width=400, height=70)
        self.all_book = Button(self.frame_2, text='Показать карточки бронирования', font=(cs.font_1, 16), bd=2,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=290, width=400, height=70)
        self.all_book = Button(self.frame_2, text='Показать место хранения книг', font=(cs.font_1, 16), bd=2,
                       command=self.ShowBookPlaces,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=380, width=400, height=70)
        self.all_book = Button(self.frame_2, text='Показать читателей', font=(cs.font_1, 16), bd=2,
                       command=self.ShowReaders,
                       cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=470, width=400, height=70)

        self.clear = Button(self.frame_2, text='Очистить экран', font=(cs.font_1, 16), bd=2, command=self.ClearScreen,
                            cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=10, y=560, width=400, height=70)
        self.exit = Button(self.frame_2, text='Выйти', font=(cs.font_1, 16), bd=2, command=self.Exit, cursor="hand2",
                           bg=cs.color_2, fg=cs.color_3).place(x=10, y=645, width=400, height=70)
    def OnSelectedforShowBooks(self, a):
        self.dlt_record = Button(self.frame_3, text='Delete', font=(cs.font_1, 12), bd=2, command=self.DeleteBook,
                                 cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(x=50, y=100, width=100)
        self.update_record = Button(self.frame_3, text='Update', font=(cs.font_1, 12), bd=2,
                                    command=self.UpdateBookDetails, cursor="hand2", bg=cs.color_2, fg=cs.color_3).place(
            x=180, y=100, width=100)

    def DeleteBook(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']
        try:
            status = messagebox.askokcancel('Delete Book', 'Are you want to proceed?')

            if status == True:
                connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
                curs = connection.cursor()

                curs.execute("select * from books where id=%s", row[0])
                var = curs.fetchall()

                curs.execute("delete from books where id=%s", (row[0]))
                messagebox.showinfo("Success!", "The book record has been deleted")
                connection.commit()
                connection.close()
                self.ClearScreen()
                self.ShowBooks()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

            # Function 5: It gets call from 'Function 1', is used to return a book from the borrower

    # Function 12: It is used get the book name for searching and calls 'Function 17'
    # when the search button is pressed
    def UpdateBookDetails(self):
        x = self.tree.selection()
        row = self.tree.item(x)['values']

        self.ClearScreen()

        book_id = Label(self.frame_1, text="Book Id", font=(cs.font_2, 18, "bold"), bg=cs.color_1).place(x=220, y=30)
        id = Label(self.frame_1, text=row[0], font=(cs.font_1, 10))
        id.place(x=220, y=60, width=300)

        book_name = Label(self.frame_1, text="Book Name", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220,
                                                                                                             y=100)
        self.bookname_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.bookname_entry.insert(0, row[1])
        self.bookname_entry.place(x=220, y=130, width=300)

        author = Label(self.frame_1, text="Author", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=170)
        self.author_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.author_entry.insert(0, row[2])
        self.author_entry.place(x=220, y=200, width=300)

        edition = Label(self.frame_1, text="Edition", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=240)
        self.edition_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.edition_entry.insert(0, row[3])
        self.edition_entry.place(x=220, y=270, width=300)

        price = Label(self.frame_1, text="Price", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=310)
        self.price_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.price_entry.insert(0, row[4])
        self.price_entry.place(x=220, y=340, width=300)

        quantity = Label(self.frame_1, text="Quantity", font=(cs.font_2, 15, "bold"), bg=cs.color_1).place(x=220, y=380)
        self.qty_entry = Entry(self.frame_1, bg=cs.color_4, fg=cs.color_3)
        self.qty_entry.insert(0, row[5])
        self.qty_entry.place(x=220, y=410, width=300)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(cs.font_1, 12), bd=2,
                                  command=partial(self.SubmitforUpdateBook, row), cursor="hand2", bg=cs.color_2,
                                  fg=cs.color_3).place(x=310, y=459, width=100)

    # Function 10: It gets call from 'Function 9' when the submit button is pressed.
    # It updates a entry in the 'book_list' table
    def SubmitforUpdateBook(self, row):
        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("update book_list set book_name=%s,author=%s,edition=%s,price=%s,qty=%s where book_id=%s",
                         (
                             self.bookname_entry.get(),
                             self.author_entry.get(),
                             self.edition_entry.get(),
                             self.price_entry.get(),
                             self.qty_entry.get(),
                             row[0]
                         ))
            messagebox.showinfo("Success!", "The data has been updated")
            connection.commit()
            connection.close()
            self.ClearScreen()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)



    def ShowBooks(self):
        self.ClearScreen()
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
        self.tree.heading('author', text='Author', anchor=W)
        self.tree.heading('publication_year', text='Publication year', anchor=W)
        self.tree.heading('publisher', text='Publisher', anchor=W)
        self.tree.heading('name', text='Book Name', anchor=W)
        self.tree.heading('isbn', text='ISBN', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from books")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def ShowRooms(self):
        self.ClearScreen()
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
        self.tree.heading('name', text='Room Name', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from rooms")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1]))

    def ShowLibrarians(self):
        self.ClearScreen()
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
        self.tree.heading('login', text='Login', anchor=W)
        self.tree.heading('password', text='Password', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from librarians")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", (rows.index(list)),
                             values=(list[0], list[1], list[2]))

    def ShowBookPlaces(self):
        self.ClearScreen()
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
        self.tree.heading('shell_number', text='Shell Number', anchor=W)
        self.tree.heading('books_id', text='Book ID', anchor=W)
        self.tree.heading('rooms_id', text='Room ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from book_places")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3]))

    def LibrarianRooms(self):
        self.ClearScreen()
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
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from librarian_rooms")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1]))

    def ShowReaders(self):
        self.ClearScreen()
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
        self.tree.heading('name', text='Reader Name', anchor=W)
        self.tree.heading('password', text='Password', anchor=W)
        self.tree.heading('passport', text='Passport', anchor=W)
        self.tree.heading('address', text='Address', anchor=W)
        self.tree.heading('phone', text='Phone', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from readers")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))

    def ShowIssueCards(self):
        self.ClearScreen()
        # Defining two scrollbars
        scroll_x = ttk.Scrollbar(self.frame_1, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.frame_1, orient=VERTICAL)
        self.tree = ttk.Treeview(self.frame_1, columns=cs.columns, height=400, selectmode="extended",
                                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        # vertical scrollbar: left side
        scroll_y.pack(side=LEFT, fill=Y)
        scroll_x.config(command=self.tree.xview)
        # Horizontal scrollbar: at bottom
        scroll_x.pack(side=BOTTOM, fill=X)

        # Table headings
        self.tree.heading('time', text='Time', anchor=W)
        self.tree.heading('period', text='Period', anchor=W)
        self.tree.heading('readers_id', text='Reader ID', anchor=W)
        self.tree.heading('books_id', text='Book ID', anchor=W)
        self.tree.pack()
        # Double click on a row
        self.tree.bind('<Double-Button-1>', self.OnSelectedforShowBooks)

        try:
            connection = pymysql.connect(host=cr.host, user=cr.user, password=cr.password, database=cr.database)
            curs = connection.cursor()
            curs.execute("select * from issue_cards")
            rows = curs.fetchall()

            if rows == None:
                messagebox.showinfo("Database Empty", "There is no data to show", parent=self.window)
                connection.close()
                self.ClearScreen()
            else:
                connection.close()
        except Exception as e:
            messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

        for list in rows:
            self.tree.insert("", 'end', text=(rows.index(list) + 1),
                             values=(list[0], list[1], list[2], list[3], list[4], list[5]))


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
    obj = Select(root)
    root.mainloop()