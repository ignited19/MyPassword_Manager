from tkinter import *
import PasswordManager as PM
import pyperclip


print("Let's Rock!!")
PasswordManagement = PM.PasswordManager()

def startPasswordSave():
    website = Website_Entry.get()
    newPassword = Password_Entry.get()
    email = User_Entry.get()

    PasswordManagement.SavePassword(website,email,newPassword)

def startPasswordGeneration():
    newPassword = PasswordManagement.GeneratePassword()
    Password_Entry.insert(0,newPassword)
    pyperclip.copy(Password_Entry.get())


#GUI
session = Tk()
session.title("Password Manager")
session.config(padx=20, pady=20)
canvas = Canvas(height=200,width=200)
background_img = PhotoImage(file="Resources/img/logo.png")
canvas.create_image(100, 100, image=background_img)
canvas.grid(row=0, column=1)

#Form
Website_Label = Label(text="Website")
Website_Label.grid(row=1, column=0 )
User_Label = Label(text="Email/Username")
User_Label.grid(row=2, column=0)
Password_Label = Label(text="Password")
Password_Label.grid(row=3, column=0)

#Entries
Website_Entry = Entry(width=45) #35
Website_Entry.grid(row=1, column=1, columnspan=3)
User_Entry = Entry(width=45) #34
User_Entry.grid(row=2, column=1, columnspan=3)
Password_Entry = Entry(width=27) #21
Password_Entry.grid(row=3, column=1)

#Buttons
Button_GeneratePass = Button(text="Generate Password", width=14, command=startPasswordGeneration)
Button_GeneratePass.grid(row=3, column=2, columnspan=2)
Button_Add = Button(text="Add", width=36, command=startPasswordSave)
Button_Add.grid(row=4, column=1, columnspan=3)


session.mainloop()

