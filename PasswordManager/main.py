from tkinter import *
from tkinter import messagebox
import random
import pyperclip

#PASSWORD GENERATOR#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.delete(0,END)
    password_input.insert(0,password)
    

#SAVE PASSWORD#
def save_password():
    if website_input.get == "" or password_input.get() == "":
        messagebox.showerror(title="Error",message="Missing input fields!")
    else:
        messagebox.showinfo(title="New password",message="New password added.")
        global passwords
        passwords = open('data.txt', 'a+')
        passwords.write(f"Website: {website_input.get()}\nUsername: {emailUsername_input.get()} \nPassword: {password_input.get()}\n---------------\n")
        passwords.close()
        
        website_input.delete(0,END)
        emailUsername_input.delete(0,END)
        password_input.delete(0,END)
    
#UI SETUP#
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

# invisible label to set up grid
invi_label = Label(text="")
invi_label.grid(row=0,column=0)

canvas = Canvas(width=200, height=200,  highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
emailUsername_label = Label(text="Email/Username:")
emailUsername_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

website_input = Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2,sticky="EW")
website_input.focus()
emailUsername_input = Entry(width=35)
emailUsername_input.grid(row=2,column=1,columnspan=2,sticky="EW")
emailUsername_input.insert(0,"miggyalino35@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3,column=1,sticky="EW")

generate_button = Button(text="Generate", width=15, command=generate_password)
generate_button.grid(row=3,column=2,padx=0,pady=0,sticky="EW")
add_button = Button(text="Add", width=35, command=save_password) 
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")


window.mainloop()


