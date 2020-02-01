import tkinter as tkinter
import time
import sys
import BookCheckout as C

##ID,Title,Author
## 0, 1,      2
books = []
logs = []
b = []
count = 0
searchbooks = []
oldbook = ""

def ReadFile(Filename):
    file = open(Filename, "r")
    for line in file:
        x=line.strip()
        record = x.split(":")
        books.append(record)
    file.close()

def ReadFileLog(Filename):
            file = open(Filename, "r")
            for line in file:
                x=line.strip()
                record = x.split(":")
                logs.append(record)
            file.close()  

def MainBooks():
    global books
    global logs
    books = []
    logs = []
    ReadFile("Database.txt")
    ReadFileLog("Log.txt")
    def Returned():
        book.destroy()
        global count
        global b
        global oldbook
        global searchbooks
        count = 0
        b = []
        oldbook = []
        searchbooks = []

    def Unavailable(Name):
        Returned()
        C.Unavailable(Name)
        

    def RunSearch(Name):
        C.CheckoutScreen(Name)
        book.destroy()
    
    def SearchBook():
        rows2 = 0
        global count
        global b
        global oldbook
        global searchbooks
        count2 = 0
        if count > 0:
            for book1 in searchbooks:
                if oldbook in book1[1]:
                    for x in range(0,len(books[1])+1):
                        b[count2].grid_forget()
                        count2 +=1
                rows2+=3
        rows2 = 0
        WantedBook = searchent.get()
        search3 = tkinter.Label(book, text="SEARCH RESULTS",bg= "black",fg= "white")
        search3.grid(row = rows2, column = 1)
        search3.config(font=("Arial", "30"))
        ret.grid(row=0, column =3)
        count = 0
        searchbooks = []
        searchnum = 0
        b = []
        for book1 in books:
            if WantedBook in book1[1]:
                if books.index(book1) != 0:
                    searchbooks.append(book1)        
        for each in searchbooks:
             rows2+=3
             for x in range(0,len(each)):
                 b.append(tkinter.Label(book, text=each[x],bg= "black",fg= "white"))
                 b[count].grid(row = rows2, column = x)
                 count +=1
             for log in logs:
                 if log[0] == each[0]:
                     if int(log[3]) > 0:
                         b.append(tkinter.Button(book, text = "Available",command = lambda Name=(searchbooks[searchnum]): RunSearch(Name),bg= "black",fg= "white"))
                         b[count].grid(row=rows2,column=3)
                         b[count].config(height=2, width=10)
                     else:
                         b.append(tkinter.Button(book, text = "Unavailable",command = lambda Name=(searchbooks[searchnum][1]): Unavailable(Name),bg= "black",fg= "white"))
                         b[count].grid(row=rows2,column=3)
                         b[count].config(height=2, width=10)
                     count+=1
                     searchnum +=1
        oldbook = WantedBook
    book = tkinter.Tk()
    book.title("Search Books")
    book.configure(bg = "black")
    book.geometry("700x450")
    searchlbl = tkinter.Label(book, text="Type what you would like to search for:",bg= "black",fg= "white")
    searchlbl.grid(row=1,column=1,sticky="E")
    searchent = tkinter.Entry(book)
    searchent.grid(row=1,column=2)
    runsearch = tkinter.Button(book, text="Search",command=SearchBook,bg= "black",fg= "white")
    runsearch.grid(row=1, column=3)
    runsearch.config(height=2, width=10)
    ret = tkinter.Button(book, text="Main Menu",command=Returned,bg= "black",fg= "white")
    ret.grid(row = 1, column = 4)
    ret.config(height=2, width=10)
    book.mainloop()
