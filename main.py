from tkinter import *
from tkinter import messagebox
import ttkbootstrap
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    my_password = "".join(password_list)

    password_entry.insert(0, my_password)
    pyperclip.copy(my_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as my_file:
                data = json.load(my_file)
        except FileNotFoundError:
            with open("data.json", "w") as my_file:
                json.dump(data, my_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as my_file:
                json.dump(data, my_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = ttkbootstrap.Window()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)

# widgets
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_entry = Entry(width=21)
website_entry.focus()
username_entry = Entry(width=35)
username_entry.insert(0, "tayfun@gmail.com")
password_entry = Entry(width=21)
generate_button = Button(text="Generate Password", command=password_generator)
add_button = Button(text="Add", width=36, command=save)
search_button = Button(text="Search", width=13, command=find_password)

# grid
website_label.grid(column=0, row=1, sticky=W)
username_label.grid(column=0, row=2, sticky=W)
password_label.grid(column=0, row=3, sticky=W)
website_entry.grid(column=1, row=1, sticky=W)
username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry.grid(column=1, row=3, sticky=W)
generate_button.grid(column=2, row=3)
search_button.grid(column=2, row=1)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)
canvas.grid(column=1, row=0, sticky=W)





window.mainloop()