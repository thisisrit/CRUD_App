from tkinter import *
import sqlite3

# conn = sqlite3.connect('myDb.db')
conn = sqlite3.connect("myDb.db")
curr = conn.cursor()

cl = Tk()
cl.minsize(800,600)
cl.maxsize(1000,800)

# Rollno= IntVar()
# Name = StringVar()
# Age = IntVar()
# Course = StringVar()
# Marks = IntVar()

def database():
    roll = e1.get()
    name = e2.get()
    age = e3.get()
    course = e4.get()
    marks = e5.get()
    # conn = sqlite3.connect("myDb.db")
    # with conn:
    #     curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS Student (Roll Integer, Name String, Age Integer, Course String, Marks Integer)")
    curr.execute("INSERT INTO Student (Roll, Name, Age, Course, Marks) VALUES(?,?,?,?,?)",(roll, name, age, course, marks))
    conn.commit()

def show():
    nf = Tk()
    nf.minsize(700,500)
    nf.maxsize(800,600)
    nf.title("Student Records")
    L1 = Label(nf, text="Student Details", font=('Arial', 25), bg = 'blue', fg = 'white',padx = 350, pady = 20)
    L1.grid(row=0, column=0, columnspan= 20)
    rno = Label(nf, text="Roll no.",font=('Arial', 15))
    rno.grid(row=1, column=1, padx=20, pady=10)
    name = Label(nf, text="Name",font=('Arial', 15))
    name.grid(row=1, column=2, padx=60, pady=10)
    age = Label(nf, text="Age",font=('Arial', 15))
    age.grid(row=1, column=3, padx=50, pady=10)
    cou = Label(nf, text="Course",font=('Arial', 15))
    cou.grid(row=1, column=4, padx=40, pady=10)
    mark = Label(nf, text="Marks",font=('Arial', 15))
    mark.grid(row=1, column=5, padx=30, pady=10)
    conn = sqlite3.connect("myDb.db")
    curr = conn.cursor()
    curr.execute("Select * from Student")
    r = curr.fetchall()
    num = 2
    for i in r:
        rno = Label(nf, text=i[0],font=('Arial', 15))
        rno.grid(row=num, column=1, padx=20, pady=10)

        name = Label(nf, text=i[1],font=('Arial', 15))
        name.grid(row=num, column=2, padx=20, pady=10)

        age = Label(nf, text=i[2],font=('Arial', 15))
        age.grid(row=num, column=3, padx=20, pady=10)

        cou = Label(nf, text=i[3],font=('Arial', 15))
        cou.grid(row=num, column=4, padx=20, pady=10)

        mark = Label(nf, text=i[4],font=('Arial', 15))
        mark.grid(row=num, column=5, padx=20, pady=10)

        num = num + 1

L = Label(cl, text="~ MySQL DB by Python-GUI ~", font=('Arial', 25), fg = 'green')
L.pack()

l1 = Label(cl, text="Rollno",font=('Arial', 15))
l1.place( x = 30, y = 100)
e1 = Entry(cl, bd =3)
e1.place(x = 100, y = 100, width=60, height=30)

l2 = Label(cl, text="Name",font=('Arial', 15))
l2.place( x = 30, y = 150)
e2 = Entry(cl, bd =3)
e2.place(x = 100, y = 150, width=230, height=30)

l3 = Label(cl, text="Age",font=('Arial', 15))
l3.place( x = 30, y = 200)
e3 = Entry(cl, bd =3)
e3.place(x = 100, y = 200, width=60, height=30)

l4 = Label(cl, text="Course",font=('Arial', 15))
l4.place( x = 30, y = 250)
e4 = Entry(cl, bd =3)
e4.place(x = 100, y = 250, width=150, height=30)

l5 = Label(cl, text="Marks",font=('Arial', 15))
l5.place( x = 30, y = 300)
e5 = Entry(cl, bd =3)
e5.place(x = 100, y = 300, width=60, height=30)

l6 = Label(cl, text="Select Roll no. to\n Update/Find/Delete",font=('Arial', 15))
l6.place( x = 30, y = 380)

drop= OptionMenu(cl,"C++", "Java","Python","JavaScript","Rust","GoLang")
drop.place(x = 40, y = 440)

b1 = Button(cl, text="Show Db",font=('Arial', 15),command=show)
b1.place(x = 600 , y = 100, width = 100)

b2 = Button(cl, text="Add Data",font=('Arial', 15),command=database)
b2.place(x = 600 , y = 150, width = 100)

b3 = Button(cl, text="Clear",font=('Arial', 15))
b3.place(x = 600 , y = 200, width = 100)

b4 = Button(cl, text="Update",font=('Arial', 15))
b4.place(x = 200 , y = 440, width = 100)

b5 = Button(cl, text="Find",font=('Arial', 15))
b5.place(x = 350 , y = 440, width = 100)

b6 = Button(cl, text="Remove",font=('Arial', 15))
b6.place(x = 500 , y = 440, width = 100)

b7 = Button(cl, text="Exit",font=('Arial', 15))
b7.place(x = 350 , y = 500, width = 100)
cl.mainloop()