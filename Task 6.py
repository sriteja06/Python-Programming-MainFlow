import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('billing_software.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        price REAL NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        contact TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER NOT NULL,
                        product_id INTEGER NOT NULL,
                        quantity INTEGER NOT NULL,
                        total REAL NOT NULL,
                        FOREIGN KEY(customer_id) REFERENCES customers(id),
                        FOREIGN KEY(product_id) REFERENCES products(id))''')
    conn.commit()
    conn.close()

# Functions for CRUD operations
def add_product():
    name = product_name_var.get()
    price = product_price_var.get()
    if name and price:
        conn = sqlite3.connect('billing_software.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        conn.commit()
        conn.close()
        product_name_var.set("")
        product_price_var.set("")
        update_product_list()
    else:
        messagebox.showerror("Error", "All fields are required")

def update_product_list():
    product_list.delete(*product_list.get_children())
    conn = sqlite3.connect('billing_software.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    for row in rows:
        product_list.insert('', tk.END, values=row)
    conn.close()

def add_customer():
    name = customer_name_var.get()
    contact = customer_contact_var.get()
    if name and contact:
        conn = sqlite3.connect('billing_software.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customers (name, contact) VALUES (?, ?)", (name, contact))
        conn.commit()
        conn.close()
        customer_name_var.set("")
        customer_contact_var.set("")
        update_customer_list()
    else:
        messagebox.showerror("Error", "All fields are required")

def update_customer_list():
    customer_list.delete(*customer_list.get_children())
    conn = sqlite3.connect('billing_software.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        customer_list.insert('', tk.END, values=row)
    conn.close()

# GUI setup
def create_gui():
    global product_name_var, product_price_var, customer_name_var, customer_contact_var
    global product_list, customer_list

    root = tk.Tk()
    root.title("Billing Software")
    root.geometry("800x600")

    # Product Section
    product_frame = ttk.LabelFrame(root, text="Add Product")
    product_frame.pack(fill="x", padx=10, pady=5)

    ttk.Label(product_frame, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
    product_name_var = tk.StringVar()
    ttk.Entry(product_frame, textvariable=product_name_var).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(product_frame, text="Price:").grid(row=0, column=2, padx=5, pady=5)
    product_price_var = tk.DoubleVar()
    ttk.Entry(product_frame, textvariable=product_price_var).grid(row=0, column=3, padx=5, pady=5)

    ttk.Button(product_frame, text="Add Product", command=add_product).grid(row=0, column=4, padx=5, pady=5)

    product_list_frame = ttk.LabelFrame(root, text="Product List")
    product_list_frame.pack(fill="both", expand=True, padx=10, pady=5)

    product_list = ttk.Treeview(product_list_frame, columns=("ID", "Name", "Price"), show="headings")
    product_list.heading("ID", text="ID")
    product_list.heading("Name", text="Name")
    product_list.heading("Price", text="Price")
    product_list.pack(fill="both", expand=True)

    # Customer Section
    customer_frame = ttk.LabelFrame(root, text="Add Customer")
    customer_frame.pack(fill="x", padx=10, pady=5)

    ttk.Label(customer_frame, text="Customer Name:").grid(row=0, column=0, padx=5, pady=5)
    customer_name_var = tk.StringVar()
    ttk.Entry(customer_frame, textvariable=customer_name_var).grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(customer_frame, text="Contact:").grid(row=0, column=2, padx=5, pady=5)
    customer_contact_var = tk.StringVar()
    ttk.Entry(customer_frame, textvariable=customer_contact_var).grid(row=0, column=3, padx=5, pady=5)

    ttk.Button(customer_frame, text="Add Customer", command=add_customer).grid(row=0, column=4, padx=5, pady=5)

    customer_list_frame = ttk.LabelFrame(root, text="Customer List")
    customer_list_frame.pack(fill="both", expand=True, padx=10, pady=5)

    customer_list = ttk.Treeview(customer_list_frame, columns=("ID", "Name", "Contact"), show="headings")
    customer_list.heading("ID", text="ID")
    customer_list.heading("Name", text="Name")
    customer_list.heading("Contact", text="Contact")
    customer_list.pack(fill="both", expand=True)

    update_product_list()
    update_customer_list()

    root.mainloop()

if __name__ == "__main__":
    setup_database()
    create_gui()