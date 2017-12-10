from tkinter import *

window=Tk()

window.wm_title('Fantasy Language Builder')

lb1=Listbox(window,height=8,width=35,bd=3,relief='sunken')
lb1.grid(row=2,column=0,padx=8)

l1=Label(window,text="DICTIONARY",font=('Courier',18))
l1.grid(row=0,column=0,pady=20)

l2=Label(window,text="English",font='Courier')
l2.grid(row=0,column=1)

l3=Label(window,text="Word",font='Courier')
l3.grid(row=0,column=3)

l4=Label(window,text="Pronunciation",font='Courier')
l4.grid(row=1,column=1)

l5=Label(window,text="Definition",font='Courier')
l5.grid(row=1,column=3)

eng_text=StringVar()
e1=Entry(window,textvariable=eng_text)
e1.grid(row=0,column=2,padx=8)

word_text=StringVar()
e2=Entry(window,textvariable=word_text)
e2.grid(row=0,column=4,padx=8)

pronounciation_text=StringVar()
e3=Entry(window,textvariable=pronounciation_text)
e3.grid(row=1,column=2,padx=8)

definition_text=StringVar()
e4=Entry(window,textvariable=definition_text)
e4.grid(row=1,column=4,padx=8)

b1=Button(window,text="All",width=10,font='Courier')
b1.config(relief=SUNKEN)
b1.grid(row=2,column=1,padx=15)

b2=Button(window,text="Search",width=10,font='Courier')
b2.grid(row=2,column=2,padx=15)

b3=Button(window,text="Add",width=10,font='Courier')
b3.grid(row=2,column=3,padx=15)

b4=Button(window,text="Update",width=10,font='Courier')
b4.grid(row=2,column=4,padx=15)

b5=Button(window,text="Delete",width=10,font='Courier')
b5.grid(row=4,column=0,pady=12)

l6=Label(window,text="GRAMMAR",font=('Courier',18))
l6.grid(row=6,column=0)

lb2=Listbox(window,height=8,width=35,bd=3,relief='sunken')
lb2.grid(row=8,column=0,padx=8)

l7=Label(window,text="Rule Name",font='Courier')
l7.grid(row=6,column=1)

l3=Label(window,text="Rule",font='Courier')
l3.grid(row=6,column=3)

name_text=StringVar()
e5=Entry(window,textvariable=name_text)
e5.grid(row=6,column=2,padx=8)

name_text=StringVar()
e6=Entry(window,textvariable=name_text)
e6.grid(row=6,column=4,padx=8)

b6=Button(window,text="All",width=10,font='Courier')
b6.grid(row=8,column=1,padx=15)

b7=Button(window,text="Search",width=10,font='Courier')
b7.grid(row=8,column=2,padx=15)

b8=Button(window,text="Add",width=10,font='Courier')
b8.grid(row=8,column=3,padx=15)

b9=Button(window,text="Update",width=10,font='Courier')
b9.grid(row=8,column=4,padx=15)

b10=Button(window,text="Delete",width=10,font='Courier')
b10.grid(row=9,column=0,pady=12)

#lb1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
