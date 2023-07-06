import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import *
import tkinter.messagebox as mb 
root=Tk()
mydb=mysql.connector.connect(
	host="localhost",
	user="root",
	password="Hasini@123")
cursor = mydb.cursor()
connector = mydb
root.geometry("1200x700")
root.title("Contact Book")
if_bg= 'Gray70'
cf_bg = 'Gray57'
rf_bg = 'Gray35'
frame_font = ('Garamond', 14)
heading_label = Label(root, text = "CONTACT BOOK", font = ("Noto Sans CJK TC", 15, "bold"), bg="Black", fg="White")
l_frame = Frame(root, bg =if_bg)
c_frame = Frame(root, bg = cf_bg)
r_frame = Frame(root, bg = rf_bg)
name_strvar = StringVar()
phone_strvar = StringVar()
email_strvar = StringVar()
address_strvar=StringVar()
search_strvar=StringVar()
Label(l_frame, text="Name", bg=if_bg, fg ="black", font = frame_font).place(relx=0.3, rely = 0.05)
name_entry = Entry(l_frame, width = 15, font =("Verdana ", 11), textvariable=name_strvar)
name_entry.place(relx = 0.1, rely = 0.1)
Label(l_frame, text="Phone Number", bg=if_bg, fg ="black", font = frame_font).place(relx=0.23, rely = 0.2)
phone_entry = Entry(l_frame, width = 15, font =("Verdana ", 11), textvariable=phone_strvar)
phone_entry.place(relx = 0.1, rely = 0.25)
Label(l_frame, text="Email", bg=if_bg, fg ="black", font = frame_font).place(relx=0.3, rely = 0.35)
email_entry = Entry(l_frame, width = 15, font =("Verdana ", 11), textvariable=email_strvar)
email_entry.place(relx = 0.1, rely = 0.4)
Label(l_frame, text="Address", bg=if_bg, fg ="black", font = frame_font).place(relx=0.28, rely = 0.5)
address_entry = Entry(l_frame, width = 15, font =("Verdana ", 11), textvariable=address_strvar)
address_entry.place(relx = 0.1, rely = 0.55)

def search():
	global connector 
	query = str(search_strvar.get())
	if query !='':
		listbox.delete(0, END)
		cursor.execute('SELECT * FROM ADDRESS_BOOK.CONTACTS WHERE NAME LIKE %s', ("%"+query+ "%",))
		check = cursor.fetchall()
		for data in check:
			listbox.insert(END, data[1])
	else:
		list_contacts()
def submit_record(): 
	global name_strvar, email_strvar, phone_strvar, address_entry
	global cursor
	name, email, phone, address = name_strvar.get(), email_strvar.get(), phone_strvar.get(), address_strvar.get()
	if name == '' or email == '' or phone == '' or address == "": 
		mb.showerror("Error!, Please fill all the fields")
	else: 
		cursor.execute(
			"INSERT INTO ADDRESS_BOOK.CONTACTS (NAME, EMAIL, PHONE_NUMBER, ADDRESS) VALUES (%s, %s, %s, %s)", (name, email, phone, address))
	connector.commit()
	mb.showinfo("Contact added", "We have stored the contact sucessfully")	
	listbox.delete(0, END)
	list_contacts()
	clear_fields()
def view_record(): 
	global name_strvar, phone_strvar, email_strvar, address_entry, listbox, cursor
	x=listbox.get(ACTIVE)

def clear_fields():
	global name_strvar, phone_strvar, email_strvar, address_entry, listbox
	listbox.selection_clear(0, END)
	name_strvar.set('')
	phone_strvar.set('')
	email_strvar.set('')
	address_strvar.set('')
def delete_record(): 
	global listbox, connector, cursor
	if not listbox.get(ACTIVE):
		mb.showerror("No item selected", "You have not selected any time!")
	cursor.execute('DELETE FROM ADDRESS_BOOK.CONTACTS WHERE NAME = %s', (listbox.get(ACTIVE)))
	connector.commit()
	mb.showinfo("Contact deleted", "The desired contact has been deleted")
	listbox.delete(0,END)
	list_contacts()
def delete_all_records(): 
	cursor.execute('DELETE FROM ADDRESS_BOOK.CONTACTS')
	connector.commit()
	mb.showinfo("All record deleted", "All of the records in your contact boox have been deleted")
	listbox.delete(0, END)
	list_contacts()

def list_contacts(): 
	global cursor 
	cursor.execute('SELECT NAME FROM ADDRESS_BOOK.CONTACTS')
	fetch = cursor.fetchall()
	for data in fetch: 
		listbox.insert(END, data)
search_entry=Entry(c_frame, width=16, font=("Verdana", 12), textvariable=search_strvar).place(relx=0.13, rely=0.04)
Button(c_frame, text = "Search", font=frame_font, width=15, command=search).place(relx=0.13, rely=0.1)
Button(c_frame, text = "Add Record", font=frame_font, width=15, command=submit_record).place(relx=0.13, rely=0.2)
Button(c_frame, text = "View Record", font=frame_font, width=15, command=view_record).place(relx=0.13, rely=0.3)
Button(c_frame, text = "Clear Fields", font=frame_font, width=15, command=clear_fields).place(relx=0.13, rely=0.4)
Button(c_frame, text = "Delete Record", font=frame_font, width=15, command=delete_record).place(relx=0.13, rely=0.5)
Button(c_frame, text = "Delete All Records", font=frame_font, width=15, command=delete_all_records).place(relx=0.13, rely=0.6)

Label(r_frame, text="Saved Contacts", font =("Noto Sans CJK TC", 14), bg=rf_bg).place(relx=0.25, rely=0.05)
listbox=Listbox(r_frame, selectbackground = "Sky Blue", bg="Gainsboro", font=("Helvetica", 12), height = 20, width=25)
scroller = Scrollbar(listbox, orient=VERTICAL, command=listbox.yview)
scroller.place(relx=0.93, rely=0, relheight=1)
listbox.config(yscrollcommand = scroller.set)
listbox.place(relx=0.1, rely=0.15)
heading_label.pack(side=TOP, fill=X)
l_frame.place(relx=0, relheight = 1, y=30, relwidth = 0.3)
c_frame.place(relx=0.3, relheight=1, y=30, relwidth=0.3)
r_frame.place(relx = 0.6, relheight =1, y=30, relwidth=0.4)
#root.resizable(0,0)
root.mainloop()