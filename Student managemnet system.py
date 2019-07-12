import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
mainWindow=tk.Tk()
connection = sqlite3.connect('studentinfo.db') #file name
print("databsse opened sucessfully.")

TABLE_NAME="student_table"
STUDENT_ID="student_id"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_college"
STUDENT_ADDRESS="student_address"
STUDENT_PHONE="student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME +  " ( " + STUDENT_ID + " INTEGER PRIMARY KEY "  " AUTOINCREMENT, "
                   + STUDENT_NAME + " TEXT, "
                    + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT , " + STUDENT_PHONE + " INTEGER);")

print("table created sucessfully.")
mainWindow.title("database")#title

heading_label = tk.Label(mainWindow, text="student name")
heading_label.pack()

name_field=tk.Entry(mainWindow)
name_field.pack()

heading_label = tk.Label(mainWindow, text="student college")
heading_label.pack()

college_field=tk.Entry(mainWindow)
college_field.pack()

heading_label = tk.Label(mainWindow, text="student address")
heading_label.pack()

address_field=tk.Entry(mainWindow)
address_field.pack()


heading_label = tk.Label(mainWindow, text="student phone")
heading_label.pack()

phone_field=tk.Entry(mainWindow)
phone_field.pack()


def takeValueInput():
    name = name_field.get()
    college = college_field.get()
    address = address_field.get()
    phone = phone_field.get()
    if ((name == '') | (college == '') | (address == '') | (phone == '')):
        messagebox.showerror("nothing ", "nothing Saved in database.")
    else:
        try:

            connection.execute(
                "INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                                   ", " + STUDENT_PHONE + " ) VALUES ( '" +name+"', '"+college+"'," + " '"+address+"',"+phone +");")
            connection.commit()
            messagebox.showinfo("Sucess ", "data Saved database.")

        except sqlite3.OperationalError:
            messagebox.showerror("sqlite3.OperationalError"," enter values accordingly")


button = tk.Button(mainWindow, text="save value", command=lambda: takeValueInput())
button.pack()

# Retrieve record\

def retrive():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

    for row in cursor:
        print("Student id is: ", row[0])
        print("Student name is: ", row[1])
        print("Student college is: ", row[2])
        print("Student phone is: ", row[4])

button=tk.Button(mainWindow, text="get value", command=lambda :retrive())
button.pack()

mainWindow.mainloop()