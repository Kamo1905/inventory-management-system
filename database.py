import sqlite3

def connect():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def add_product(name, price, quantity):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))

    conn.commit()
    conn.close()

def get_products():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    conn.close()
    return rows

def delete_product(product_id):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()

def update_product(product_id, name, price, quantity):
    conn= sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE products
    SET name=?, price=?, quantity=?
    WHERE id=?                    
""", (name, price, quantity, product_id))
    
    conn.commit()
    conn.close()

def search_products(name):
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    conn.close()
    return rows 