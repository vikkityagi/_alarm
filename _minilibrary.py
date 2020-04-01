class Library:
    # define constructor which help create the class variable, method or attributes
    def __init__(self,list_of_book,library_name):
        self.lend_data={}
        self.list_of_book=list_of_book
        self.library_name=library_name

        #add book in dictionary
        for books in self.list_of_book:
            #none define no author have lend book
            self.lend_data[books]= None

    #this method define the index
    def display_books(self):
        for index, books in enumerate(self.list_of_book):
            print(f"{index}){books}")

    #this method define the book lend
    def lend_book(self,book,author):
        #check here that, book avavilable in the list  of book
        if book in self.list_of_book:
            # check here this book not lend by another person
            if self.lend_data[book] is None:
                #this book lend by this author
                self.lend_data[book]=author
            else:
                print(f"sorry! this book lend by {self.lend_data[book]}")
        else:
            print('you have written wrong book name')

     #define method add book
    def add_book(self,book_name):
        # here book add into the list of book
        self.list_of_book.append(book_name)
        # add book have not lend by any author till that
        self.lend_data[book_name]=None

    #this method used delete the book
    def delete_book(self,book_name):
        #delete book in the list
        self.list_of_book.remove(book_name)
        #delete book from author
        self.lend_data.pop(book_name)

    #this metod for return book
    def return_book(self,book,author):
        #here checks that this book available in the list of book
        if book in self.list_of_book:
            # here check book lend or not
            if self.lend_data(book) is not None:
                self.lend_book.pop(book)
            else:
                print(f"sorry! this {self.book} is not lend")
        else:
            print(f"you have written wrong book name")

def main():
    print("\n\n\nLibrary project made by vikki\n\n")
    list_book=['001  Adventure of Sherlock Holmes','002  Adventure of Tom Sawyer','003  Ain-i-Akbari','004  Alchemist, The','Alice in the Wonderland','005  An American Tragedy','006  Anand Math','007  Apple Cart','008  Area of Darkness']
    library_name='w.f.b'
    secret_key='123456'
    obj1=Library(list_book,library_name)
    print(f'welcome to {obj1.library_name} library \n\n for exit press q \n\n for display press d \n\n for lend press l \n\n for add press a \n\n for delete press del \n\n for return press r \n ')



    while True:
        _input = input("option:")
        print("\n")
        if _input == 'q':
            break
        elif _input == 'd':
            obj1.display_books()
        elif _input == 'l':
            _input1=input("What is your name:")
            _input2=input("which book do you want to lend:")
            if _input2 in obj1.list_of_book:
                print(" \n lend book \n")
                obj1.lend_book(_input2,_input1)
            else:
                print(f"you have written wrong book name")
        elif _input == 'a':
            _input2=input("Book Name: ")
            obj1.add_book(_input2)

        elif _input == 'del':
            _input3=input("Enter the secret key:")
            if secret_key == _input3:
                _input2=input("which book do you want to delete:")
                if _input2 in obj1.list_of_book:
                    obj1.delete_book(_input2)
                    print("\n deleted \n")
                else:
                    print(f"sorry! this book is not available into the {obj1.library_name} library")
            else:
                print(f"you have don't delete any book into the {obj1.library_name} library")

        elif _input == 'r':
            _input1=input("What is your name:")
            _input2=input("Which book do you want to return: ")
            if _input2 in obj1.list_of_book:
                obj1.return_book(_input2,_input1)
            else:
                print(f"this type of book is not lend by {_input1}")
main()
