from json import loads, dump
from tkinter import Button, Entry
from buying_page import display_products
from canvas import root, frame
from helpers import clean_screen, get_password_hash


def get_users_data():
    info_data = []

    with open("db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def render_entry():
    register_btn = Button(
        root,
        text="Register",
        bg="green",  # background color
        fg="white",  # font color
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=login,
    )

    frame.create_window(350, 260, window=register_btn)
    frame.create_window(350, 320, window=login_btn)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 100, window=password_box)

    frame.create_window(250, 150, window=logging_btn)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(160, 200, text="Invalid username or password!", fill="red")


def check_logging():
    info_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == user_username and password == user_password:
            return True

    return False


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name:")
    frame.create_text(100, 100, text="Last name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(200, 50, window=first_name_box)
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        command=registration,
    )

    frame.create_window(300, 250, window=registration_btn)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": get_password_hash(password_box.get()),
    }

    if check_registration(info_dict):
        with open("db/users_information.txt", "a") as users_file:
            dump(info_dict, users_file)
            users_file.write('\n')
            display_products()


def check_registration(info):
    for el in info.values():
        if not el.strip():
            frame.create_text(
                300,
                300,
                text="We are missing some information!",
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")

    info_data = get_users_data()

    for record in info_data:
        if record["username"] == info["username"]:
            frame.create_text(
                300,
                300,
                text="User with this username already exists!",
                fill="red",
                tag="error",
            )

            return False

    frame.delete("error")

    return True


def check_if_login_is_fulfilled(event):
    info = {
        "username": username_box.get(),
        "password": password_box.get(),
    }

    for el in info.values():
        if not el.strip():
            logging_btn["state"] = "disabled"
            break
    else:
        logging_btn["state"] = "normal"


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")  # let the user choose

logging_btn = Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    command=logging,
)

logging_btn["state"] = "disabled" # options: active, normal, disabled

root.bind('<KeyRelease>', check_if_login_is_fulfilled)
