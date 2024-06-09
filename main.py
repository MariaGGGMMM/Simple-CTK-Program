from customtkinter import *
from func import*
from password_generator import PasswordGenerator
from PIL import Image


pwo = PasswordGenerator()


app = CTk ()
app.geometry('800x600')


# title = CTkLabel(master = app, text = 'моя програма')
# title.pack(side = LEFT)

# submit = CTkButton(master = app, text = 'submit',command = lambda : foo('Mary','010811'))
# submit.pack(side = LEFT)

# submit1 = CTkButton(master = app, text = 'submit')
# submit1.pack(side = RIGHT)

# submit2 = CTkButton(master = app, text = 'submit')
# submit2.pack(side = TOP)

# submit3 = CTkButton(master = app, text = 'submit')
# submit3.pack(side = BOTTOM)

def generate():
    password = pwo.generate()

    
    passwordEntry.delete(0)
    passwordEntry.insert(0,password)
             




def submit():
    password = passwordEntry.get()
    email = emailEntry.get()
    websit = websiteEntry.get()

    statusLabel.configure (text = 'well done :3')



    if email == 'Maria':
        print('hallo vnvv')

logo = Image.open("Simple-CTK-Program/kundurin.png")
image = CTkImage(light_image = logo,dark_image = logo, size = (300,300))
imageLabel = CTkLabel(master = app, image = image)
imageLabel.pack(side = TOP)



container = CTkFrame (master = app)
container.pack(side=TOP)

websiteLabel =CTkLabel (master = container, text = 'Website :')
websiteLabel.grid(column = 1,row = 1)

emailLabel =CTkLabel (master = container, text = 'email/username :')
emailLabel.grid(column = 1,row = 2)

passwordLabel =CTkLabel (master = container, text = 'password :')
passwordLabel.grid(column = 1,row = 3)

websiteEntry = CTkEntry (master = container, width = 280)
websiteEntry.grid (column = 2, row = 1, columnspan = 2,padx = 5, pady = 5)

emailEntry = CTkEntry (master = container, width = 280)
emailEntry.grid (column = 2, row = 2, columnspan = 2,padx = 5, pady = 5)

passwordEntry = CTkEntry (master = container, width = 130)
passwordEntry.grid (column = 2, row = 3,padx =5,pady = 5)

generateBtn= CTkButton (master = container, text ='generate', command = generate)
generateBtn.grid (column = 3, row = 3, padx = 5, pady = 5)

submitBtn = CTkButton (master = container, text ='submit', width = 280, command = submit)
submitBtn.grid (column = 2, row = 4, columnspan = 2, pady = 5)

statusLabel =CTkLabel (master = container, text = "i'll kill you if you don't fill this in!!!")
statusLabel.grid(column = 2,row = 5, padx = 5, pady = 5, columnspan = 2)



app.mainloop()