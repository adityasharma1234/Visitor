from tkinter import *
import os
from pymysql import*
from tkinter import messagebox as msg
from datetime import datetime
now = datetime.now()
checkin = now.strftime('%Y-%m-%d')
checkout = now.strftime('%Y-%m-%d')
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("3000x2500")

    global name
    global phone
    global name_entry
    global phone_entry
    global checkin_entry
    global checkout_entry
    global host_entry
    global address_entry

    username = StringVar()
    phone = StringVar()

    Label(register_screen, text="Please enter details below", bg="red").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="NAME * ")

    #username_label.grid(register_screen,row=0,column=0)

    username_lable.pack()
    username_entry = Entry(register_screen,textvariable=username)
    #username_entry.grid(register_screen,row=0,column=1)
    username_entry.pack()
    contactnumber_lable = Label(register_screen, text="PHONE * ")
    contactnumber_lable.pack()
    phone_entry = Entry(register_screen)
    phone_entry.pack()
    checkout_lable = Label(register_screen, text="check-out time * ")
    checkout_lable.pack()
    checkout_entry = Entry(register_screen)
    checkout_entry.pack()
    checkin_lable = Label(register_screen, text="check-in time * ")
    checkin_lable.pack()
    checkin_entry = Entry(register_screen)
    checkin_entry.pack()
    host_lable = Label(register_screen, text="host  name * ")
    host_lable.pack()
    host_entry = Entry(register_screen)
    host_entry.pack()


    address_lable = Label(register_screen, text="address visited * ")
    address_lable.pack()
    address_entry = Entry(register_screen)
    address_entry.pack()

    Label(register_screen, text="").pack()
    #Button(register_screen, text="Register", width=10, height=1, bg="red", command = register_user).pack()
    Button(register_screen, text="Register", width=10, height=1, bg="red", command = save2).pack()
def save2():
    con=connect(db='so',user='root',password='system',host='localhost')
    cur=con.cursor()
    name=name_entry.get()
    phone=int(phone_entry.get())
    checkout=checkout_entry.get()
    #checkout=checkin_entry.get()
    checkin=checkin_entry.get()
    host=host_entry.get()
    address=address_entry.get()
    i=cur.execute("insert into aditya values('%s', %d ,%s, %s,'%s','%s')"%(name,phone,checkout,checkin,host,address))
    if i>=1:
	    con.commit()
	    msg.showinfo('Information','Reocrd Saved')
	    name_entry.delete(0,'end')
	    phone_entry.delete(0,'end')
	    #am1.delete(0,'end')
            #if1.delete(0,'end')
            #b1.delete(0,'end')
    con.close()
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("3000x2500")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="green", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Register", height="5", width="50",fg='black',bg='blue',font=("Arial Bold", 10), command=register).pack()
    Label(text="").pack()
    main_screen.mainloop()


main_account_screen()
