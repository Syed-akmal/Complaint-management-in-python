from tkinter import *
from tkinter import messagebox as msg
import mysql.connector

root = Tk()
root.title("LOGIN")
root.geometry("720x600+300+130")
root.config(bg = "yellow")
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="complaint")
cur = db.cursor()
def verify_data():
 
    sql = "Select email, Password from login"
    cur.execute(sql)
    login = cur.fetchall()
    email = user.get()
    Password = pswrd.get()
     
    check = (email, Password)

    if check in login:
        msg.showinfo("Login", "You Logged in Successfully.")
        B = Button(root, text="View", font=("None 25 bold"), bg = "blue", activebackground="#268946",command=view)
        B.place(x = 250, y = 400)
    
    else:
        msg.showerror("Error", "Please Provide Right Credentials.")


Label(text="LOGIN FORM", font=("None 35 bold underline"), bg = "yellow").place(x = 160, y = 0)
 
Label(text="Email:", font=("None 25 bold"), bg = "yellow").place(x = 60, y = 100)
 
user = StringVar()
Entry(root, textvariable=user, font=("None 20 bold"), width=24).place(x = 230, y = 105)
 
Label(text="Password:", font=("None 25 bold"), bg = "yellow").place(x = 30, y = 200)
 
pswrd = StringVar()
Entry(root, textvariable=pswrd, font=("None 20 bold"), width=24).place(x = 230, y = 205)
 
B = Button(root, text="Login", font=("None 25 bold"), bg = "red", activebackground="#268946",command=verify_data)
B.place(x = 250, y = 300)

def view():
    my_w= Tk()
    my_w.geometry("400x250")
    my_connect=mysql.connector.connect(host="localhost",user="root",password="",database="complaint")
    my_conn= my_connect.cursor()
    my_conn.execute("SELECT * FROM info")
    i=0
    for  info in my_conn:
        for j in range(len(info)):
            e= Entry(my_w,width=20,fg="green")
            e.grid(row= i ,column= j)
            e.insert(END,info[j])
    i=i+1
    #my_w.mainloop()

    
root.mainloop()

