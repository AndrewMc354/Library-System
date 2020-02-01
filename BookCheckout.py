import tkinter as tkinter
from tkinter import TOP
from tkinter import LEFT
import time
import datetime

a = []
books = []
logs = []
count = 0
Correct = True
run2 = True
ran = 0
b = []
today = datetime.datetime.now()
curdate = str(today.day) + "/" + str(today.month) + "/" + str(today.year)

def ReadFile(Filename):
        global books
        file = open(Filename, "r")
        for line in file:
            x=line.strip()
            record = x.split(":")
            books.append(record)
        file.close()

def ReadFileLog(Filename):
        global logs
        file = open(Filename, "r")
        for line in file:
            x=line.strip()
            record = x.split(":")
            logs.append(record)
        file.close()    

def SaveFileLog(Filename):
        global logs
        file = open(Filename, "w")
        for log in logs:
            towrite = ":".join(log)
            towrite+="\n"
            file.write(towrite)
        file.close()    

def CheckoutScreen(Book):
        def CheckValidBook(inp,cuser):
            global Correct
            global books
            global logs
            Valid = True
            Found = False
            for book in books:
                if inp == book[0]:
                        Found = True
                        for log in logs:
                                if log[0] == inp:
                                    currentIds = []
                                    currentIds = log[4].split()
                                    for Id in currentIds:
                                        if Id == cuser:
                                            Valid = False
                                            Curtext = Passed.cget("text")
                                            Curtext += "\nYou already rent this book"
                                            Passed.config(text=Curtext)
            if Found == False:
                Correct = False
                Curtext = Passed.cget("text")
                Curtext += "\nInvalid Book Id"
                Passed.config(text=Curtext,fg="red")
            if Valid == False:
                Correct = False
                Passed.config(text=Curtext,fg="red")
                
        def CheckValidUser(inp):
            global Correct
            cuser = inp 
            if inp.isnumeric() == True and 999<int(inp)<10000:
                Valid = True
            else:
                Valid = False
                Correct = False
                Curtext = "Invalid User Id"
                Passed.config(text=Curtext,fg="red")
                
        def Check(Book):
                global Correct
                global logs
                global books
                global curdate
                logs = []
                books = []
                ReadFile("Database.txt")
                ReadFileLog("Log.txt")
                Correct = True
                Curtext = ""
                Passed.config(text=Curtext)
                cuser = user.get()
                cbook = bookid.get()
                CheckValidUser(cuser)
                CheckValidBook(cbook,cuser)
                if str(Book[0]) == str(cbook):
                        if Correct == True:
                                count = 0
                                for log in logs:
                                    if cbook == log[0]:
                                        CurrentIds = []
                                        CurrentIds = log[4].split(",")
                                        CurrentIds.append(cuser)
                                        logs[count][4] = ",".join(CurrentIds)
                                        logs[count][2] = str(int(logs[count][2])+1)
                                        logs[count][5] = str(int(logs[count][5])+1)
                                        logs[count][6] = curdate
                                        logs[count][3] = str(int(logs[count][3])-1)
                                    count +=1
                                SaveFileLog("Log.txt")
                                Checkout.destroy()
                                global run2
                                run2 = False
                else:
                        Curtext = "You have entered a different Book Id to what you selected"
                        Passed.config(text=Curtext,fg="red")

        def Return():
            Checkout.destroy()
            
        Checkout = tkinter.Tk()
        Checkout.configure(bg="black")
        Checkout.geometry("580x300")
        Checkout.title("Login")
        avail = tkinter.Label(Checkout, text="LOGIN",bg= "black",fg= "white")
        avail.grid(row = 0, column = 1)
        avail.config(font=("Arial", "30"))
        currentbook = tkinter.Label(Checkout, text=("The Id for " + Book[1] + " is " + Book[0]),bg= "black",fg= "white")
        currentbook.grid(row = 1, column = 1)
        b = tkinter.Label(Checkout, text="User ID",bg= "black",fg= "white")
        b.grid(row = 2, column = 0)
        b = tkinter.Label(Checkout, text="Book ID",bg= "black",fg= "white")
        b.grid(row = 3, column = 0)
        user = tkinter.Entry(Checkout,bg="black",fg="white")
        user.grid(row = 2,column = 1)
        bookid = tkinter.Entry(Checkout,bg="black",fg="white")
        bookid.grid(row = 3,column = 1)
        returnbook = tkinter.Button(Checkout,text="Return",bg="black",fg="white",command=Return)
        returnbook.config(height=2, width= 10)
        returnbook.grid(row = 0,column = 2)
        Passed = tkinter.Label(Checkout,text = "",bg="black",fg="white")
        Passed.grid(row=5,column=1)
        FinalCheck = tkinter.Button(Checkout,text="Checkout", bg = "black", fg = "white",command=lambda: Check(Book))
        FinalCheck.config(height=2,width=10)
        FinalCheck.grid(row=4, column = 1)

def Unavailable(Book):
        def Returned():
           unavail.destroy()
        global logs
        global books
        logs = []
        books = []
        ReadFile("Database.txt")
        ReadFileLog("Log.txt")
        unavail = tkinter.Tk()
        unavail.configure(bg="black")
        unavail.title("Unavailable Book")
        unavail.geometry("600x200")
        temp = "The requested book " + Book + " is unavailable"
        ubook = tkinter.Label(unavail, text=temp,bg="black",fg="white")
        ubook.pack()
        for book in books:
                if book[1] == Book:
                        cbook = book
        for log in logs:                
                if str(log[0]) == str(cbook[0]):
                        currentIds = []
                        currentIds = log[4].split(",")
                        for Id in currentIds:
                                output = "This book is rented by: " + Id
                                b = tkinter.Label(unavail, text =output,bg="black",fg="white")
                                b.pack()
        FinalCheck = tkinter.Button(unavail,text="Main Menu", bg = "black", fg = "white",command=Returned)
        FinalCheck.config(height=2,width=10)
        FinalCheck.pack()

def MainCheck():            
    def Returned():
            global run2
            run2 = False
            abook.destroy()
            global rows
            global a
            global count
            global b
            rows = 1
            a = []
            count = 0
            b = []
    def AvailableBooks():
        def checkingout(name):
            global books
            for book in books:
                    if book[1] == name:
                            output = book
            CheckoutScreen(output)
            abook.destroy()
            global rows
            global a
            global count
            global b
            rows = 1
            a = []
            count = 0
            b = []
            

        def checkIds(name):
                abook.destroy()
                Unavailable(name)
                global rows
                global a
                global count
                global b
                rows = 1
                a = []
                count = 0
                b = []
            
        def DisplayAvailableBooks():      
            global rows
            global a
            global count
            global b
            rows = 1
            rows2 = 1
            count2 = 0
            for each in books:
                for log in logs:
                    if each[0] == log[0]:
                        if each[1] != "Title":
                            if int(log[3]) > 0:
                                for x in range(0,len(each)):
                                    b.append(tkinter.Label(abook, text=each[x],bg= "black",fg= "white"))
                                    b[count2].grid(row = rows, column = x)
                                    if x == (len(each)-1):
                                        a.append(tkinter.Button(abook, text="Checkout",bg= "black",fg= "white"))
                                        a[count]['command']=lambda name=b[(count2-1)].cget("text") : checkingout(name)
                                        a[count].grid(row = rows, column = (x+1))
                                        a[count].config(height=2, width= 10)
                                        count +=1
                                    count2 += 1
                                rows +=1
                            else:
                                 for x in range(0,len(each)):
                                    b.append(tkinter.Label(abook, text=each[x],bg= "black",fg= "white"))
                                    b[count2].grid(row = rows2, column = 5+x)
                                    if x == (len(each)-1):
                                        a.append(tkinter.Button(abook, text="IDs of Users",bg= "black",fg= "white"))
                                        a[count]['command']=lambda name=b[(count2-1)].cget("text") : checkIds(name)
                                        a[count].grid(row = rows2, column = (5+(x+1)))
                                        a[count].config(height=2, width= 10)
                                        count +=1
                                    count2 += 1
                                 rows2 +=1
                        else:
                            for x in range(0,len(each)):
                                    b = tkinter.Label(abook, text=each[x])
                                    b.grid(row = rows, column = x)
                            rows +=1
        DisplayAvailableBooks()
    global books
    global logs
    books = []
    logs = []
    abook = tkinter.Tk()
    abook.configure(bg="black")
    abook.geometry("1250x550")
    abook.title("Checkout Books")
    avail = tkinter.Label(abook, text="AVAILABLE BOOKS",bg= "black",fg= "white")
    avail.grid(row = 0, column = 1)
    avail.config(font=("Arial", "30"))
    notavail = tkinter.Label(abook, text="UNAVAILABLE BOOKS",bg= "black",fg= "white")
    notavail.grid(row = 0, column = 6)
    notavail.config(font=("Arial", "30"))
    ReadFile("Database.txt")
    ReadFileLog("Log.txt")
    ret = tkinter.Button(abook, text="Main Menu",command=Returned,bg= "black",fg= "white")
    ret.grid(row = 0, column = 8)
    ret.config(height=2, width=10)
    AvailableBooks()
