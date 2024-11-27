from tkinter import *
from tkinter import ttk
import sqlite3


root = Tk()
root.geometry('550x600')
root.maxsize(width=550, height=600)
root.minsize(width= 550, height=600)
root.configure(bg="sky blue")
root.title("Property Registration")

conn = sqlite3.connect('PropReg.db')
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Property(FullName text, Email text, Gender text, Age integer, P_type text, P_loc text, PAN integer)""")

def submit():
    conn = sqlite3.connect('PropReg.db')
    genshow=''
    typeshow=''
    if var1.get() == 1:
        genshow='Male'
    elif var1.get() == 2:
        genshow='Female'
    if var2.get() == 1:
        typeshow='Residential'
    elif var2.get() == 2:
        typeshow='Commercial'
    c = conn.cursor()
    c.execute("INSERT INTO Property VALUES(:FullName, :Email, :Gender, :Age, :P_type, :P_loc, :PAN)",
    {
        'FullName': FullName.get(),
        'Email': Email.get(),
        'Gender': genshow,
        'Age': Age.get(),
        'P_type': typeshow,
        'P_loc': P_loc.get(),
        'PAN': PAN.get(),
    })
    conn.commit()

    conn.close()

    FullName.delete(0, END)
    Email.delete(0, END)
    var1.set(0)
    Age.delete(0, END)
    var2.set(0)
    P_loc.delete(0, END)
    PAN.delete(0, END)


def show():
    conn = sqlite3.connect('PropReg.db')
    c = conn.cursor()
    w = Tk()

    w.title('REGISTRATIONS')    
    w.geometry('850x500') 
    w.minsize(width=850, height=500)
    w.maxsize(width=850, height=500)

    tree = ttk.Treeview(w, height=450)
    tree.pack()

    tree["columns"] = ('one', 'two', 'three', 'four', 'five', 'six', 'seven','eight')
    tree["show"] = 'headings'

    tree.column('one', width=150, minwidth=150, anchor='c')
    tree.column('two', width=170, minwidth=170, anchor='c')
    tree.column('three', width=75, minwidth=75, anchor='c')
    tree.column('four', width=75, minwidth=75, anchor='c')
    tree.column('five', width=100, minwidth=100, anchor='c')
    tree.column('six', width=130, minwidth=130, anchor='c')
    tree.column('seven', width=100, minwidth=100, anchor='c')
    tree.column('eight', width=50, minwidth=50, anchor='c')

    tree.heading('one', text='Full Name')
    tree.heading('two', text='Email')
    tree.heading('three', text='Gender')
    tree.heading('four', text='Age')
    tree.heading('five', text='Prop. Type')
    tree.heading('six', text='Prop. Loc.')
    tree.heading('seven', text='PAN No.')
    tree.heading('eight', text='Reg. ID')

    c.execute("SELECT *, oid FROM Property ")
    record = c.fetchall()
    #print(record)
    # print_rec=' '
    for i in record:
        tree.insert('', 'end', values=i)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('PropReg.db')
    c = conn.cursor()

    c.execute("DELETE FROM Property WHERE oid=?", (Delete.get(),))

    conn.commit()

    conn.close()

label_0 = Label(root, text="Property Registration", width=20, font=('Times New Roman',20,"bold"), bg='sky blue')
label_0.place(x=100, y=20)
FullNamelab = Label(root, text="Full Name:", width=20, font=("bold", 12), bg='sky blue')
FullNamelab.place(x=80, y=80)
FullName = Entry(root)
FullName.place(x=240, y=80)
Emaillab = Label(root, text="Email:", width=20, font=("bold", 12), bg='sky blue')
Emaillab.place(x=68, y=130)
Email = Entry(root)
Email.place(x=240, y=130)
Genderlab = Label(root, text="Gender:", width=20, font=("bold", 12), bg='sky blue')
Genderlab.place(x=70, y=180)
var1 = IntVar()
Gender = Radiobutton(root, text="Male", padx=5, variable=var1, value=1, bg='sky blue').place(x=235, y=180)
Gender = Radiobutton(root, text="Female", padx=20, variable=var1, value=2, bg='sky blue').place(x=290, y=180)
Agelab = Label(root, text="Age:", width=20, font=("bold", 12), bg='sky blue')
Agelab.place(x=70, y=230)
Age = Entry(root)
Age.place(x=240, y=230)
P_typelab = Label(root, text="Property Type:", width=20, font=("bold", 12), bg='sky blue')
P_typelab.place(x=70, y=280)
var2 = IntVar()
P_type = Radiobutton(root, text="Residential", padx=5, variable=var2, value=1, bg='sky blue').place(x=235, y=280)
P_type = Radiobutton(root, text="Commercial", padx=20, variable=var2, value=2, bg='sky blue').place(x=330, y=280)
P_loclab = Label(root, text="Property Location:", width=20, font=("bold", 12), bg='sky blue')
P_loclab.place(x=80, y=330)
P_loc = Entry(root)
P_loc.place(x=240, y=330)
PANlab = Label(root, text="PAN number:", width=20, font=("bold", 12), bg='sky blue')
PANlab.place(x=80, y=380)
PAN = Entry(root)
PAN.place(x=240, y=380)

Sub_btn = Button(root, text='Submit', width=20, bg='grey64', fg='black', command=submit, font=('Times New Roman', 10, "bold")).place(x=80, y=460)

Show_btn = Button(root, text='Show all registrations', width=20, bg='grey64', fg='black', command=show, font=('Times New Roman', 10, "bold")).place(x=320, y=460)

label_10 = Label(root, text="DELETE", width=20, font=('Times New Roman', 15, "bold"), bg='sky blue')
label_10.place(x=150, y=510)

Deletelab = Label(root, text="Enter Reg. ID:", width=20, font=("bold", 12), bg='sky blue')
Deletelab.place(x=50, y=560)
Delete = Entry(root)
Delete.place(x=200, y=560)

Delete_btn = Button(root, text='Delete Registration', width=20, bg='grey64', fg='black', command=delete, font=('Times New Roman', 10, "bold")).place(x=360, y=560)

root.mainloop()
