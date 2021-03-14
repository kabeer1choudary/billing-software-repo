from tkinter import *
import sqlite3
import tkinter.messagebox as msgbx

connection = sqlite3.connect("F:\Python_Files\Billing Software\Database\store_db.db")
c = connection.cursor()

class Database_update:
    def __init__(self, master, *args, **kwargs):
        
        self.master = master
        self.heading = Label(master, text='Update the Database', font=(' ariel 20 bold'), fg='steelblue')
        self.heading.place(x=180, y=0)

        #Labels for the window

        self.id_l = Label(master, text='Enter Product ID', font=('ariel 12 bold'))
        self.id_l.place(x=0, y=50)

        self.name_l = Label(master, text='Enter Product Name', font=('ariel 12 bold'))
        self.name_l.place(x=0, y=100)

        self.stock_l = Label(master, text='Enter Stock Details', font=('ariel 12 bold'))
        self.stock_l.place(x=0, y=150)

        self.cost_l = Label(master, text='Enter Cost Price', font=('ariel 12 bold'))
        self.cost_l.place(x=0, y=200)

        self.retail_cost_l = Label(master, text='Enter Retail Cost Price', font=('ariel 12 bold'))
        self.retail_cost_l.place(x=0, y=250)

        self.vendor_name_l = Label(master, text='Enter Vendor Name', font=('ariel 12 bold'))
        self.vendor_name_l.place(x=0, y=300)

        self.vendor_num_l = Label(master, text='Enter Vendor Phone Number', font=('ariel 12 bold'))
        self.vendor_num_l.place(x=0, y=350)

        self.tbox_l = Label(master, text='Current Logs', font=('ariel 12 bold'))
        self.tbox_l.place(x=600, y=50)

        #Entries for the window
        self.id_e = Entry(master, width=15, font=('ariel 12 bold'))
        self.id_e.place(x=250, y=50)

        self.name_e = Entry(master, width=15, font=('ariel 12 bold'))
        self.name_e.place(x=250, y=100)

        self.stock_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.stock_e.place(x=250, y=150)

        self.cost_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.cost_e.place(x=250, y=200)

        self.retail_cost_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.retail_cost_e.place(x=250, y=250)

        self.vendor_name_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.vendor_name_e.place(x=250, y=300)

        self.vendor_num_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.vendor_num_e.place(x=250, y=350)


        #Buttons to update the Database
        self.btn_srch_1 = Button(master, text='Search ID', width=10, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.search_db_1)
        self.btn_srch_1.place(x=450, y=50)

        self.btn_srch_2 = Button(master, text='Search Name', width=10, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.search_db_2)
        self.btn_srch_2.place(x=450, y=100)

        self.btn_exit = Button(master, text='Exit', width=10, height=1, bg='brown', fg='white', font=('ariel 12 bold'), command=exit)
        self.btn_exit.place(x=300, y=400)

        self.btn_clear = Button(master, text='Clear fields', width=10, height=1, bg='green', fg='white', font=('ariel 12 bold'), command=self.clear_all)
        self.btn_clear.place(x=480, y=400)

        self.btn_updt = Button(master, text='Update in DB', width=10, height=1, bg='steelblue', fg='white', font=('ariel 12 bold'), command=self.update_db)
        self.btn_updt.place(x=300, y=460)

        #Text box for the logs
        self.tbox = Text(master, width=49, height=25)
        self.tbox.place(x=600, y=80)
        
    def search_db_1(self, *args, **kwargs):
        sql_id = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql_id, (self.id_e.get(), ))
        for r in result:
            self.n1 = r[1] #Item_name
            self.n2 = r[2] #Stock
            self.n3 = r[3] #Cost
            self.n4 = r[4] #Retail_cost
            self.n5 = r[5] #Vendor_name
            self.n6 = r[6] #Vendor_phone_num
        connection.commit()
            #Insert in entries for update
        self.name_e.delete(0,END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0, str(self.n2))

        self.cost_e.delete(0,END)
        self.cost_e.insert(0, str(self.n3))

        self.retail_cost_e.delete(0,END)
        self.retail_cost_e.insert(0, str(self.n4))

        self.vendor_name_e.delete(0,END)
        self.vendor_name_e.insert(0, str(self.n5))

        self.vendor_num_e.delete(0,END)
        self.vendor_num_e.insert(0, str(self.n6))

    def search_db_2(self, *args, **kwargs):
        sql_name = "SELECT * FROM inventory WHERE Item_name=?"
        result = c.execute(sql_name, (self.name_e.get(), ))
        for r in result:
            self.n0 = r[0] #ID
            self.n1 = r[1] #Item_name
            self.n2 = r[2] #Stock
            self.n3 = r[3] #Cost
            self.n4 = r[4] #Retail_cost
            self.n5 = r[5] #Vendor_name
            self.n6 = r[6] #Vendor_phone_num
        connection.commit()
            #Insert in entries for update
        self.id_e.delete(0,END)
        self.id_e.insert(0, str(self.n0))

        self.name_e.delete(0,END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0,END)
        self.stock_e.insert(0, str(self.n2))

        self.cost_e.delete(0,END)
        self.cost_e.insert(0, str(self.n3))

        self.retail_cost_e.delete(0,END)
        self.retail_cost_e.insert(0, str(self.n4))

        self.vendor_name_e.delete(0,END)
        self.vendor_name_e.insert(0, str(self.n5))

        self.vendor_num_e.delete(0,END)
        self.vendor_num_e.insert(0, str(self.n6))

    
    def update_db(self, *args, **kwargs):
        #Update all the values

        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cost_e.get()
        self.u4 = self.retail_cost_e.get()
        self.u5 = self.vendor_name_e.get()
        self.u6 = self.vendor_num_e.get()

        query = "UPDATE inventory SET Item_name=?, Stock=?, Cost=?, Retail_cost=?, Vendor_name=?, Vendor_phone_num=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.id_e.get()))
        connection.commit()
        msgbx.showinfo("Success", "The database has been updated, successfully")
        self.tbox.insert(END, "\nLast updated item was " + str(self.u1))

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cost_e.delete(0,END)
        self.retail_cost_e.delete(0,END)
        self.vendor_name_e.delete(0,END)
        self.vendor_num_e.delete(0,END)
        self.id_e.delete(0,END)

root = Tk()
b = Database_update(root)

root.geometry('1024x512')
root.title('Update the Database')
root.mainloop()