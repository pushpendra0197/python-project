#!/usr/bin/env python
# coding: utf-8

# In[12]:


#calculator
from tkinter import *
import tkinter
from tkinter.ttk import Combobox
#for resize window
cal=tkinter.Tk()
cal.geometry("300x300")
cal.maxsize(width=600,height=600)
#to give the name
cal.title("Calculator")
#to edit the background
cal.configure(bg="red")
#label
l=Label(cal,text="My Calculator",fg="red",font=('Arial',14)).place(x=70,y=1)
l2=Label(cal,text="First Number",fg="black").place(x=1,y=40)
l3=Label(cal,text="Second Number",fg="black").place(x=1,y=70)
l4=Label(cal,text="Operator",fg="black").place(x=1,y=100)
l5=Label(cal,text="Answer",fg="black").place(x=1,y=130)
data=["+","-","*","/"]
combo= Combobox(cal,value=data,width=20)
combo['state']="readonly"
combo.place(x=90,y=100)
l6=Label(cal,text="Operator: +,-,*,/",font=("Arial",9)).place(x=80,y=230)
#creatinh entry  box for enter the value
E1=Entry(cal,bd=5)
E1.place(x=90,y=35)
E2=Entry(cal,bd=5)
E2.place(x=100,y=65)
E4=Entry(cal,bd=5)
E4.place(x=90,y=130)

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
B=Button(cal, text ="Submit",command = operation,bg='yellow',bd=5).place(x=50,y=170)
c=Button(cal, text ="reset",command = reset,bg='yellow',bd=5).place(x=150,y=170)
cal.mainloop()
 


# In[ ]:





# In[ ]:




