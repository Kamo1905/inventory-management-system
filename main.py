import tkinter as tk 
from tkinter import messagebox
import database 

database.connect()

def add_product():
    name = name_entry.get()

    try:
        price = price_entry.get()
        quantity = quantity_entry.get()
    except ValueError:
        messagebox.showerror("Error", "Price must be a number and quantity must be an integer")
        return

    if name == "":
        messagebox.showerror("Error", "Name is required")
        return
    
    database.add_product(name, price, quantity)
    messagebox.showinfo("Success", "Product added successfully")
    clear_entries()
    display_products()

def display_products():
    listbox.delete(0, tk.END)
    for product in database.get_products():
        listbox.insert(tk.END, product)

def delete_product():
    selected =listbox.get(tk.ACTIVE)
    if not selected:
        return
    
    database.delete_product(selected[0])
    display_products()

def update_products():
    selected = listbox.get(tk.ACTIVE)
    if not selected:
        return
    
    database.update_product(
        selected[0],
        name_entry.get(),
        float(price_entry.get()),
        int(quantity_entry.get())
    )

    display_products()

def select_product(event):
    selected = listbox.get(tk.ACTIVE)

    name_entry.delete(0, tk.END)
    name_entry.insert(tk.END, selected[1])
    
    price_entry.delete(0, tk.END)
    price_entry.insert(tk.END, selected[2])

    quantity_entry.delete(0, tk.END)
    quantity_entry.insert(tk.END, selected[3])


def clear_entries():
    name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def search_product():
    listbox.delete(0, tk.END)
    results = database.search_products(name_entry.get())

    for products in results:
        listbox.insert(tk.END, products)


# GUI Window
root = tk.Tk()
root.title("Kamo's Inventory Management System")

# Labels
tk.Label(root, text="Name").grid(row=0, column=0)
tk.Label(root, text="Price").grid(row=0, column=1)
tk.Label(root, text="Quantity").grid(row=0, column=2)

# Entries
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=0)

price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1, column=2)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.grid(row=2, column=0, columnspan=3)
listbox.bind("<<ListboxSelect>>", select_product)

# Buttons
tk.Button(root, text="Add", command=add_product).grid(row=3, column=0)
tk.Button(root, text="Update", command=update_products).grid(row=3, column=1)
tk.Button(root, text="Delete", command=delete_product).grid(row=3, column=2)
tk.Button(root, text="Search", command=search_product).grid(row=4, column=1)
tk.Button(root, text="Clear", command=clear_entries).grid(row=4, column = 0)

# Run app
display_products()
root.mainloop()