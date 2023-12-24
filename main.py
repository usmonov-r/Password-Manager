from tkinter import *
from tkinter import messagebox
import random
import pyperclip


#===============PASSWORD GENERATOR

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    print(nr_numbers)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password) # for coping  automatically  to clipboard

# ==============SAVE PASSWORD
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You don't leave filed empty")
    else:
        isok = messagebox.askokcancel(
            title="Verify you data",
            message=f"Website: {website}\nEmail: {email}\nPassword: {password}\n Is data correct?")
        if isok:# isok returns boolen
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                file.close()
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            messagebox.showinfo(title="Info", message="You data is saved")
#================ UI SETUP

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

#Labels

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:" )
password_label.grid(row=3, column=0)


#Enties

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
website_entry.focus() # is for focus on that entry when we run code first time
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com") # insert for setting default text in entry and index for position
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)




#Buttons

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_password = Button(text="Add Password", width=36, command=save_password)
add_password.grid(row=4,column=1, columnspan=2)





window.mainloop()






