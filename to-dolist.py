#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
tdl=Tk()
tdl.geometry("600x600")
tdl.maxsize(width=600,height=600)
tdl.configure(bg="AntiqueWhite")
#label and function
l1=Label(text="TO-DO LIST",bg="AntiqueWhite",fg="Red",font=("timesnewroman",20)).place(x=200,y=0)
l2=Label(text=" Enter Task",bg="AntiqueWhite",fg="black",font=("timesnewroman",13)).place(x=20,y=120)
e1=Entry(bd=5,width=30)
e1.place(x=20,y=150)
listbox=Listbox(bd=5,width=20,height=15,font=("timesnewroman",15))
listbox.place(x=280,y=100)
#function
def addtask():
    data=Entry.get(e1)
    Listbox.insert(listbox,1,data)
    print(data)
def clearall():
    e1.delete(0,END)
    listbox.delete(0,END)
def clearrecent():
    listbox.delete(1,END)
    
b1=Button(text="Enter",bd=5,bg="red",command=addtask,width=7,height=1).place(x=100,y=200)
b1=Button(text="Clear Task",bd=5,bg="yellow",command=clearall,width=7,height=1).place(x=100,y=300)
b1=Button(text="Clear Recent Task ",bd=5,bg="yellow",command=clearrecent,width=15,height=1).place(x=70,y=250)

tdl.mainloop()
 
 


# In[ ]:



