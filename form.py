import tkinter
from tkinter import *
from tkinter import messagebox
gui = Tk()
gui.geometry("300x100")
gui.title("Login")

user_label = Label(gui,text="Customer Name:").grid(row=0,column=0)
pwd_label= Label(gui,text="Password:").grid(row=1,column=0)

user_entry=Entry(gui)
user_entry.grid(row=0,column=1)

pwd_entry=Entry(gui,show="*")
pwd_entry.grid(row=1,column=1)
def log(event):
	import pymongo
	client = pymongo.MongoClient("mongodb://localhost:27017/")
	db=client["Login_info"]
	collection = db["Customer"]
	CustName = user_entry.get()
	pwd=pwd_entry.get()
	for a in collection.find({},{"CustName": 1, "Password":1}):
		cname=str(a["CustName"])
		cpwd=str(a["Password"])
		if CustName ==cname and pwd==cpwd:
			messagebox.showinfo("Login Successfull","Login Successful!")
			user_entry.delete('0',END)
			pwd_entry.delete('0',END)
		else:
			messagebox.showerror("Login Unsuccessfull","Invalid Name and Password")
			user_entry.delete('0',END)
			pwd_entry.delete('0',END)
logbtn=Button(gui,text="Login")
logbtn.grid(row=2,column=1)
logbtn.bind('<Button-1>',log)
gui.mainloop()
