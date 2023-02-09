import json
from tkinter import *

from canvas import tk
from helpers import clean_screen
from products import render_products


def login(username, pword):
    with open("databases/user_credentials_db.txt", "r") as file:
        data = file.readlines()
        for line in data:
            name, password = line[:-1].split(", ")
            if name == username and pword == password:
                with open("databases/current_user.txt", "w") as file:
                    file.write(name)
                render_products()
                return

        render_login(error="Invalid username or password")


def register(**user):
    user.update({"products": []})
    with open("databases/users.txt", "a", newline='\n') as file:
        file.write(json.dumps(user))
        file.write('\n')
    with open("databases/user_credentials_db.txt", "a", newline='') as file:
        file.write(f"{user['username']}, {user['password']}\n")
    render_login()


def render_login(error=None):
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)

    if error is not None:
        Label(tk, text="Invalid username or password").grid(row=3, column=0)
    Button(tk, text="Enter", bg="green", command=lambda: login(username.get(), password.get())).grid(row=2, column=0)


def render_register():
    clean_screen()
    username = Entry(tk)
    username.grid(row=0, column=0)
    password = Entry(tk)
    password.grid(row=1, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=0)
    # Make validations for names lenght and username to be unique and with no special chars
    Button(
        tk,
        text="Register", bg="green",
        command=lambda: register(username=username.get(), password=password.get(), first_name=first_name.get(),
                                 last_name=last_name.get())).grid(row=4,
                                                                  column=0)


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="white", command=render_login).grid(row=0, column=0)
    Button(tk, text="Register", bg="yellow", fg="black", command=render_register).grid(row=0, column=1, sticky="e")
