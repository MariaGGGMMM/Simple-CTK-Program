from customtkinter import *

def button_callback():
    request = request.get("http://127.0.0.1:5000/denis")

app = CTk()
app.geometry("400x150")

button = CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

requestLable = CTkLabel(app, text="hello")
requestLable.pack(padx=20, pady=30)


app.mainloop()