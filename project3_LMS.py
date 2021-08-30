class Library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("Books Present In Library Are: ")    
        for book in self.books:
            print(" *", book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(f"The Book {bookname} Has Been Issued To You!") 
            self.books.remove(bookname) 
        else:
            print("Sorry This Book Is Either Not Available Or Has Been Already Issued To Someone!")   

    def returnbook(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for Adding/Returning The Book {bookname}! Keep Reading!")


class Student(Library):

    def requestbook(self):
        try:
            req = input("Enter The Book You Want To Issue: ")
        except ValueError :
            print(" Please Enter A Valid Value!")
        l.borrowbook(req)   


    def returnbook(self):
        try:
            ret = input("Enter The Book You Want To Return: ")    
        except ValueError :
            print("Please Enter A Valid Value")
        l.returnbook(ret)

            
l = Library(["Algorithms", "django", "Clrs", "Python"])
s = Student(["Algorithms", "django", "Clrs", "Python"])

while True:
    welcomemsg = '''*************** WELCOME TO CENTRAL LIBRARY ***************

    Please Choose A Option:

    1. List Of Books
    2. Request A Book
    3. Add/Return A Book
    4. Exit
    '''
    print(welcomemsg)

    a = int(input("Enter A Choice: "))

    if a == 1 :
      l.displayavailablebooks()
    elif a == 2 :
      s.requestbook() 
    elif a == 3 :
      s.returnbook()  
    elif a == 4 :
        print("Thanks For Coming To Central Library! ")
        exit()
    else: 
        print("Invalid Choice!")    

    

    





        