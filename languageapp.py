from tkinter import *
from backend import Database

database = Database("mylanguage.db")

def view_words_command():
    lb1.delete(0,END)
    for row in database.view_all_words():
        lb1.insert(END,lb1.insert(END,str(row[0])+ ". Language: " + row[1] + ", English: " + row[2] + ", Word: " + row[3] + ", Pronunciation: " + row[4] + ", Definition: " + row[5]))

def view_rules_command():
    lb2.delete(0,END)
    for row in database.view_all_rules():
        lb2.insert(END,str(row[0]) + ". Language: " + row[1] + ", Rule Name: " + row[2] + ", Rule: " + row[3])

def search_words_command():
    lb1.delete(0,END)
    for row in database.search_words(lang_text.get(),eng_text.get(),word_text.get(),pronunciation_text.get(),definition_text.get()):
        lb1.insert(END,str(row[0]) + ". Language: " + row[1] + ", English: " + row[2] + ", Word: " + row[3] + ", Pronunciation: " + row[4] + ", Definition: " + row[5])
        e_lang.delete(0,END)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)

def search_rules_command():
    lb2.delete(0,END)
    for row in database.search_rules(lang_text2.get(),name_text.get(),rule_text.get()):
        lb2.insert(END,str(row[0]) + ". Language: " + row[1] + ", Rule Name: " + row[2] + ", Rule: " + row[3])
        e_lang2.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)

def add_word_command():
    database.insert_word(lang_text.get(),eng_text.get(),word_text.get(),pronunciation_text.get(),definition_text.get())
    lb1.delete(0,END)
    e_lang.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_words_command()

def add_rule_command():
    database.insert_rule(lang_text2.get(),name_text.get(),rule_text.get())
    lb2.delete(0,END)
    e_lang2.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    view_rules_command()

def delete_word_command():
    database.delete_word(int(selected_tuple1[0]))
    lb1.delete(0,END)
    e_lang.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    view_words_command()

def delete_rule_command():
    database.delete_rule(int(selected_tuple2[0]))
    lb2.delete(0,END)
    e_lang2.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    view_rules_command()

def get_selected_row1(event):
    try:
        global selected_tuple1
        index=lb1.curselection()[0]
        selected_tuple1=lb1.get(index)
        try:
            get_val=int(selected_tuple1[0] + selected_tuple1[1] + selected_tuple1[2] + selected_tuple1[3] + selected_tuple1[4] + selected_tuple1[5])
        except ValueError:
            try:
                get_val=int(selected_tuple1[0] + selected_tuple1[1] + selected_tuple1[2] + selected_tuple1[3] + selected_tuple1[4])
            except ValueError:
                try:
                    get_val=int(selected_tuple1[0] + selected_tuple1[1] + selected_tuple1[2] + selected_tuple1[3])
                except ValueError:
                    try:
                        get_val=int(selected_tuple1[0] + selected_tuple1[1] + selected_tuple1[2])
                    except ValueError:
                        try:
                            get_val=int(selected_tuple1[0] + selected_tuple1[1])
                        except ValueError:
                            try:
                                get_val=int(selected_tuple1[0])
                            except ValueError:
                                pass
        e_lang.delete(0,END)
        e_lang.insert(END,database.show_lang1_values(get_val))
        e1.delete(0,END)
        e1.insert(END,database.show_eng_values(get_val))
        e2.delete(0,END)
        e2.insert(END,database.show_word_values(get_val))
        e3.delete(0,END)
        e3.insert(END,database.show_pronunciation_values(get_val))
        e4.delete(0,END)
        e4.insert(END,database.show_definition_values(get_val))
    except IndexError:
        pass

def get_selected_row2(event):
    try:
        global selected_tuple2
        index=lb2.curselection()[0]
        selected_tuple2=lb2.get(index)
        get_val=int(selected_tuple2[0])
        e_lang2.delete(0,END)
        e_lang2.insert(END,database.show_lang2_values(get_val))
        e5.delete(0,END)
        e5.insert(END,database.show_name_values(get_val))
        e6.delete(0,END)
        e6.insert(END,database.show_rule_values(get_val))
    except IndexError:
        pass

def update_word_command():
    database.update_word(selected_tuple1[0],lang_text.get(),eng_text.get(),word_text.get(),pronunciation_text.get(),definition_text.get())
    lb1.delete(0,END)
    view_words_command()
    e_lang.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def update_rule_command():
    database.update_rule(selected_tuple2[0],lang_text2.get(),name_text.get(),rule_text.get())
    lb2.delete(0,END)
    view_rules_command()
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

b3=Button(window,text="Add",width=10,font='Courier',command=add_word_command)
b3.grid(row=2,column=3,padx=15)

b4=Button(window,text="Update",width=10,font='Courier',command=update_word_command)
b4.grid(row=2,column=4,padx=15)

b5=Button(window,text="Delete",width=10,font='Courier',command=delete_word_command)
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

b8=Button(window,text="Add",width=10,font='Courier',command=add_rule_command)
b8.grid(row=8,column=3,padx=15)

b9=Button(window,text="Update",width=10,font='Courier',command=update_rule_command)
b9.grid(row=8,column=4,padx=15)

b10=Button(window,text="Delete",width=10,font='Courier',command=delete_rule_command)
b10.grid(row=9,column=0,pady=12)

b11=Button(window,text="Close",width=10,font='Courier',command=window.destroy)
b11.grid(row=9,column=4)

lb1.bind('<<ListboxSelect>>',get_selected_row1)
lb2.bind('<<ListboxSelect>>',get_selected_row2)

window.mainloop()
