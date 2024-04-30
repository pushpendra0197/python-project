#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# TRAFFIC CHALLAN-Label




#TYPE(TRAFFIC RULE BREAK)-label= COMBOBOX WITH OPTION( red light,helmet,license,seatbelt,PUC)
#FINE=RS-label=ENTRY BOX - for append the fine value in entry box
#Vehicle no-label=Entrybox=for enter the vehicle number. 
from tkinter import *
from tkinter.ttk import Combobox
tc=Tk()
tc.geometry("600x600")
tc.maxsize(width=600,height=600)
tc.title("TRAFFIC CHALLAN")
#icon or bgic=PhotoImage(file=r"C:\Users\KINGNICKS-DELL\Downloads\r.jpg")
ic=PhotoImage(file=r"C:\Users\KINGNICKS-DELL\Downloads\—Pngtree—black texture public welfare obeys_1044038.png")
tc.iconphoto(False,ic)
bg=PhotoImage(file=r"C:\Users\KINGNICKS-DELL\Downloads\ta.png")
l0=Label(tc,image=bg).place(x=0,y=0)
#label
l1=Label(text="TRAFFIC CHALLAN",fg="black",font=("ARIAL",15)).place(x=250,y=0)
l2=Label(text="Type(Traffic rule break",fg="black",font=("ARIAL",12)).place(x=130,y=70)
combo=Combobox(tc,value=["RedLight"," No-Helmet","No-License","No-Seatbelt","PUC","OverSpeeding","Accident"],width=20)
combo.place(x=300,y=70)
l3=Label(text="Vehicle No",fg="black",font=("ARIAL",12)).place(x=130,y=120)
#entry box for fine value show
E1=Entry(bd=5)
E1.place(x=300,y=120)
#list box for showing display
box=Listbox(tc,bd=5,width=50,height=10)
box.place(x=130,y=160)

#creating function

def reset():
    E1.delete(0,END)
    box.delete(0,END)
    combo.delete(0,END)
def traffic():
    vehicle=Entry.get(E1)
    traffic=Entry.get(combo)
    if traffic=="RedLight":
      f=("You Break Red Light: Fine RS.200")
    elif traffic=="NO-Helmet":
      f=("NO-Helmet: Fine RS.500")
    elif traffic=="No-License":
      f=("No-License: Fine RS.1000")
    elif traffic=="No-Seatbelt":
      f=("No-Seatbelt: Fine RS.1500")
    elif traffic=="PUC":
      f=("PUC: Fine RS.1200")
    elif traffic=="OverSpeeding":
      f=("Over Speeding: Fine RS.300")
    elif traffic=="Accident":
      f=("Accident: Punishment of 7 Year Jail and 7 Lakh Fine")
    Listbox.insert(box,0,f)
    print(f)
    Listbox.insert(box,0,vehicle)
    print(vehicle)
B=Button(tc, text ="Submit",command = traffic,bg='yellow',bd=10,font=("Arial",10)).place(x=190,y=350)
c=Button(tc, text ="Reset",command = reset,bg='yellow',bd=10,font=("Arial",10)).place(x=280,y=350)
    
    

tc.mainloop()
 


# In[ ]:




