from customtkinter import *
import db
import db_func
app = CTk ()
app.geometry('800x600')

container = CTkFrame (master = app)
container.pack(side=TOP)

def submit():
    name = NameEntry.get()
    surname = SurnameEntry.get()
    date = DateEntry.get(), DateEntry2.get(), DateEntry3.get()
    
    db_func.insert(db.cursor, surname, date, name)

    

    




ShopLabel =CTkLabel (master = container, text = 'Cats shop')
ShopLabel.grid(column = 1,row = 1,pady = 5)

NameLabel =CTkLabel (master = container, text = 'name')
NameLabel.grid(column = 1,row = 2,pady = 5)

SurnameLabel =CTkLabel (master = container, text = 'surname')
SurnameLabel.grid(column = 1,row = 3,pady = 5) 

DateLabel =CTkLabel (master = container, text = 'date of birth :')
DateLabel.grid(column = 1,row = 4,pady = 5)

NameEntry = CTkEntry (master = container, width = 130)
NameEntry.grid (column = 2, row = 2,pady = 5, columnspan =2)

SurnameEntry = CTkEntry (master = container, width = 130)
SurnameEntry.grid (column = 2, row = 3,pady = 5, columnspan = 2)

DateEntry = CTkEntry (master = container, width = 70)
DateEntry.grid (column = 1, row = 5,pady = 5)

DateEntry2 = CTkEntry (master = container, width = 70)
DateEntry2.grid (column = 2, row = 5,pady = 5)

DateEntry3 = CTkEntry (master = container, width = 70)
DateEntry3.grid (column = 3, row = 5,pady = 5, columnspan = 2)

submitBtn = CTkButton (master = container, text ='submit', width = 80,command = submit )
submitBtn.grid (column = 2, row = 6, pady = 5)



app.mainloop()