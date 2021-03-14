'''import tkinter as tk 
from tkinter import ttk 
  
# Creating tkinter window 
window = tk.Tk() 
window.geometry('350x250') 
# Label 
ttk.Label(window, text = "Select the Month :",  
        font = ("Times New Roman", 10)).grid(column = 0,  
        row = 15, padx = 10, pady = 25) 
  
n = tk.StringVar() 
monthchoosen = ttk.Combobox(window, width = 27,  
                            textvariable = n) 
  
# Adding combobox drop down list 
monthchoosen['values'] = (' January',  
                          ' February', 
                          ' March', 
                          ' April', 
                          ' May', 
                          ' June',  
                          ' July',  
                          ' August',  
                          ' September',  
                          ' October',  
                          ' November',  
                          ' December') 
  
monthchoosen.grid(column = 1, row = 15) 
  
# Shows february as a default value 
monthchoosen.current()  
window.mainloop() '''

'''from tkinter import *
import sqlite3

connection = sqlite3.connect("F:\Python_Files\Billing Software\Database\store_db.db")
c = connection.cursor()

# Function for checking the 
# key pressed and updating 
# the listbox 
def checkkey(event): 
	value = event.widget.get() 
	#print(value) 
	# get data from l 
	if value == '': 
		data = l 
	else: 
		data = [] 
		for item in l: 
			if value.lower() in item.lower(): 
				data.append(item)				 

	# update data in listbox 
	update(data) 


def update(data): 
	
	# clear previous data 
	lb.delete(0, 'end') 

	# put new data 
	for item in data: 
		lb.insert('end', item) 

# Driver code
q = "SELECT Item_name FROM inventory"
r = c.execute(q,)
l = tuple(r)


root = Tk() 

#creating text box 
e = Entry(root) 
e.pack() 
e.bind('<KeyRelease>', checkkey) 

#creating list box 
lb = Listbox(root) 
lb.pack() 
update(l) 

root.mainloop()'''


from tkinter import *
import re
import sqlite3

connection = sqlite3.connect("F:\Python_Files\Billing Software\Database\store_db.db")
c = connection.cursor()

q = "SELECT Item_name FROM inventory"
r = list(c.execute(q))
print(r)
for item in r:
	print(re.sub(r" ?\([^)]+\)", "", item))

'''lista = ['a', 'actions', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets', 'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field', 'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind', 'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part', 'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless', 'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you']


class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
        
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

if __name__ == '__main__':
    root = Tk()

    entry = AutocompleteEntry(lista, root)
    entry.grid(row=0, column=0)
    Button(text='nothing').grid(row=1, column=0)
    Button(text='nothing').grid(row=2, column=0)
    Button(text='nothing').grid(row=3, column=0)

    root.mainloop()'''