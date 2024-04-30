#!/usr/bin/env python
# coding: utf-8

# In[1]:


#square and square root
from tkinter import *
import tkinter
#for resize window
cal=tkinter.Tk()
cal.geometry("400x400")
cal.maxsize(width=400,height=400)
#to give the name
cal.title("SquareAndRoot")
#to edit the background
cal.configure(bg="red")
#label
l=Label(cal,text="SquareAndRoot",fg="red",font=('Arial',14)).place(x=70,y=1)
l2=Label(cal,text="Enter Number",fg="black").place(x=1,y=40)
l5=Label(cal,text="Square",fg="black").place(x=1,y=100)
l6=Label(cal,text="SquareRoot",fg="black").place(x=1,y=150)
#creatinh entry  box for enter the value
E1=Entry(cal,bd=5)
E1.place(x=90,y=35)
E3=Entry(cal,bd=5)
E3.place(x=90,y=100)
E4=Entry(cal,bd=5)
E4.place(x=90,y=150)


def reset():
   E1.delete(0, END)
   E3.delete(0, END)
def square():
    num1=Entry.get(E1)
    num1=int(num1)
    square=num1**2
    Entry.insert(E3,0,int(square))
    print(square)
def squareroot():
    num1=Entry.get(E1)
    num1=int(num1)
    squareroot=num1**(1/2)
    Entry.insert(E4,0,squareroot)
    print(squareroot)
B=Button(cal, text ="sumbit",command = lambda:[square(),squareroot()],bg='yellow',bd=5).place(x=100,y=190)
d=Button(cal, text ="reset",command = reset,bg='yellow',bd=5).place(x=170,y=190)
cal.mainloop()
 


# In[ ]:




