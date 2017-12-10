from tkinter import *
from backend import Database

database = Database("mylanguage.db")

def view_words_command():
    lb1.delete(0,END)
    for row in database.view_all_words():
        lb1.insert(END,row)

def view_rules_command():
    lb2.delete(0,END)
    for row in database.view_all_rules():
        lb2.insert(END,row)

def search_words_command():
    lb1.delete(0,END)
    for row in database.search_words(lang_text.get(),eng_text.get(),word_text.get(),pronunciation_text.get(),definition_text.get()):
        lb1.insert(END,row)
        e_lang.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

def search_rules_command():
    lb1.delete(0,END)
    for row in database.search_rules(lang_text2.get(),name_text.get(),rule_text.get()):
        lb2.insert(END,row)
        e_lang2.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)

window=Tk()

window.wm_title('Fantasy Language Builder')

lb1=Listbox(window,height=8,width=35,bd=3,relief='sunken')
lb1.grid(row=2,column=0,padx=8,pady=10)

l1=Label(window,text="LANGUAGE",font=('Courier',18))
l1.grid(row=0,column=0)

l2=Label(window,text="English",font='Courier')
l2.grid(row=0,column=1)

l3=Label(window,text="Word",font='Courier')
l3.grid(row=0,column=3)

l4=Label(window,text="Pronunciation",font='Courier')
l4.grid(row=1,column=1)

l5=Label(window,text="Definition",font='Courier')
l5.grid(row=1,column=3)

lang_text=StringVar()
e_lang=Entry(window,textvariable=lang_text)
e_lang.grid(row=1,column=0)

eng_text=StringVar()
e1=Entry(window,textvariable=eng_text)
e1.grid(row=0,column=2,padx=8)

word_text=StringVar()
e2=Entry(window,textvariable=word_text)
e2.grid(row=0,column=4,padx=8)

pronunciation_text=StringVar()
e3=Entry(window,textvariable=pronunciation_text)
e3.grid(row=1,column=2,padx=8)

definition_text=StringVar()
e4=Entry(window,textvariable=definition_text)
e4.grid(row=1,column=4,padx=8)

b1=Button(window,text="All",width=10,font='Courier',command=view_words_command)
b1.grid(row=2,column=1,padx=15)

b2=Button(window,text="Search",width=10,font='Courier',command=search_words_command)
b2.grid(row=2,column=2,padx=15)

b3=Button(window,text="Add",width=10,font='Courier')
b3.grid(row=2,column=3,padx=15)

b4=Button(window,text="Update",width=10,font='Courier')
b4.grid(row=2,column=4,padx=15)

b5=Button(window,text="Delete",width=10,font='Courier')
b5.grid(row=4,column=0,pady=12)

l6=Label(window,text="GRAMMAR (Enter Language)",font=('Courier',18))
l6.grid(row=6,column=0)

lb2=Listbox(window,height=8,width=35,bd=3,relief='sunken')
lb2.grid(row=8,column=0,padx=8,pady=10)

l7=Label(window,text="Rule Name",font='Courier')
l7.grid(row=6,column=1)

l3=Label(window,text="Rule",font='Courier')
l3.grid(row=6,column=3)

lang_text2=StringVar()
e_lang2=Entry(window,textvariable=lang_text2)
e_lang2.grid(row=7,column=0)

name_text=StringVar()
e5=Entry(window,textvariable=name_text)
e5.grid(row=6,column=2,padx=8)

rule_text=StringVar()
e6=Entry(window,textvariable=rule_text)
e6.grid(row=6,column=4,padx=8)

b6=Button(window,text="All",width=10,font='Courier',command=view_rules_command)
b6.grid(row=8,column=1,padx=15)

b7=Button(window,text="Search",width=10,font='Courier',command=search_rules_command)
b7.grid(row=8,column=2,padx=15)

b8=Button(window,text="Add",width=10,font='Courier')
b8.grid(row=8,column=3,padx=15)

b9=Button(window,text="Update",width=10,font='Courier')
b9.grid(row=8,column=4,padx=15)

b10=Button(window,text="Delete",width=10,font='Courier')
b10.grid(row=9,column=0,pady=12)

b11=Button(window,text="Close",width=10,font='Courier')
b11.grid(row=9,column=4)

#lb1.bind('<<ListboxSelect>>',get_selected_row)

window.mainloop()
