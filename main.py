from customtkinter import *

app = CTk ()
app.geometry('800x600')

def foo():
    print('ты куку')

title = CTkLabel(master = app, text = 'моя програма')
title.pack(side = LEFT)

submit = CTkButton(master = app, text = 'submit',command = foo)
submit.pack(side = LEFT)

submit1 = CTkButton(master = app, text = 'submit')
submit1.pack(side = RIGHT)

submit2 = CTkButton(master = app, text = 'submit')
submit2.pack(side = TOP)

submit3 = CTkButton(master = app, text = 'submit')
submit3.pack(side = BOTTOM)




app.mainloop()