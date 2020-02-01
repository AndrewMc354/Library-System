import tkinter as tkinter

logs = []
books = []
oldid = ""
count = 0
a = []
CurrentBook = []

##
##
##
##
##
##
##
##Code Return
##
##
##
##
##
##
##

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

def MainReturn():
    def returning(name,cid):
        count = 0
        for book in books:
                if book[1] == name:
                        cbook = book
        for log in logs:
                if cbook[0] == log[0]:
                        CurrentIds = []
                        CurrentIds = log[4].split(",")
                        NewId = ""
                        count2 = 0
                        for Id in CurrentIds:
                                if Id != cid:
                                        if count2 == 0:
                                                NewId = Id
                                        else:
                                                NewId += "," + Id
                                        count2 +=1
                        logs[count][4] = NewId
                        logs[count][3] = str(int(logs[count][3])+1)
                        logs[count][2] = str(int(logs[count][2])-1)
                count +=1
        SaveFileLog("Log.txt")
        returntk.destroy()
        global a
        global CurrentBook
        count = 0
        a = []
        CurrentBook = []
        succ = tkinter.Tk()
        succ.config(bg="black")
        succ.geometry("200x50")
        succ.title("Successful Return")
        returned = tkinter.Label(succ, text="Successfully Returned",bg= "black",fg= "green")
        returned.pack()
        main = tkinter.Button(succ,text="Close",bg="black",fg="white",command= lambda: succ.destroy())
        main.pack()
                    
    def CheckedBooks(cid):
        if cid != "":
                global logs
                global books
                global count
                global a
                global CurrentBook
                logs = []
                books = []
                ReadFile("Database.txt")
                ReadFileLog("Log.txt")
                rows = 2
                count2 = 0
                if count > 0:
                    for Id in CurrentBook:
                        for x in range(0,len(books[0])+1):
                                a[count2].grid_forget()
                                count2 +=1
                        rows+=1
                count = 0
                a = []
                count = 0
                CurrentBook = []
                for log in logs:
                        currentIds = log[4].split(",")
                        for Id in currentIds:
                            if str(Id) == str(cid):
                                CurrentBook.append(log[0])
                
                for book in books:
                    for Id in CurrentBook:
                        if str(book[0]) == str(Id):
                            for x in range(0,len(book)):
                                a.append(tkinter.Label(returntk, text=book[x],bg= "black",fg= "white"))
                                a[count].grid(row = rows, column = x)
                                count +=1
                                if x == (len(book)-1):
                                    a.append(tkinter.Button(returntk, text="Return",bg= "black",fg= "white"))
                                    a[count]['command']=lambda name=a[count-2].cget("text"): returning(name,cid)
                                    a[count].grid(row = rows, column = (x+1))
                                    a[count].config(height=2, width= 10)
                                    count +=1                        
                            rows +=1
    returntk = tkinter.Tk()
    returntk.configure(bg="black")
    returntk.geometry("400x200")
    returntk.title("Return")
    returned = tkinter.Label(returntk, text="RETURN",bg= "black",fg= "white")
    returned.grid(row = 0, column = 1)
    returned.config(font=("Arial", "30"))
    login = tkinter.Label(returntk, text = "User ID",bg="black",fg="white")
    login.grid(row = 1, column = 0)
    userid = tkinter.Entry(returntk,bg="black",fg="white")
    userid.grid(row = 1,column = 1)
    checkbooks = tkinter.Button(returntk,text="Rented Books", bg = "black", fg = "white",command=lambda: CheckedBooks(userid.get()))
    checkbooks.config(height=2,width=10)
    checkbooks.grid(row=1, column = 3)
    def Return2():
        returntk.destroy()
        global a
        global CurrentBook
        count = 0
        a = []
        CurrentBook = []
    mainmenu = tkinter.Button(returntk,text="Main Menu", bg = "black", fg = "white",command=lambda: Return2())
    mainmenu.config(height=2,width=10)
    mainmenu.grid(row=0, column = 3)
