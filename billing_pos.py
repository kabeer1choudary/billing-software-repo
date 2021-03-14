from tkinter import *
import sqlite3
import datetime
from time import strftime
import tkinter.messagebox as msgbx

connection = sqlite3.connect("F:\Python_Files\Billing Software\Database\store_db.db")
c = connection.cursor()

#date
date = datetime.datetime.now().date()

#variable
v = StringVar

#temp list values
product_id=[]
product_name=[]
product_price=[]
product_quantity=[]
product_cpu=[]

class Application:
    def __init__(self, master, *args, **kwargs):
        self.master = master

        #setting up frames
        self.left = Frame(master, width=600, height=512, bg='white')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=524, height=512, bg='steelblue')
        self.right.pack(side=RIGHT)

        #setting up components
        self.heading = Label(self.left, text='Billing Software', font=('ariel 30 bold'), fg='steelblue', bg='white')
        self.heading.place(x=10, y=20)
        #setting up date and time
        self.time_l = Label(self.right, font=('ariel 12 bold'), fg='white', bg='steelblue')
        self.time_l.place(x=180, y=20)

        self.date_l = Label(self.right, text=str(date), font=('ariel 12 bold'), fg='white', bg='steelblue')
        self.date_l.place(x=10, y=20)

        #function for time stramp
        def time_stramp(): 
            string = strftime('%H:%M:%S %p') 
            self.time_l.config(text = string) 
            self.time_l.after(1000, time_stramp)
        time_stramp()

        #setting up invoice table
        self.right_products_l = Label(self.right, text='Products', font=('ariel 15 bold'), fg='white', bg='steelblue')
        self.right_products_l.place(x=0,y=60)

        self.right_cost_per_unit_l = Label(self.right, text='CostPU', font=('ariel 15 bold'), fg='white', bg='steelblue')
        self.right_cost_per_unit_l.place(x=100,y=60)

        self.right_quantity_l = Label(self.right, text='Qty', font=('ariel 15 bold'), fg='white', bg='steelblue')
        self.right_quantity_l.place(x=200,y=60)

        self.right_amount_l = Label(self.right, text='Amount', font=('ariel 15 bold'), fg='white', bg='steelblue')
        self.right_amount_l.place(x=280,y=60)

        #setting up bill table
        self.left_id_l = Label(self.left, text='Enter product ID', font=('ariel 15 bold'), bg='white')
        self.left_id_l.place(x=0,y=90)

        self.left_id_e = Entry(self.left, width=15, font=('ariel 15 bold'), bg='lightblue')
        self.left_id_e.place(x=200,y=90)

        self.left_name_l = Label(self.left, text='Enter product name', font=('ariel 15 bold'), bg='white')
        self.left_name_l.place(x=0,y=150)

        self.left_name_e = Entry(self.left, width=15, font=('ariel 15 bold'), bg='lightblue')
        self.left_name_e.place(x=200,y=150)
        self.left_name_e.focus()

        #setting up total label
        self.total_l = Label(self.right, text='Total', font=('ariel 20 bold'), fg='white', bg='steelblue')
        self.total_l.place(x=0,y=450)
    
        #setting up search button
        self.btn_srch_1 = Button(self.left, text='Search ID', width=10, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.get_from_id)
        self.btn_srch_1.place(x=450, y=90)

        self.btn_srch_2 = Button(self.left, text='Search Name', width=10, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.get_from_name)
        self.btn_srch_2.place(x=450, y=150)

        #setting up product update labels
        self.left_product_name_l = Label(self.left, text='', font=('ariel 15 bold'), bg='white')
        self.left_product_name_l.place(x=0, y=200)

        self.left_product_price_l = Label(self.left, text='', font=('ariel 15 bold'), bg='white')
        self.left_product_price_l.place(x=0, y=240)

    def get_from_id(self, *args, **kwargs):
        self.get_id = self.left_id_e.get()
        #get product details and fill on labels
        query = "SELECT Item_name, Retail_cost FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_name_1 = self.r[0]
            self.get_r_cost_1 = self.r[1]
        self.left_product_name_l.configure(text="Product's Name: " + str(self.get_name_1))
        self.left_product_price_l.configure(text="Product's Price: " + str(self.get_r_cost_1))

    def get_from_name(self, *args, **kwargs):
        self.get_name = self.left_name_e.get()
        #get product details and fill on labels
        query = "SELECT ID, Stock, Retail_cost FROM inventory WHERE Item_name=?"
        result = c.execute(query, (self.get_name, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_stock = self.r[1]
            self.get_r_cost_2 = self.r[2]
        if self.get_name == '':
            msgbx.showwarning('Warning', 'Enter a valid product name')
        else:
            self.left_product_name_l.configure(text="Product's Name: " + str(self.get_name))
            self.left_product_price_l.configure(text="Product's Price: " + str(self.get_r_cost_2))
        
        #setting up quantity labels
        self.left_quantity_l = Label(self.left, text='Enter the Quantity', font=('ariel 15 bold'), bg='white')
        self.left_quantity_l.place(x=0, y=300)

        self.left_quantity_e = Entry(self.left, width=15, font=('ariel 15 bold'), bg='lightblue')
        self.left_quantity_e.place(x=200,y=300)
        self.left_quantity_e.focus()

        #setting up add to cart button
        self.add_to_cart_btn = Button(self.left, text='Add to Cart', width=10, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.add_to_cart)
        self.add_to_cart_btn.place(x=450, y=300)

        #setting up Amount given label and calculate change button
        self.left_amount_given_l = Label(self.left, text='Amount Given', font=('ariel 15 bold'), bg='white')
        self.left_amount_given_l.place(x=0,y=350)

        self.left_amount_given_e = Entry(self.left, width=15, font=('ariel 15 bold'), bg='lightblue')
        self.left_amount_given_e.place(x=200,y=350)

        #calculate change button
        self.calc_chge_btn = Button(self.left, text='Calculate Change', width=13, height=1, bg='orange', fg='white', font=('ariel 12 bold'), command=self.get_change_fun)
        self.calc_chge_btn.place(x=450, y=350)

        #generate bill button
        self.gen_bill_btn = Button(self.left, text='Generate Bill', width=55, height=1, bg='Red', fg='white', font=('ariel 12 bold'), command=exit)
        self.gen_bill_btn.place(x=10, y=450)

    def add_to_cart(self, *args, **kwargs):
        #get the quantity and value from database
        self.quantity_value = int(self.left_quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            msgbx.showinfo('Error', 'Product shortage')
        else:
            #price calculation
            self.final_price = float(self.quantity_value)*float(self.get_r_cost_2)
            product_id.append(self.get_id)
            product_name.append(self.get_name)
            product_cpu.append(self.get_r_cost_2)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)

            #addding items

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.bill in product_name:
                self.tempname = Label(self.right, text=str(product_name[self.counter]), font=('ariel 10 bold'), bg='steelblue', fg='white')
                self.tempname.place(x=0, y=self.y_index)

                self.tempcpu = Label(self.right, text=str(product_cpu[self.counter]), font=('ariel 10 bold'), bg='steelblue', fg='white')
                self.tempcpu.place(x=100, y=self.y_index)

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('ariel 10 bold'), bg='steelblue', fg='white')
                self.tempqt.place(x=200, y=self.y_index)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('ariel 10 bold'), bg='steelblue', fg='white')
                self.tempprice.place(x=280, y=self.y_index)

                self.y_index += 20
                self.counter += 1

                #total calculation
                self.total_l.configure(text='Total: Rs. '+ str(sum(product_price)))

                #cleaning up the fields
                self.left_quantity_l.place_forget()
                self.left_quantity_e.place_forget()
                self.left_product_name_l.configure(text='')
                self.left_product_price_l.configure(text='')

                #adding focus to the entry search box
                self.left_name_e.focus()
                self.left_name_e.delete(0, END)

    def get_change_fun(self, *args, **kwargs):
        #get the amount given and total
        self.balance_amnt = float(self.left_amount_given_e.get()) - float(sum(product_price))

        #balance amount
        self.balance_amnt_l = Label(self.left, text='Balance to give Rs.'+str(self.balance_amnt), font=('ariel 15 bold'), bg='white')
        self.balance_amnt_l.place(x=0, y=400)

    def generate_bill(self, *args, **kwargs):
        #updating the stocks

        self.new_stock = int(self.get_stock) - int(self.quantity_value)
        sql = "UPDATE inventory SET Stock=? WHERE ID=?"
        c.execute(sql,(self.new_stock, self.get_id))
        connection.commit()


root = Tk()
b = Application(root)
root.geometry('1024x512')
root.title('Billing Software')
root.mainloop()