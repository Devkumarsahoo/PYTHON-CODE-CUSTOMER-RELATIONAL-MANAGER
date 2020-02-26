#importing of libraries
import numpy as np
import matplotlib.pyplot as plt
from pymysql import *
from tkinter import *
import csv
from tkinter import messagebox
from PIL import ImageTk,Image

#connnection of database
hostname="localhost"
dbname="autodice"
dbpass=""
dbuser="root"
conn=connect(hostname, dbuser, dbpass, dbname)		
my_cursor=conn.cursor()



def myfunction():
    messagebox.showinfo("Info","Record Inserted")
def myfunction2():
    messagebox.showinfo("Info","File saved as Excel File")
def myfunction1():
    messagebox.showwarning("Info","Record Deleted")
def myfunction6():
	messagebox.showwarning("Info","Excel Data is Imported to database")
def myfunction7():
	messagebox.askquestion("Info","Do you want to Edit Record")

def myfunction4(event):
	warning.set("")
	
def myfunction5(event):
	warning1.set("")	


def add():
	root=Tk()
	# global declarations
	global first_name_box
	global address2_box
	global city_box
	global pincode_box
	global state_box
	global course_box
	global country_box
	global email_box
	global category_box
	global phone_box
	global payment_method_box
	global click1
	global click
	global drop1

	conn=connect(hostname, dbuser, dbpass, dbname)		
	my_cursor=conn.cursor()

	title_label =Label(root, text="AUTODICE CUSTOMER RELATIONAL MANAGER ",font="bold")
	title_label.grid(row=0, column=0, columnspan=2, pady=10)

	root.title(" AUTODICE CLASSES") 

	#Labels are created
	first_name_label = Label(root, text="Name").grid(row=1, column=0, sticky=W, padx=10)
	address2_label = Label(root, text="Address ").grid(row=4, column=0, sticky=W, padx=10)
	city_label = Label(root, text="City").grid(row=5, column=0, sticky=W, padx=10)
	state_label = Label(root, text="State").grid(row=6, column=0, sticky=W, padx=10)
	pincode_label =Label(root, text="Pincode").grid(row=7, column=0, sticky=W, padx=10)
	country_label = Label(root, text="Country").grid(row=8, column=0, sticky=W, padx=10)
	phone_label = Label(root, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
	email_label = Label(root, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
	payment_method_label = Label(root, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
	category_label=Label(root, text="Category").grid(row=12, column=0, sticky=W, padx=10)
	product_label=Label(root,text="Course").grid(row=13,column=0, sticky=W, padx=10)
	#Entry boxes are created
	first_name_box = Entry(root)
	first_name_box.grid(row=1, column=1)

	address2_box = Entry(root)
	address2_box.grid(row=4, column=1, pady=5)

	city_box = Entry(root)
	city_box.grid(row=5, column=1, pady=5)

	state_box = Entry(root)
	state_box.grid(row=6, column=1, pady=5)

	pincode_box = Entry(root)
	pincode_box.grid(row=7, column=1, pady=5)

	country_box = Entry(root)
	country_box.grid(row=8, column=1, pady=5)

	phone_box = Entry(root)
	phone_box.grid(row=9, column=1, pady=5)

	email_box = Entry(root)
	email_box.grid(row=10, column=1, pady=5)

	payment_method_box = Entry(root)
	payment_method_box.grid(row=11, column=1, pady=5)

	click1=StringVar(root)
	category_options=["CALL-ATTENDED","BUSY","INTERESTED","NOT-INTERESTED"]
	click1.set("Select-Category")
	#filter_button=Button(root,text="Apply Filter",command=filter).grid(row=16,column=0)
	drop2=OptionMenu(root,click1,*category_options).grid(row=12,column=1)
						
	click=StringVar(root)
	product_options=["PYTHON","NODE JS ","JAVA","SQL"]
	click.set("Select-Course")
	#filter_button=Button(root,text="Apply Filter",command=filter).grid(row=16,column=0)
	drop1=OptionMenu(root,click,*product_options).grid(row=13,column=1)

	# buttons are created
	add_customer_button = Button(root, text="Save Record to Database",bg='gold',fg='black', command=lambda:add_customer())
	add_customer_button.grid(row=15, column=1, columnspan=2, pady=10, padx=10, ipadx=145)
	root.state('zoomed')

def clear_fields():
	
	first_name_box.delete(0, END)				  
	address2_box.delete(0, END)
	city_box.delete(0, END)
	state_box.delete(0, END)
	pincode_box.delete(0, END)
	country_box.delete(0, END)
	phone_box.delete(0, END)
	email_box.delete(0, END)
	payment_method_box.delete(0, END)

def add_customer():
	conn=connect(hostname, dbuser, dbpass, dbname)
	my_cursor=conn.cursor()
	#my_cursor=conn.cursor()
	
	name=first_name_box.get()                   # using of get() to get input of text-boxes
	address=address2_box.get()
	city=city_box.get()
	state=state_box.get()
	pincode=pincode_box.get()
	country=country_box.get()
	phone=phone_box.get()
	email=email_box.get()
	payment=payment_method_box.get()
	category=click1.get()
	product=click.get()
	str="INSERT INTO customer(NAME,ADDRESS,CITY,STATE,PINCODE,COUNTRY,PHONE,EMAIL,PAYMENT,CATEGORY,PRODUCT) VALUES ('"+name+"' ,'"+address+"' ,'"+city+"' ,'"+state+"' ,'"+pincode+"' ,'"+country+"' ,'"+phone+"' ,'"+email+"' ,'"+payment+"' ,'"+category+"','"+product+"')"
	res=my_cursor.execute(str)
	print(name)
	conn.commit()
	conn.close()
	clear_fields()
	#myfunction()
	root.destroy()

#To open Look-up list

def look():
	
	conn=connect(hostname, dbuser, dbpass, dbname)
	my_cursor=conn.cursor()
	#my_cursor=conn.cursor()
	
	list_customer_query = Tk()
	list_customer_query.title("AUTODICE STUDENTS DETAILS")
	list_customer_query.iconbitmap(r'autodice.ico')
	#list_customer_query.geometry("800x800")
	
	#list_customer_query_label=Label(list_customer_query,text="AUTODICE STUDENTS DETAILS",font="bold").grid(row=0, column=0, columnspan=2, pady=10)
	
	# Query The Database
	my_cursor.execute("SELECT * FROM customer")
	result = my_cursor
	for index, x in enumerate(result):
		num = 0
		for y in x:
			lookup_label = Label(list_customer_query, text=y)
			lookup_label.grid(row=index, column=num)
			num +=1
	
	
	#look1_label.grid(row=0,column=0)
	#look1_label=Label(window1,text="AUTODICE STUDENTS",font="bold")
	#look_label=Label(window1,text=" NAME:-   "+str(x[1])+"   PHONE no.:-  "+str(x[7]))
	list_customer_query.state('zoomed')
	list_customer_query.mainloop()


# Write To CSV Excel Function

def write_to_csv():
	myfunction2()
	conn=connect(hostname, dbuser, dbpass, dbname)		
	my_cursor=conn.cursor()
	query = "SELECT * FROM CUSTOMER;" 
	my_cursor.execute(query)
	with open('Customer Data-List','w', newline='') as f:
		writer = csv.writer(f)
		for row in my_cursor.fetchall():
        		writer.writerow(row)

#To Draw Pie chart of Categories
def pie():
	#Counting the Number of Occurence of CATEGORY=BUSY
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'BUSY'")
	m=my_cursor.fetchone()[0]
	#Counting the Number of Occurence of CATEGORY=NOT-INTERSTED
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'NOT-INTERESTED'")
	n=my_cursor.fetchone()[0]
	#Counting the Number of Occurence of CATEGORY=INTERESTED
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'INTERESTED'")
	o=my_cursor.fetchone()[0]
	plt.title("CATEGORY VS SUB-CATEGORY")
	explode=(0.05,0.03,0.05)
	height = [m, n, o]
	bars = ('BUSY', 'NON-INTERESTED', 'INTERESTED')
	plt.pie(height,labels=bars,explode=explode,autopct='%1.1f%%',shadow=True)
	plt.show()
	
# Function to Draw Bar chart of Categories
def bar():
	#Counting the Number of Occurence of CATEGORY=BUSY
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'BUSY'")
	m=my_cursor.fetchone()[0]
	#Counting the Number of Occurence of CATEGORY=NOT-INTERESTED
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'NOT-INTERESTED'")
	n=my_cursor.fetchone()[0]
	#Counting the Number of Occurence of CATEGORY=INTERESTED
	my_cursor.execute("SELECT count(*) from customer where CATEGORY = 'INTERESTED'")
	o=my_cursor.fetchone()[0]
	
	height = [m, n, o]
	bars = ('BUSY', 'NON-INTERESTED', 'INTERESTED')
 # Create bars and choose color
	plt.bar(bars, height, color = (0.5,0.1,0.5,0.6))
 # Add title and axis names
	plt.title('CATEGORIES VS SUB-CATEGORIES')
	plt.xlabel('CATEGORIES')
	plt.ylabel('NO. OF ENQUIREIS')
 # Show graph
	plt.show()

# To Call the Graph
def call_graph():
	if(i.get()==1):
		pie()
	else:
		bar()	

def filter():
	
	my_cursor=conn.cursor()
	window3=Tk()
	window3.title("FILTER of AUTODICE STUDENTS")
	#window3.geometry("600x600")
	window3.iconbitmap(r'autodice.ico')
	#label=Label(window3,text=clicked.get(),font="bold").grid(row=0, column=0, columnspan=2, pady=10)
    
	my_cursor.execute("SELECT * from customer where CATEGORY='"+clicked.get()+"'")
	result=my_cursor
	for index,x in enumerate(result): # used when two indexes(here :- index,x) are used 
		num = 0
		for y in x:
			lookup_label=Label(window3, text= y)
			lookup_label.grid(row=index+1, column=num)
			num=num+1
	window3.state('zoomed')	     
	window3.mainloop()

def delete():
	
	conn=connect(hostname, dbuser, dbpass, dbname)
	my_cursor=conn.cursor()
    #res2=my_cursor.execute(str1)
	m=delete_entry.get()
	my_cursor.execute("DELETE from customer where ID = '"+m+"'")
    #result=my_cursor
	#label3=Label(window,text="DELETED").grid(row=15,column=3)
    #res=my_cursor.execute(str)
	conn.commit()
	conn.close()
	delete_entry.delete(0, END)
	myfunction1()

def edit():
	
	global window5
	window5=Tk()
	window5.title("UPDATION OF CUSTOMER RECORD") 
	title_label =Label(window5,text=" UPDATATION OF CUSTOMER DATA RECORD ",font="bold")
	title_label.grid(row=0, column=0, columnspan=2, pady=10)
	window5.geometry("500x560")
#global declarations of variables 

	global first_name_box
	global address2_box
	global city_box
	global pincode_box
	global state_box
	global course_box
	global country_box
	global email_box
	global category_box
	global phone_box
	global payment_method_box

	window5.iconbitmap(r'autodice.ico')
	
	record_id = edit_entry.get()
	my_cursor.execute("SELECT * FROM customer WHERE ID = " +record_id)
	records = my_cursor.fetchall()

#Labels are created
	first_name_label = Label(window5, text="Name").grid(row=1, column=0, sticky=W, padx=10)
	address2_label = Label(window5, text="Address ").grid(row=4, column=0, sticky=W, padx=10)
	city_label = Label(window5, text="City").grid(row=5, column=0, sticky=W, padx=10)
	state_label = Label(window5, text="State").grid(row=6, column=0, sticky=W, padx=10)
	pincode_label =Label(window5, text="Pincode").grid(row=7, column=0, sticky=W, padx=10)
	country_label = Label(window5, text="Country").grid(row=8, column=0, sticky=W, padx=10)
	phone_label = Label(window5, text="Phone Number").grid(row=9, column=0, sticky=W, padx=10)
	email_label = Label(window5, text="Email Address").grid(row=10, column=0, sticky=W, padx=10)
	payment_method_label = Label(window5, text="Payment Method").grid(row=11, column=0, sticky=W, padx=10)
	category_label=Label(window5, text="Category").grid(row=12, column=0, sticky=W, padx=10)
	product_label=Label(window5,text="Course").grid(row=13,column=0, sticky=W, padx=10)

#Entry boxes are created
	first_name_box = Entry(window5)
	first_name_box.grid(row=1, column=1)

	address2_box = Entry(window5)
	address2_box.grid(row=4, column=1, pady=5)

	city_box = Entry(window5)
	city_box.grid(row=5, column=1, pady=5)

	state_box = Entry(window5)
	state_box.grid(row=6, column=1, pady=5)

	pincode_box = Entry(window5)
	pincode_box.grid(row=7, column=1, pady=5)

	country_box = Entry(window5)
	country_box.grid(row=8, column=1, pady=5)

	phone_box = Entry(window5)
	phone_box.grid(row=9, column=1, pady=5)

	email_box = Entry(window5)
	email_box.grid(row=10, column=1, pady=5)

	payment_method_box = Entry(window5)
	payment_method_box.grid(row=11, column=1, pady=5)

	category_box=Entry(window5)
	category_box.grid(row=12,column=1, pady=5)

	course_box=Entry(window5)
	course_box.grid(row=13,column=1, pady=5)
	
	for record in records:
		first_name_box.insert(0,record[1])
		address2_box.insert(0,record[2])		    
		city_box.insert(0,record[3])
		state_box.insert(0,record[4])
		pincode_box.insert(0,record[5])
		country_box.insert(0,record[6])
		phone_box.insert(0,record[7])
		email_box.insert(0,record[8])
		payment_method_box.insert(0,record[9])
		category_box.insert(0,record[10])
		course_box.insert(0,record[11])
	edit_btn=Button(window5, text="Save Record",command=update,bg="gold",fg="black")
	edit_btn.grid(row=15, column=1, columnspan=2, pady=10, padx=10, ipadx=145)	
	window5.state('zoomed')


def update():
	
	conn=connect(hostname,dbuser,dbpass,dbname)
	my_cursor=conn.cursor()
	
	name=first_name_box.get()                   # using of get() to get input of text-boxes
	address=address2_box.get()
	city=city_box.get()
	state=state_box.get()
	pincode=pincode_box.get()
	country=country_box.get()
	phone=phone_box.get()
	email=email_box.get()
	payment=payment_method_box.get()
	category=category_box.get()
	product=course_box.get()	
	i=edit_entry.get()    	
	
	my_cursor.execute("UPDATE customer SET NAME='"+name+"',ADDRESS='"+address+"',CITY='"+city+"',STATE='"+state+"',PINCODE='"+pincode+"',COUNTRY='"+country+"',PHONE='"+phone+"',EMAIL='"+email+"',PAYMENT='"+payment+"',CATEGORY='"+category+"',PRODUCT='"+product+"' WHERE ID='"+i+"'")
	
	conn.commit()    
	
	conn.close()    
	window5.destroy()


# Write To CSV Excel Function

def write_to_csv():
	myfunction2()
	conn=connect(hostname, dbuser, dbpass, dbname)		
	my_cursor=conn.cursor()
	query = "SELECT * FROM CUSTOMER;" 
	my_cursor.execute(query)
	with open('Customer Data-List','w', newline='') as f:
		writer = csv.writer(f)
		for row in my_cursor.fetchall():
        		writer.writerow(row)



#To Import Excel Data to Database
def import_to_database():
	myfunction6()
	conn=connect(hostname, dbuser, dbpass, dbname)
	my_cursor=conn.cursor()
	csv_data=csv.reader(open('DEV.csv'))
	for row in csv_data:
		my_cursor.execute("INSERT INTO customer(NAME,ADDRESS,CITY,STATE,PINCODE,COUNTRY,PHONE,EMAIL,PAYMENT,CATEGORY,PRODUCT)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",row)
		
	conn.commit()
	conn.close()
	print("succesfully transfered")	

def add_customer():
	conn=connect(hostname, dbuser, dbpass, dbname)
	my_cursor=conn.cursor()
	#my_cursor=conn.cursor()
	
	name=first_name_box.get()                   # using of get() to get input of text-boxes
	address=address2_box.get()
	city=city_box.get()
	state=state_box.get()
	pincode=pincode_box.get()
	country=country_box.get()
	phone=phone_box.get()
	email=email_box.get()
	payment=payment_method_box.get()
	category=click1.get()
	product=click.get()
	str="INSERT INTO customer(NAME,ADDRESS,CITY,STATE,PINCODE,COUNTRY,PHONE,EMAIL,PAYMENT,CATEGORY,PRODUCT) VALUES ('"+name+"' ,'"+address+"' ,'"+city+"' ,'"+state+"' ,'"+pincode+"' ,'"+country+"' ,'"+phone+"' ,'"+email+"' ,'"+payment+"' ,'"+category+"','"+product+"')"
	res=my_cursor.execute(str)
	conn.commit()
	conn.close()
	clear_fields()
	myfunction()







window=Tk()


window.iconbitmap(r'autodice.ico')
window.title(" AUTODICE CLASSES") 
window.state('zoomed')
################################################upper row ################################################ 
# add-to-custumer image 
canvas=Canvas(window,width=2000,height=2000)
photo=ImageTk.PhotoImage(file="add.png")
canvas.create_image(0,0,image=photo,anchor='nw')
canvas.place(x=60,y=20)

#delete customer image
canvas1=Canvas(window,width=2000,height=2000)
photo1=ImageTk.PhotoImage(file="import.png")
canvas1.create_image(0,0,image=photo1,anchor='nw')
canvas1.place(x=360,y=20)

#edit customer image
canvas2=Canvas(window,width=2000,height=2000)
photo2=ImageTk.PhotoImage(file="look.png")
canvas2.create_image(0,0,image=photo2,anchor='nw')
canvas2.place(x=660,y=20)

# import customer image
canvas3=Canvas(window,width=2000,height=2000)
photo3=ImageTk.PhotoImage(file="graph.png")
canvas3.create_image(0,0,image=photo3,anchor='nw')
canvas3.place(x=960,y=20)


#######################    UPPER    buttons ***************************************************************

add_customer_button = Button(window, text="Add Customer To Database",bg='gold',fg='black', command=add)
add_customer_button.place(x=80,y=240)

import_button=Button(window,text="Import to Database",bg='gold',fg='black',command=import_to_database)
import_button.place(x=400,y=240)

list_button=Button(window,text="Look-up Customer List",bg='gold',fg='black',command=look)
list_button.place(x=700,y=240)


graph_button=Button(window,text="Show Graph",command=call_graph,bg='gold',fg='black').place(x=960,y=240)

i=IntVar()
rad1=Radiobutton(window,text="Pie Graph",bg='gold',fg='black',value=1,variable=i).place(x=1060,y=240)


rad2=Radiobutton(window,text="Bar Graph",bg='gold',fg='black',value=2,variable=i).place(x=1060,y=270)




##################################################### lower row ***************************************************

canvas4=Canvas(window,width=2000,height=2000)
photo4=ImageTk.PhotoImage(file="filter.png")
canvas4.create_image(0,0,image=photo4,anchor='nw')
canvas4.place(x=60,y=360)



canvas5=Canvas(window,width=2000,height=2000)
photo5=ImageTk.PhotoImage(file="edit.png")
canvas5.create_image(0,0,image=photo5,anchor='nw')
canvas5.place(x=360,y=360)



canvas6=Canvas(window,width=2000,height=2000)
photo6=ImageTk.PhotoImage(file="delete.png")
canvas6.create_image(0,0,image=photo6,anchor='nw')
canvas6.place(x=660,y=360)



canvas7=Canvas(window,width=2000,height=2000)
photo7=ImageTk.PhotoImage(file="export.png")
canvas7.create_image(0,0,image=photo7,anchor='nw')
canvas7.place(x=960,y=360)


##############################  BUTTON LOWER ROW****************************************************************

clicked=StringVar()
options=["CALL-ATTENDED","BUSY","INTERESTED","NOT-INTERESTED"]
clicked.set("DROP-MENU")
filter_button=Button(window,text="Apply Filter",bg='gold',fg='black',command=filter).place(x=60,y=580)
drop=OptionMenu(window,clicked,*options).place(x=150,y=580)


warning1=StringVar()
warning1.set("Enter the ID")
edit_button=Button(window,text="Edit Record",bg='gold',fg='black',command=edit)
edit_button.place(x=360,y=580)
edit_entry=Entry(window,text=warning1)
edit_entry.bind("<FocusIn>",myfunction5)
edit_entry.place(x=450,y=586)   



delete_button=Button(window,text="Delete Record",bg='gold',fg='black',command=delete)
delete_button.place(x=660,y=580)

warning=StringVar()
warning.set("Enter the ID")
delete_entry=Entry(window,text=warning)
delete_entry.bind("<FocusIn>",myfunction4)
delete_entry.place(x=760,y=586)


csv_button = Button(window, text="   Save to Excel  ",bg='gold',fg='black',command=write_to_csv)
csv_button.place(x=1020,y=580)

#************************************************END OF PROJECT *********************************

window.mainloop()