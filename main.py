from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import codecs
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():

    input_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_letters = [choice(letters) for _ in range(randint(4, 7))]
    password_numbers = [choice(numbers) for _ in range(randint(4, 7))]

    password_list = password_letters + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = input_website.get()
    try:
        with codecs.open("data.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
            if website in data:
                info = data[website]
                messagebox.showinfo(title=website, message=f"Username:{info['username']}\n Password:{info['password']}")
            elif website not in data:
                messagebox.showerror(title="Password not found", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title=website, message="Please do not leave any fields empty!")
    else:
        try:
            with codecs.open("data.json", "r", encoding="utf-8") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with codecs.open("data.json", "w", encoding="utf-8") as data_file:
                json.dump(new_data, data_file, indent=4, ensure_ascii=False)
        else:
            data.update(new_data)

            with codecs.open("data.json", "w", encoding="utf-8") as data_file:
                json.dump(data, data_file, indent=4, ensure_ascii=False)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

lable_website = Label(text="Website:")
lable_username = Label(text="Email/Username:")
lable_password = Label(text="Password:")
lable_website.grid(column=0, row=1)
lable_username.grid(column=0, row=2)
lable_password.grid(column=0, row=3)

input_website = Entry(width=28)
input_website.focus()
input_username = Entry(width=45)
input_password = Entry(width=28)
input_website.grid(column=1, row=1)
input_username.grid(column=1, row=2, columnspan=2)
input_password.grid(column=1, row=3)
input_username.insert(0, "bryanlin16899@outlook.com")

button_gen = Button(text="Generate Password", command=password_generator)
button_add = Button(text="Add", width=45, command=save)
button_search = Button(text="Search", width=15, command=find_password)
button_gen.grid(column=2, row=3)
button_add.grid(column=1, row=4, columnspan=2)
button_search.grid(column=2, row=1)


window.mainloop()
