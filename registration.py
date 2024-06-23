from sqlite3.dbapi2 import IntegrityError
from tkinter import *
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


registration_number=StringVar()
password_user=StringVar()
name = StringVar( )




def login():
   refNumber=registration_number.get()
   password= password_user.get()
   conn = sqlite3.connect('registration.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Registration_number TEXT PRIMARY KEY NOT NULL,Password TEXT)')
   try:
      cursor.execute('INSERT INTO Student (Registration_number,password) VALUES(?,?)',(refNumber,password))
   except(sqlite3.IntegrityError):
      cursor.execute("UPDATE Student SET password = ? WHERE Registration_number = ? ",(password,refNumber))
   conn.commit()
   registration_number.initialize("")
   password_user.initialize("")
   messagebox.showinfo('INFORMATION',"LOGIN SUCCESSFULL")
   
   
             
label_0 = Label(root, text="REGISTRATION FORM",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Registration Number",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=registration_number)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Password",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=password_user, show="*")
entry_2.place(x=240,y=180)




Button(root, text='Submit',width=20,bg='brown',fg='white',command=login).place(x=180,y=300)

root.mainloop()























