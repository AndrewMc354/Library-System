import tkinter as tkinter
import datetime

books = []
logs = []
b = []
leastcheckedout = []
lastcheckedout = []
newbooks = []
newlogs = []

def ReadFile(Filename):        
        global books           
        file = open(Filename, "r")      
        for line in file:               
            stripped=line.strip()        
            record = stripped.split(":")
            books.append(record)        
        file.close()                    

def ReadFileLog(Filename):
        global logs     
        file = open(Filename, "r")      
        for line in file:               
            stripped=line.strip()       
            record = stripped.split(":")
            logs.append(record)         
        file.close()                    

def SaveFileLog(Filename):
        global newlogs  
        file = open(Filename, "w")      
        for log in newlogs:             
            towrite = ":".join(log)     
            towrite+="\n"               
            file.write(towrite)         
        file.close()                    
        
def SaveFile(Filename):
        global newbooks 
        file = open(Filename, "w")      
        for book in newbooks:           
            towrite = ":".join(book)    
            towrite+="\n"               
            file.write(towrite)         
        file.close()                   

def MainWeed():
    def Returned():
            weed.destroy()      
    def DisplayAllBookInformation():
        def Remove(row):
                global leastcheckedout
                global lastcheckedout
                global newbooks
                global newlogs
                
                if row == (len(books)+3):
                        bookid = (leastcheckedout[0])
                elif row == (len(books)+5):
                        bookid = (lastcheckedout[0])

                for book in books:
                        if book[0] != bookid:
                                newbooks.append(book)
                for log in logs:
                        if log[0] != bookid:
                                newlogs.append(log)

                SaveFileLog("Log.txt")
                SaveFile("Database.txt")

                weed.destroy()  

                succ = tkinter.Tk()
                succ.config(bg="black")
                succ.geometry("250x50")
                succ.title("Successful Return")
                returned = tkinter.Label(succ, text="Book Successfully Removed"
                                         ,bg= "black",fg= "green")
                returned.pack()
                main = tkinter.Button(succ,text="Close",bg="black",fg="white"
                                      ,command= lambda: succ.destroy())
                main.pack()

        global b
        global books
        global logs
        books = []
        logs = []
        ReadFile("Database.txt")
        ReadFileLog("Log.txt")

        rows = 1
        for book in books:
            if book[1] != "Title":
                for log in logs:       
                    if log[0] == book[0]:
                        for x in range(0,len(book)): 
                            b = tkinter.Label(weed, text=book[x],bg= "black"
                                              ,fg= "white")
                            b.grid(row = rows, column = x)
                        for x in range(0,len(log)):
                                if x != 0:
                                    b = tkinter.Label(weed, text=log[x]
                                                      ,bg= "black",fg= "white")
                                    b.grid(row = rows, column = (x+3))
                        rows += 1
            else:
                for x in range(0,len(book)):
                    b = tkinter.Label(weed, text=book[x],bg= "black"
                                      ,fg= "white")
                    b.grid(row = rows, column = x)

                b = tkinter.Label(weed, text="Num of Copies",bg= "black"
                                  ,fg= "white")
                b.grid(row = rows, column = 4)
                b = tkinter.Label(weed, text="Num of Rented Copies"
                                  ,bg= "black",fg= "white")
                b.grid(row = rows, column = 5)
                b = tkinter.Label(weed, text="Num of Available Copies"
                                  ,bg= "black",fg= "white")
                b.grid(row = rows, column = 6)
                b = tkinter.Label(weed, text="Id's of Users with Book"
                                  ,bg= "black",fg= "white")
                b.grid(row = rows, column = 7)
                b = tkinter.Label(weed, text="Num of Copies ever Rented"
                                  ,bg= "black",fg= "white")
                b.grid(row = rows, column = 8)
                b = tkinter.Label(weed, text="Last Date checked out"
                                  ,bg= "black",fg= "white")
                b.grid(row = rows, column = 9)
                rows += 1
        global leastcheckedout
        global lastcheckedout
        for log in logs:
                if leastcheckedout == [] or int(log[5]) < int(leastcheckedout[8]):
                        leastcheckedout = []
                        for book in books:
                                if book[0] == log[0]:
                                        for each in book:
                                                leastcheckedout.append(each)
                                        for each in log:
                                                leastcheckedout.append(each)
        for log in logs:
                if lastcheckedout == []:
                        lastcheckedout = []
                        for book in books:
                                if book[0] == log[0]:
                                        for each in book:
                                                lastcheckedout.append(each)
                                        for each in log:
                                                lastcheckedout.append(each)
                else:
                        if len(log[6]) == 9:
                                y1 = int(log[6][5:9])
                                m1 = int(log[6][2:4])
                                d1 = int(log[6][0])
                                date1 = datetime.date(y1, m1, d1)
                        else:
                                y1 = int(log[6][6:10])
                                m1 = int(log[6][3:5])
                                d1 = int(log[6][0:2])
                                date1 = datetime.date(y1, m1, d1)
                        if len(lastcheckedout[9]) == 9:
                                y1 = int(lastcheckedout[9][5:9])
                                m1 = int(lastcheckedout[9][2:4])
                                d1 = int(lastcheckedout[9][0])
                                date2 = datetime.date(y1, m1, d1)
                        else:
                                y2 = int(lastcheckedout[9][6:10])
                                m2 = int(lastcheckedout[9][3:5])
                                d2 = int(lastcheckedout[9][0:2])
                                date2 = datetime.date(y2, m2, d2)
                        date3 = date1 - date2
                        if str(date3)[0] == "-":
                                lastcheckedout = []
                                for book in books:
                                        if book[0] == log[0]:
                                                for each in book:
                                                        lastcheckedout.append(each)
                                                for each in log:
                                                        lastcheckedout.append(each)  
        header = tkinter.Label(weed, text="REMOVEABLE BOOKS",bg= "black"
                               ,fg= "white")
        header.grid(row = rows, column = 1)
        header.config(font=("Arial", "30"))
        rows += 1
        header = tkinter.Label(weed, text="It is recommended you remove the following book\nAs it has been checked out the fewest times"
                               ,bg= "black",fg= "white")
        header.grid(row = rows, column = 1)
        header.config(font=("Arial", "10"))
        rows += 1
        for x in range(0,len(leastcheckedout)):
            b = tkinter.Label(weed, text=leastcheckedout[x],bg= "black"
                              ,fg= "white")
            b.grid(row = rows, column = x)
        remove = tkinter.Button(weed, text="Remove Book"
                                ,command=lambda row = rows:Remove(row)
                                ,bg= "black",fg= "white")
        remove.grid(row = rows, column = 10)
        remove.config(height=2, width=10)
        rows += 1
        header = tkinter.Label(weed,text="It is recommended you remove the following book\nSince it was last checked out earliest"
                               , bg= "black",fg= "white")
        header.grid(row = rows, column = 1)
        header.config(font=("Arial", "10"))
        rows += 1
        for x in range(0,len(lastcheckedout)):
            b = tkinter.Label(weed, text=lastcheckedout[x],bg= "black"
                              ,fg= "white")
            b.grid(row = rows, column = x)
        remove = tkinter.Button(weed, text="Remove Book"
                                ,command=lambda row = rows:Remove(row)
                                ,bg= "black",fg= "white")
        remove.grid(row = rows, column = 10)
        remove.config(height=2, width=10)
        rows += 1
    weed = tkinter.Tk()
    weed.title("Weeding")
    weed.configure(background = "black")
    weed.geometry("1440x600")
    header = tkinter.Label(weed, text="WEEDING",bg= "black",fg= "white")
    header.grid(row = 0, column = 1)
    header.config(font=("Arial", "30"))
    ret = tkinter.Button(weed, text="Main Menu",command=Returned
                         ,bg= "black",fg= "white")
    ret.grid(row = 0, column = 10)
    ret.config(height=2, width=10)
    DisplayAllBookInformation()
