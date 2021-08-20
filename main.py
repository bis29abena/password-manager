from tkinter import *
from tkinter import messagebox
from random import choices, sample
import pyperclip
import json


# ---------------------------- SEARCH -------------------------------------------#
def search_website():
    # Getting the value of the web textbox
    web = website_textbox.get().title()
    # Opening the json file and saving it into var dict call sites
    if web == "":
        messagebox.showinfo(title="ERROR", message="Please type in a website")
    else:
        try:
            with open("data.json", "r") as search_site:
                sites = json.load(search_site)
        except FileNotFoundError:
            messagebox.showinfo(title="ERROR", message="No Data File Found")
        else:
            # Searching through the dict to find if the site exists
            for key, value in sites.items():
                if web in key:
                    email = value["email"]
                    password = value["password"]

                    messagebox.showinfo(title=web, message=f"Email: {email}\nPassword: {password}")

                    break
                else:
                    messagebox.showinfo(title=web, message="Web not in the list yet please add")
                    break


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly Selecting elements in a list using the choices function
    # And add the number samples it should bring out
    letters_ = choices(letters, k=4)
    numbers_ = choices(numbers, k=4)
    symbols_ = choices(symbols, k=4)

    # adding the selected randomly picked integers into a single string
    password_gen = letters_ + symbols_ + numbers_

    # Sampling the single string into the password shuffle
    password_shuffle = ''.join(sample(password_gen, len(password_gen)))

    password_textbox.insert(0, password_shuffle)
    # Using pyperclip for easy copying and pasting
    pyperclip.copy(password_shuffle)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # Getting the text in the text box
    website = website_textbox.get().title()
    email = email_textbox.get()
    password = password_textbox.get()
    file = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Error", message="Please don't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {email}\nPassword: {password}\nAre you sure about the details")
        if is_ok:
            try:
                # Reading the file
                with open("data.json", "r") as files:
                    data = json.load(files)
            except FileNotFoundError:
                # Creating a json file
                with open("data.json", "w") as files:
                    json.dump(file, files, indent=4)
            else:
                # Updating a json file
                data.update(file)
                with open("data.json", "w") as files:
                    json.dump(data, files, indent=4)
            finally:
                website_textbox.delete(first=0, last=END)
                password_textbox.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #

# Setting the up the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Creating the canvas
canvas = Canvas(width=200, height=200)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(row=0, column=1)

# Creating the website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
# website_label.config(pady=10)

# Creating the Website textbox
website_textbox = Entry(width=23)
website_textbox.focus()
website_textbox.grid(row=1, column=1)

# Creating the email label
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
# email_label.config(pady=10)

# Creating the email textbox
email_textbox = Entry(width=39)
email_textbox.insert(0, "bismark@gmail.com")
email_textbox.grid(row=2, column=1, columnspan=2)

# Creating the password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Creating the password textbox
password_textbox = Entry(width=23)
password_textbox.grid(row=3, column=1)

# Creating the generate password button
generate_button = Button(text="Generate Password", command=generate_password, width=12)
generate_button.grid(row=3, column=2)

# Creating the Add button
add_button = Button(text="Add", command=add_password)
add_button.config(width=36)
add_button.grid(row=4, column=1, columnspan=2)

# Creating search button
search_button = Button(text="Search", command=search_website, width=11)
search_button.grid(row=1, column=2)

window.mainloop()
