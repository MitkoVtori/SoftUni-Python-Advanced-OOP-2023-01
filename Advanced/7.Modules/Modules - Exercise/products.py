from helpers import clean_screen
from canvas import tk
from tkinter import *
from tkinter.ttk import *
import json
import os
base_folder = os.path.dirname(__file__)


def render_products():
    clean_screen()
    row = 0
    col = 0
    max = 4
    with open("databases/products.txt", "r") as file:
        products = file.readlines()
        for line in products:
            product = json.loads(line[:-1] if "\n" in line else line)
            if col == max:
                row = 0
                col = 0
                row += 1

            Label(tk, text=product["name"]).grid(row=row + 1, column=col, pady=2)

            from PIL import Image, ImageTk

            # Create the PIL image object
            image = Image.open(os.path.join(os.path.join(base_folder, "images"), product["img_path"]))
            image = image.resize((100, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=row + 2, column=col)

            Label(tk, text=product["count"]).grid(row=row + 3, column=col, pady=2)
            button = Button(tk, text=f"Buy {product['id']}")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=row + 4, column=col)
            col += 1


def update_product_quantity(product_id):
    with open("databases/products.txt", "r+") as file:
        products = file.readlines()
        file.seek(0)
        for line in products:
            current_product = json.loads(line[:-1])
            if current_product["id"] == product_id:
                current_product["count"] -= 1
            file.write(json.dumps(current_product) + "\n")


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    username = None
    with open("databases/current_user.txt", "r", ) as file:
        username = file.readline()
    if username:
        with open("databases/users.txt", "r+", newline="\n") as users_file:
            data = users_file.readlines()
            users_file.seek(0)
            for line in data:
                current_user = json.loads(line[:-1])
                if current_user["username"] == username:
                    current_user["products"].append(product_id)
                users_file.write(json.dumps(current_user) + "\n")
        update_product_quantity(product_id)
        render_products()