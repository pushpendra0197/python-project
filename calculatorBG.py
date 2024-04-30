#!/usr/bin/env python
# coding: utf-8

# In[2]:


#calculator
from tkinter import *
import tkinter
from tkinter.ttk import Combobox
#for resize window
cal=tkinter.Tk()
cal.geometry("529x505")
cal.maxsize(width=529,height=505)
#to give the name
cal.title("Calculator")
#to edit the background
cal.configure(bg="red")
#label
bg=PhotoImage(file=r"C:\Users\KINGNICKS-DELL\Downloads\kindpng_1850674.png")
l7=Label(cal,image=bg).place(x=0,y=0)
l=Label(cal,text="My Calculator",fg="red",font=('Arial',18)).place(x=160,y=1)
l2=Label(cal,text="First Number",fg="black",font=('Arial',9)).place(x=10,y=40)
l3=Label(cal,text="Second Number",fg="black",font=('Arial',9)).place(x=10,y=70)
l4=Label(cal,text="Operator",fg="black",font=('Arial',9)).place(x=10,y=100)
l5=Label(cal,text="Answer",fg="black",font=('Arial',9)).place(x=10,y=130)
data=["+","-","*","/"]
combo= Combobox(cal,value=data,width=20)
combo['state']="readonly"
combo.place(x=150,y=100)
l6=Label(cal,text="Operator: +,-,*,/",font=("Arial",14)).place(x=130,y=230)

#creatinh entry  box for enter the value
E1=Entry(cal,bd=5)
E1.place(x=150,y=35)
E2=Entry(cal,bd=5)
E2.place(x=150,y=65)
E4=Entry(cal,bd=5)
E4.place(x=150,y=130)

def reset():
   E1.delete(0, END)
   E2.delete(0, END)
   E4.delete(0, END)
   combo.delete(0,END)

def operation():
    num1=Entry.get(E1)
    num2=Entry.get(E2)
    operator=Entry.get(combo)
    num1=int(num1)
    num2=int(num2) 
    if operator =="+":
        answer=num1+num2
    elif operator =="-":
        answer=num1-num2
    elif operator=="*":
        answer=num1*num2
    elif operator=="/":
        answer=num1/num2
    elif operator=="/":
        answer=num1/num2
    Entry.insert(E4,0,answer)
    print(answer)
B=Button(cal, text ="Submit",command = operation,bg='yellow',bd=5).place(x=130,y=170)
c=Button(cal, text ="reset",command = reset,bg='yellow',bd=5).place(x=200,y=170)
cal.mainloop()
 
 
 
 
 


# In[ ]:




