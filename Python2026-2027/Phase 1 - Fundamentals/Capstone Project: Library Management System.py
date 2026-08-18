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
        if flag < 1:
            print("Book Not Found")
    elif choice == 2:
        genre_input = input("Enter Genre Of Book To Find/Search => ")
        genre_input = detail_formatter(genre_input)
        for i in range(0,len(books_list)):
            if books_list[i]["book_genre"] == genre_input:
                view_all_books(genre_input)
                flag = flag +1
        if flag < 1:
            print("Book Not Found")
    else:
        print("Invalid Option")

def add_new_member():
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
    return False

def issue_book():
    member_id_input= int(input("Enter Your Member ID =>"))
    member_id = member_id_check(member_id_input)
    temp = 0
    temp_1 = 0
    if member_id != False:
        print("Member Id Found")
        view_all_books()
        book_choice = input("Enter Name of the book you want to issue => ") 
        book_choice = detail_formatter(book_choice)
        for i in range(0,len(books_list)):
            if books_list[i]["book_title"] == book_choice:
                if books_list[i]["book_available_copies"] > 0:
                    for j in range(0,len(members_list)):
                        if members_list[j]["member_id"] == member_id:
                            members_list[j]["member_borrowed_books"].append(book_choice)
                            print("Book Issued Successfully")
                            books_list[i]["book_available_copies"] -= 1
                            temp_1 += 1
                            break
                if temp_1 < 1:
                    print("Book Not Available. Book Not Issued")
                temp = temp +1
        if temp < 1 :
            print("Book Not Found By Name")
    else:
        print(f"Member Does Not Exist / Not Found Having ID => {member_id_input}")

"""
return_book function does the following : 
1. takes book name as input. then formats it. ( Done )
2.checks whether the book name is present in the all books or not. If yes then proceeds with the process else not and gives error message. ( Done )
3.then member id input is taken and is being checked whether it is an member id from the database or not. if yes then proceeds else gives an error message.
4.then books title is removed from borrowed books list along with available copies is updated with count +1
"""

def return_book():
    flag = 0 , temp = 0
    book_return = input("Enter the name of the book to return")
    book_return = detail_formatter(book_return) #1
    for i in range(0,len(books_list)): #2
        if(books_list[i]["book_title"] == book_return):
            temp +=1
            member_id = int(input("Enter Your Member Id"))
            member_id = member_id_check(member_id)
            if member_id != False:
                for j in range(0,len(members_list)):
                    if members_list[j]["member_id"] == member_id:
                        for k in range(0,len(members_list[j]["member_borrowed_books"])):
                            if members_list[j]["member_borrowed_books"][k] == book_return:
                                print("Book Returned Successfully")
                                members_list[j]["member_borrowed_books"].remove(book_return)      
                                books_list[i]["book_available_copies"] += 1
                                flag +=1
                                break
                        if flag < 1:
                            print("Book Not Found In member's Borrowed Books")
            else:
                print("Member Id Not Found")
                break

    if temp < 1:
        print("Book Not Found in DataBase.")

while True:
    print("1. Add New Book")
    print("2. Add New Member")
    print("3. Issue Book")
    print("4. Return a Book")
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

    elif choice == 4:
        return_book()

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


