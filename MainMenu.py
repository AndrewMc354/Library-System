import tkinter as tkinter
from tkinter import TOP
from tkinter import LEFT
import sys
import BookSearch as S
import BookCheckout as C
import BookReturn as R
import BookWeed as W

def Searches():
    S.MainBooks()

def Checkout():
    C.MainCheck()

def Returned():
    R.MainReturn()

def Weeding():
    W.MainWeed()

def Menu():
    main = tkinter.Tk()
    main.title("Main Menu -- Student")
    main.configure(background = "black")
    main.geometry("400x220")

    menu = tkinter.Label(main, text="MAIN MENU",fg="white",bg="black")
    menu.config(font=("Arial", "30"))
    menu.pack(side = TOP)

    search = tkinter.Button(main, text = "Search",fg="white",bg="black"
                            ,command=Searches)
    search.config(height=2, width =10)
    search.pack(side = LEFT)

    checkout = tkinter.Button(main, text = "Checkout",fg="white",bg="black"
                              ,command=Checkout)
    checkout.config(height=2, width =10)
    checkout.pack(side = LEFT)

    return1 = tkinter.Button(main, text = "Return",fg="white",bg="black"
                             ,command=Returned)
    return1.config(height=2, width =10)
    return1.pack(side = LEFT)

    weed = tkinter.Button(main, text = "Weed",fg="white",bg="black"
                          ,command = Weeding)
    weed.config(height=2, width =10)
    weed.pack(side = LEFT)

    exit2 = tkinter.Button(main, text = "Exit", command = exit
                           ,fg="white",bg="black")
    exit2.config(height=2, width=10)
    exit2.pack(side = LEFT)

    main.mainloop()

Menu()
