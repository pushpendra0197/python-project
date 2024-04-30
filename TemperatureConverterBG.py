#!/usr/bin/env python
# coding: utf-8

# In[2]:


#temperature converter

from tkinter import *
import tkinter 
cv=tkinter.Tk()
cv.geometry("300x300")
cv.maxsize(width=615,height=440)
cv.title("coverter")
cv.configure(bg="red")
#lables
ti=PhotoImage(file=r"C:\Users\KINGNICKS-DELL\Downloads\temperature-2707.png")
l0=Label(cv,image=ti).place(x=0,y=0)
l1=Label(cv,text="Celsius-Fahrenheit-Celsius",bg="white",fg="red",font=('Arial',15)).place(x=150,y=5)
l2=Label(cv,text="input for fahrenheit conversion",bg="white",font=('Arial',9)).place(x=3,y=100)
l3=Label(cv,text="input for celsius conversion",bg="white",font=('Arial',10)).place(x=3,y=150)
l4=Label(cv,text="=",bg="white").place(x=180,y=100)
l5=Label(cv,text="=",bg="white").place(x=180,y=150)
l6=Label(cv,text="conversion",bg="white",font=('Arial',12)).place(x=3,y=200)
l6=Label(cv,text="=",bg="white").place(x=180,y=200)
#entry boxes
E1=Entry(cv,bd=5)
E1.place(x=210,y=95)
E2=Entry(cv,bd=5)
E2.place(x=210,y=145)
E3=Entry(cv,bd=5)
E3.place(x=210,y=200)

def reset():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
def fahrenheit():
    num=Entry.get(E1)
    num=int(num)
    fahrenheit=(num*1.8)+32
    Entry.insert(E3,0,fahrenheit)
def celsius():
    num=Entry.get(E2)
    num=int(num)
    celsius=(num-32)*5/9
    Entry.insert(E3,0,celsius)

button1=Button(cv,text="Submit for FH",command=fahrenheit,bg="yellow").place(x=80,y=250)
button2=Button(cv,text="Submit for Cel",command=celsius,bg="yellow").place(x=200,y=250)
button1=Button(cv,text="reset",command=reset,bg="yellow").place(x=300,y=250)
cv.mainloop()
 


# In[ ]:





# In[ ]:




