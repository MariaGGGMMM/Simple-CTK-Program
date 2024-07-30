from customtkinter import *
from PIL import Image
 
LARGEFONT =("Verdana", 35)
  
class tkinterApp(CTk):
     
    
    def __init__(self, *args, **kwargs): 
         
        
        CTk.__init__(self, *args, **kwargs)
         
        
        container = CTkFrame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        
        self.frames = {}  
  
        
        for F in (StartPicture,Picture1, Picture2 ):
  
            frame = F(container, self)
  
            
            self.frames[F] = frame 
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPicture)
  
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
  

  
class StartPicture(CTkFrame):
    def __init__(self, parent, controller): 
        CTkFrame.__init__(self, parent)
         
        label = CTkLabel(self, text ="StartPicture", font = LARGEFONT)
         
        
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
  
        button1 =CTkButton(self, text ="Picture 1",
        command = lambda : controller.show_frame(Picture1))
     
        
        button1.grid(row = 1, column = 1)
  
        
        button2 = CTkButton(self, text ="Picture 2",
        command = lambda : controller.show_frame(Picture2))
     
        
        button2.grid(row = 2, column = 1)
  
          
  

class Picture1(CTkFrame):
     
    def __init__(self, parent, controller):
         
        CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text ="Picture 1", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
        logo = Image.open("image.png")
        image = CTkImage(light_image = logo,dark_image = logo, size = (300,300))
        ImageLabel = CTkLabel(master = self, image = image,text = '')
        ImageLabel.grid(row = 3, column =3)
        
        button1 = CTkButton(self, text ="StartPicture",
                            command = lambda : controller.show_frame(StartPicture))
     
        
        button1.grid(row = 6, column = 1, padx = 10, pady = 10)
  
        
        button2 = CTkButton(self, text ="Picture 2",
                            command = lambda : controller.show_frame(Picture2))
     
        
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
class Picture2(CTkFrame): 
    def __init__(self, parent, controller):
        CTkFrame.__init__(self, parent)
        label = CTkLabel(self, text ="Picture 2", font = LARGEFONT)
        label.grid(row = 1, column = 1, padx = 1, pady = 1)
        logo = Image.open("yey.png")
        image = CTkImage(light_image = logo,dark_image = logo, size = (300,300))
        ImageLabel = CTkLabel(master = self, image = image,text = '')
        ImageLabel.grid(row = 2, column = 1, padx = 0, pady = 0)
        
        button1 = CTkButton(self, text ="Picture 1",
                            command = lambda : controller.show_frame(Picture1))
     
        
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        
        button2 = CTkButton(self, text ="StartPicture",
                            command = lambda : controller.show_frame(StartPicture))
     
        
        button2.grid(row = 2, column = 1)

        
app = tkinterApp()
app.mainloop()



