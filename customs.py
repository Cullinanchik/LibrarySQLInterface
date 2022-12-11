color_1 = "deep sky blue"
color_2 = "gray95"
color_3 = "black"
color_4 = "white"
color_5 = "red"
color_6 = "green3"
color_7 = "yellow"
font_1 = "times new roman bold"
font_2 = "helvetica bold"

books = ('id', 'author', 'publication_year', 'publisher', 'name', 'isbn')

booking_cards = ('id', 'time', 'period', 'readers_id', 'librarians_id', 'books_id')

book_places = ('quantity', 'shell_number', 'books_id', 'rooms_id')

librarians = ('id', 'login', 'password')

readers = ('id', 'name', 'password', 'passport', 'address', 'phone')

rooms = ('id', 'name')

librarian_rooms = ('rooms_id', 'librarians_id')

issue_cards = ('id', 'time', 'period', 'readers_id', 'books_id')

administrators = ('id', 'login', 'password', 'booking_cards_id')