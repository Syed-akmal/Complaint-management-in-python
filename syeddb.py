from tkinter import *
import mysql.connector
class income:
    def __init__(self,root):
        self.f=Frame(root,height=400,width=700,bg = "tan")
        self.f.pack()
        self.l1=Label(text="NAME",bg = "tan")
        self.l2=Label(text="ID NUMBER",bg = "tan")
        self.l3=Label(text="COMMENT",bg = "tan")
        self.e1=Entry(self.f,width=25,font=("airtel",14))
        self.e2=Entry(self.f,width=15,font=("airtel",7))
        self.e3=Entry(self.f,width=25,font=("airtel",20))
        self.b1=Button(self.f,text="SAVE",width=15,height=2,bg = "green",command=self.display)
        self.b2=Button(self.f,text="CANCEL",width=15,height=2,bg = "red")
        self.b1.place(x=50,y=350)
        self.b2.place(x=250,y=350)
        self.l1.place(x=50,y=100)
        self.e1.place(x=200,y=100)
        self.l2.place(x=50,y=150)
        self.e2.place(x=200,y=150)
        self.l3.place(x=50,y=200)
        self.e3.place(x=200,y=200)
    def display(self):
        a=self.e1.get()
        b=self.e2.get()
        c=self.e3.get()
        if(len(a.strip())==0):
            print("Enter Your Name")
        elif(len(b.strip())==0):
            print("Enter Your ID NUMBER")
        elif(len(c.strip())==0):
            print("Enter Your Comment")
        else:
            mydb=mysql.connector.connect(host="localhost",user="root",password="",database="complaint")
            mycursor=mydb.cursor()
            sql="INSERT INTO info (name,idnumber,comment)values(%s,%s,%s)"
            val=(a,b,c)
            mycursor.execute(sql,val)
            mydb.commit()
            print("Registered Successfully")

root=Tk()
root.title("COMPLAINT FORM")
mb=income(root)
root.mainloop()













    
        
         
        
