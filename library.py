"""
This program will simulate a library. There are 6 important functions:
- add_new_book: this function allows the user to add a book, and will prompt the user for important values such as title, author, edition, ISBN, etc.
- borrow_books: this function allows the user to borrow an available book in the library. Any books borrowed will not be available to be borrowed until returned
- list_all_books: when selected, this prints the list of books in the library. It will print information about the book such as title, author, and availability
- return_a_book: this function allows the user to return a book that has been borrowed
- exit_program: this function, when selected, will exit the program and print the final list of books in the library including availability
- print_menu: this function will print all options the user can select
"""


# this function will print the menu
def print_menu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')


# this function allows the user to add a book
def add_new_book(all_books):
    book_name = input('Book name> ')  # prompt the user for the name of the book

    # prevent the user from inputting a title with '*' or '%'
    while '*' in book_name or '%' in book_name:
        print('Invalid book name!')
        book_name = input('Book name> ')

    author_name = input('Author name> ')  # prompt the user for author name

    edition = '.'  # this will be used to save the user's input of edition. This variable starts with a period to enable the while loop

    # while edition is not an integer, continue to prompt the user
    while not edition.isdigit():
        edition = input('Edition> ')
        if not edition.isdigit():
            print('Invalid edition number!')

    isbn = '.'  # This will be used to store the user's isbn input. This variable starts with a period to enable the while loop

    # while isbn is not an integer or not 13 digits long, prompt the user
    while not isbn.isdigit() or len(isbn) != 13:
        isbn = input('ISBN> ')
        if not isbn.isdigit() or len(isbn) != 13:
            print('Invalid ISBN!')

    isbn_sum = 0  # this variable will hold the isbn sum

    # add all the digits in isbn according to the weight factor to check if the isbn is valid
    for i in range(0, 13):
        # all the evenly indexed (1, 3, 5...) are added to the sum
        if i in {0, 2, 4, 6, 8, 10, 12}:
            isbn_sum += int(isbn[i])
        # all the rest (2, 4, 6...) are multiplied by 3 and then added to the sum
        else:
            isbn_sum += int(isbn[i]) * 3

    # if the isbn sum is divisible by 10, check if this isbn is a duplicate (matches any other isbn in the library)
    if isbn_sum % 10 == 0:
        isbn_duplicate = False  # set a boolean variable to track if the isbn is a duplicate

        for book in all_books:
            # if this isbn matches the isbn of the current looped book, set isbn_duplicate to True
            if isbn == all_books[book]['isbn']:
                isbn_duplicate = True

        if isbn_duplicate:  # if the isbn is repeated, print an error message
            print('Duplicate ISBN is found! Cannot add the book.')
        else:  # if this isbn is not repeated, add the book into the library
            new_book_dict = {
                'name': book_name,
                'author': author_name,
                'edition': edition,
                'isbn': isbn,
                'past_borrowers': []
            }
            all_books[book_name] = new_book_dict
            print('A new book is added successfully.')

    # if the isbn sum with the weight favtor is not divisible by 10 (not a valid isbn), print an error message
    else:
        print('Invalid ISBN!')


# this function allows the user to borrow a book
# search terms:
# a search term ending with a '*' means that the term can be found anywhere in the book name
# a search term ending with a '%' means that the term can only be found in the beginning of the book name
# any other search term will look for books with names exactly matching the search term
def borrow_books(all_books, rented_isbns):
    borrower_name = input('Enter the borrower name> ')  # ask user for their name
    search_term = input('Search term> ')  # ask user for their search term

    # create variables to track if a book was found
    found = False

    # if the search term ends with *, check for the search term in all the book names
    if search_term[-1] == '*':
        for book in all_books:
            if search_term[:-1].lower() in book.lower():  # if the search term is in the book name
                if not all_books[book]['isbn'] in rented_isbns:
                    found = True
                    all_books[book]['past_borrowers'].append(borrower_name)  # add the borrowers name to the borrowers list
                    rented_isbns.append(all_books[book]['isbn'])  # add the isbn to the list of rented isbns
                    print('-"' + all_books[book]['name'] + '" is borrowed!')

    # if search term ends with %, check for the search term in the beginning of all the book names
    elif search_term[-1] == '%':
        for book in all_books:
            if search_term[:-1].lower() == book.lower()[:len(search_term[:-1])]:  # if the search_term in the beginning of the book
                if not all_books[book]['isbn'] in rented_isbns:
                    found = True
                    all_books[book]['past_borrowers'].append(borrower_name)  # add the borrowers name to the borrowers list
                    rented_isbns.append(all_books[book]['isbn'])  # add the isbn to the list of rented isbns
                    print('-"' + all_books[book]['name'] + '" is borrowed!')

    # if search term doesn't end with * or %, check if the search term is the same as the book name
    elif search_term[-1] != '%' and search_term[-1] != '*':
        for book in all_books:
            if search_term.lower() == book.lower():   # if the search_term is equal to the book name
                if not all_books[book]['isbn'] in rented_isbns:
                    found = True
                    all_books[book]['past_borrowers'].append(borrower_name)  # add the borrowers name to the borrowers list
                    rented_isbns.append(all_books[book]['isbn'])  # add the isbn to the list of rented isbns
                    print('-"' + all_books[book]['name'] + '" is borrowed!')

    # if no book was found or if the book(s) were unavailable, print No books found!
    if not found:
        print('No books found!')


# this function lists all the books, their availability and their information
def list_all_books(all_books, rented_isbns):
    for book in all_books:
        print('---------------')
        if all_books[book]['isbn'] in rented_isbns:  # if the book is rented, print Unavailable
            print('[Unavailable]')
        else:  # else, print Avaiable
            print('[Available]')
        print(all_books[book]['name'], '-', all_books[book]['author'])  # print the name and author
        print('E:', all_books[book]['edition'], 'ISBN:', all_books[book]['isbn'])  # print the edition and isbn
        print('borrowed by:', all_books[book]['past_borrowers'])  # print the list of past borrowers


# create a function that allows the user to return a book
def return_a_book(all_books, rented_isbns):
    borrowed_isbn = input('ISBN> ')  # ask the user for the isbn of the book they want to return
    found = False  # create a boolean to track if we found a matching isbn

    for isbn in rented_isbns:
        if borrowed_isbn == isbn:  # if the isbn matches the current isbn in rented_isbns, remove it from rented_isbns
            found = True
            rented_isbns.remove(isbn)

            for book in all_books:  # this segment finds the name of the book that the borrowed isbn belongs to
                if borrowed_isbn == all_books[book]['isbn']:
                    book_name = all_books[book]['name']
                    print('"' + book_name + '"', 'is returned.')

    # if there was no book found, print No book is found!
    if not found:
        print("No book is found!")


# this function prints out the exit message
def exit_program(all_books, rented_isbns):
    print('\n\n$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$')
    for book in all_books:
        print('---------------')
        if all_books[book]['isbn'] in rented_isbns:  # if the book is unavailable, print Unavailable
            print('[Unavailable]')
        else:  # else, print Avaiable
            print('[Available]')
        print(all_books[book]['name'], '-', all_books[book]['author'])  # print the book name and author
        print('E:', all_books[book]['edition'], 'ISBN:', all_books[book]['isbn'])  # print the edition and isbn
        print('borrowed by:', all_books[book]['past_borrowers'])  # print the list of past borrowers


# this function will start the program
def start():
    # add the starting set of books
    all_books = {
        'The Earth Inside Out': {
            'name': 'The Earth Inside Out',
            'author': 'Mike B',
            'edition': 2,
            'isbn': '9780596007126',
            'past_borrowers': ['Ali']
        },

        'The Human Body': {
            'name': 'The Human Body',
            'author': 'Dave R',
            'edition': 1,
            'isbn': '9780134494166',
            'past_borrowers': []
        },

        'Human on Earth': {
            'name': 'Human on Earth',
            'author': 'Jordan P',
            'edition': 1,
            'isbn': '9780321125217',
            'past_borrowers': ['David', 'b1', 'user123']
        }
    }

    rented_isbns = []  # all the isbns of rented books will be kept here
    running = True  # this variable will be used to keep the program running

    while running:

        print_menu()
        user_selection = input('Your selection> ')  # ask the user for their selection

        # if the user selects 1 or 'a' run the add new book function
        if user_selection == '1' or user_selection.lower() == 'a':
            add_new_book(all_books)

        # if the user selects 2 or 'r' run the borrow books function
        elif user_selection == '2' or user_selection.lower() == 'r':
            borrow_books(all_books, rented_isbns)

        # if the user selects 3 or 't' run the return a book function
        elif user_selection == '3' or user_selection.lower() == 't':
            return_a_book(all_books, rented_isbns)

        # if the user selects 4 or 'l' run the list all books function
        elif user_selection == '4' or user_selection.lower() == 'l':
            list_all_books(all_books, rented_isbns)

        # if the user selects 5 or 'x' print the list of books and stop the program
        elif user_selection == '5' or user_selection.lower() == 'x':
            running = False
            exit_program(all_books, rented_isbns)

        else:
            print("Wrong selection! Please selection a valid option.")


start()