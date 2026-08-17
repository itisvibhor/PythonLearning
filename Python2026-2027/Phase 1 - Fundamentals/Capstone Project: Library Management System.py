books_list = []
members_list = []
member_id_counter = 0

def detail_formatter(book_detail):
    book_detail = " ".join(book_detail.split())
    return book_detail.title()

def add_new_book():
    global books_list
    print("========== Add New Book Function==========")
    book_title = input("Enter Book Title : ")
    book_author = input("Enter Book Author : ")
    book_genre = input("Enter Book Genre : ")
    book_total_copies = int(input("Enter Book Total Copies : "))
    book_available_copies = int(input("Enter Book Available Copies : "))
    book_title = detail_formatter(book_title)
    book_author = detail_formatter(book_author)
    book_genre = detail_formatter(book_genre)

    books_dict = {
        "book_title" : book_title,
        "book_author" : book_author,
        "book_genre" : book_genre,
        "book_total_copies" : book_total_copies,
        "book_available_copies" : book_available_copies
    }
    books_list.append(books_dict)
    print("========== Book Added Successfully ==========")

def view_all_books(book_title_search = ""):
    if(book_title_search != ""):
        for i in range(0,len(books_list)):
           if(books_list[i]["book_title"] == book_title_search or books_list[i]["book_genre"] == book_title_search):
                print("========== Book Found ==========")
                print(f"Book Title => {books_list[i]['book_title']}")
                print(f"Book Author => {books_list[i]['book_author']}")
                print(f"Book Genre => {books_list[i]['book_genre']}")
                print(f"Total Book Copies => {books_list[i]['book_total_copies']}")
                print(f"Available Book Copies => {books_list[i]['book_available_copies']}")           
                
    else: 
        print("========== Book's Details ==========")
        for i in range(0,len(books_list)):
            print(f"Book Title => {books_list[i]['book_title']}")
            print(f"Book Author => {books_list[i]['book_author']}")
            print(f"Book Genre => {books_list[i]['book_genre']}")
            print(f"Total Book Copies => {books_list[i]['book_total_copies']}")
            print(f"Available Book Copies => {books_list[i]['book_available_copies']}")

def search_by_title():
    flag = 0
    print("========== Search Book Menu ==========")
    print("1. By Book Title ")
    print("2. By Book Genre")
    choice = int(input("Enter Option 1 | 2 => "))
    if choice == 1:
        title_input = input("Enter Title Of Book To Find/Search => ")
        title_input = detail_formatter(title_input)
        for i in range(0,len(books_list)):
            if books_list[i]["book_title"] == title_input:
                view_all_books(title_input)
                flag = flag + 1
            if flag > 1:
                print("Book Not Found")
    elif choice == 2:
        genre_input = input("Enter Genre Of Book To Find/Search => ")
        genre_input = detail_formatter(genre_input)
        for i in range(0,len(books_list)):
            if books_list[i]["book_genre"] == genre_input:
                view_all_books(genre_input)
                flag = flag +1
            if flag > 1:
                print("Book Not Found")
        pass
    else:
        print("Invalid Option")

def add_new_member(member_borrowed_books = []):
    global members_list
    global member_id_counter
    print("========== Add New Member Function==========")
    member_name = input("Enter Member Name => ")
    member_id_counter = member_id_counter + 1
    member_name = detail_formatter(member_name)

    members_info_dict = {
        "member_name" : member_name,
        "member_id" : member_id_counter,
        "member_borrowed_books" : []
    }
    members_list.append(members_info_dict)

def view_all_members():
    for i in range(0,len(members_list)):
        print(f"Member Name => {members_list[i]['member_name']}")
        print(f"Member Id => {members_list[i]['member_id']}")
        print(f"Member Borrowed Books => {members_list[i]['member_borrowed_books']}")

def member_id_check(member_id):
    for i in range(0,len(members_list)):
        if members_list[i]["member_id"] == member_id:
            return member_id
        else:
            return False

def issue_book():
    member_id_input= int(input("Enter Your Member ID =>"))
    member_id = member_id_check(member_id_input)
    temp = 0
    temp_1 = 0
    if member_id != False:
        view_all_books()
        book_choice = input("Enter Name of the book you want to issue => ") 
        book_choice = detail_formatter(book_choice)
        for i in range(0,len(books_list)):
            if books_list[i]["book_title"] == book_choice:
                if books_list[i]["book_available_copies"] > 0:
                    for i in range(0,len(members_list)):
                        if members_list[i]["member_id"] == member_id:
                            members_list[i]["member_borrowed_books"].append(book_choice)
                            print("Book Issue Successfully")
                    books_list[i]["book_available_copies"] - 1
                temp_1 = temp_1 + 1
            if temp_1 > 1:
                print("Book Not Available")
            temp = temp +1
        if temp >1 :
            print("Book Not Found By Name")
    else:
        print("Member Id Not Found")

while True:
    print("1. Add New Book")
    print("2. Add New Member")
    print("3. Issue Book")
    print("5. View All Books")
    print("6. View All Members")
    print("7. Search Book by Title/Genre")
    print("9. Exit")
    choice = int(input("Enter Your Selection : 1-9 => "))
    if choice == 1:
        add_new_book()

    elif choice == 2:
        add_new_member()

    elif choice == 3:
        issue_book()

    elif choice == 5:
        if books_list != []:
            view_all_books()
        else:
            print("Add Some Books First and Try Again!")

    elif choice == 6:
        if members_list != []:
            view_all_members()
        else:
            print("Add Some Books First and Try Again!")

    elif choice == 7:
        if books_list !=[]:
             search_by_title()
        else:
            print("Add Some Books First and Try Again!")  

    elif choice == 9:
        break
    else:
        print("Invalid Option! Try Again...")


