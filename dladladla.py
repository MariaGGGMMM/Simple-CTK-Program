from customtkinter import *

app = CTk ()

app.geometry('400x400')

def Calculate():
    Miles = float(MilesEntry.get())
    Kilometers = Miles * 1.60934
    statusLabel.configure(text = str(Kilometers))

FirstLabel =CTkLabel (master = app, text = 'is equal to')
FirstLabel.grid(column = 1,row = 2)

MilesLabel =CTkLabel (master = app, text = 'Miles')
MilesLabel.grid(column = 3,row = 1)

KelometersLabel =CTkLabel (master = app, text = 'Km')
KelometersLabel.grid(column = 3,row = 2)

statusLabel =CTkLabel (master = app, text = "0")
statusLabel.grid(column = 2,row = 2,)

MilesEntry = CTkEntry (master = app, width = 40)
MilesEntry.grid (column = 2, row = 1)

CalculateBtn = CTkButton (master = app, text ='Calculate', width = 280, command = Calculate)
CalculateBtn.grid (column = 2, row = 4, columnspan = 2, pady = 5)


app.mainloop()