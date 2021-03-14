from tkinter import *
import sqlite3
import tkinter.messagebox as msgbx

connection = sqlite3.connect("F:\Python_Files\Billing Software\Database\store_db.db")
c = connection.cursor()

res = c.execute("SELECT Max(id) from inventory")
for r in res:
    id = r[0]
class Database:
    def __init__(self, master, *args, **kwargs):
        
        self.master = master
        self.heading = Label(master, text='Add to the Database', font=(' ariel 20 bold'), fg='steelblue')
        self.heading.place(x=180, y=0)

        #Labels for the window
        self.name_l = Label(master, text='Enter Product Name', font=('ariel 12 bold'))
        self.name_l.place(x=0, y=50)

        self.stock_l = Label(master, text='Enter Stock Details', font=('ariel 12 bold'))
        self.stock_l.place(x=0, y=100)

        self.cost_l = Label(master, text='Enter Cost Price', font=('ariel 12 bold'))
        self.cost_l.place(x=0, y=150)

        self.retail_cost_l = Label(master, text='Enter Retail Cost Price', font=('ariel 12 bold'))
        self.retail_cost_l.place(x=0, y=200)

        self.vendor_name_l = Label(master, text='Enter Vendor Name', font=('ariel 12 bold'))
        self.vendor_name_l.place(x=0, y=250)

        self.vendor_num_l = Label(master, text='Enter Vendor Phone Number', font=('ariel 12 bold'))
        self.vendor_num_l.place(x=0, y=300)

        self.id_l = Label(master, text='Enter Product ID', font=('ariel 12 bold'))
        self.id_l.place(x=0, y=350)

        self.tbox_l = Label(master, text='Current Logs', font=('ariel 12 bold'))
        self.tbox_l.place(x=600, y=50)

        #Entries for the window
        self.name_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.name_e.place(x=250, y=50)

        self.stock_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.stock_e.place(x=250, y=100)

        self.cost_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.cost_e.place(x=250, y=150)

        self.retail_cost_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.retail_cost_e.place(x=250, y=200)

        self.vendor_name_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.vendor_name_e.place(x=250, y=250)

        self.vendor_num_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.vendor_num_e.place(x=250, y=300)

        self.id_e = Entry(master, width=35, font=('ariel 12 bold'))
        self.id_e.place(x=250, y=350)

        #Buttons to add to the Database
        self.btn_add = Button(master, text='Add to DB', width=10, height=1, bg='steelblue', fg='white', font=('ariel 12 bold'), command=self.get_items)
        self.btn_add.place(x=300, y=400)

        self.btn_clear = Button(master, text='Clear fields', width=10, height=1, bg='green', fg='white', font=('ariel 12 bold'), command=self.clear_all)
        self.btn_clear.place(x=480, y=400)

        self.btn_updt = Button(master, text='Update ID', width=10, height=1, bg='steelblue', fg='white', font=('ariel 12 bold'), command=self.updt_id)
        self.btn_updt.place(x=300, y=460)

        #Text box for the logs
        self.tbox = Text(master, width=49, height=25)
        self.tbox.place(x=600, y=80)
        self.tbox.insert(END, "ID has reached upto: " + str(id))
    
    def get_items(self, *args, **kwargs):
        #Get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cost = self.cost_e.get()
        self.retail_cost = self.retail_cost_e.get()
        self.vendor = self.vendor_name_e.get()
        self.vendor_num = self.vendor_num_e.get()

        #getting dynamic values
        # self.values<...> = <>

        if self.name == '' or self.stock == '' or self.cost == '' or self.retail_cost == '':
            msgbx.showinfo('Error', 'Please fill all the entries')
        else:
            sql = "INSERT INTO inventory (Item_name, Stock, Cost, Retail_cost, Vendor_name, Vendor_phone_num) VALUES(?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cost, self.retail_cost, self.vendor, self.vendor_num))
            connection.commit()
            msgbx.showinfo('Success', 'Values added to the Database, successfully')
            #insert in text box
            self.tbox.insert(END, "\n\nInserted " + str(self.name) + " into the Database with code " + str(self.id_e.get()))

    def clear_all(self, *args, **kwargs):
        self.name_e.delete(0,END)
        self.stock_e.delete(0,END)
        self.cost_e.delete(0,END)
        self.retail_cost_e.delete(0,END)
        self.vendor_name_e.delete(0,END)
        self.vendor_num_e.delete(0,END)
        self.id_e.delete(0,END)

    def updt_id(self, *args, **kwargs):
        res = c.execute("SELECT Max(id) from inventory")
        for r in res:
            id = r[0]
        self.tbox.insert(END, "\n\nID has reached upto: " + str(id))

root = Tk()
b = Database(root)

root.geometry('1024x512')
root.title('Add to the Database')
root.mainloop()