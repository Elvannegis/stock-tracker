"""
stock-tracker v1
Student: Elvan Negiş (251478063)

V1 GÖREV LİSTESİ:
# TASK 1: list komutunu tamamla - tüm ürünleri listele
# TASK 2: remove komutunu tamamla - stok miktarını azalt
# TASK 3: search komutunu tamamla - ürün ara

Scope: init, add, list, remove, search komutları çalışıyor.
Limitations: lowstock henüz implement edilmedi.
"""
import sys
import os
from datetime import date

# --- Fonksiyonlar ---

def initialize():
    if os.path.exists(".stocktracker"):
        return "Already initialized"
    os.mkdir(".stocktracker")
    f = open(".stocktracker/products.dat", "w")
    f.close()
    return "Initialized empty stock-tracker in .stocktracker/"

def add_product(name, quantity, price):
    if not os.path.exists(".stocktracker"):
        return "Not initialized. Run: python stocktracker.py init"
    try:
        quantity = int(quantity)
        price = float(price)
    except:
        return "Invalid quantity or price"
    f = open(".stocktracker/products.dat", "r")
    content = f.read()
    f.close()
    product_id = content.count("\n") + 1
    f = open(".stocktracker/products.dat", "a")
    today = date.today().strftime("%Y-%m-%d")
    f.write(f"{product_id}|{name}|{quantity}|{price}|{today}|1\n")
    f.close()
    return f"Added product #{product_id}: {name}"

# TASK 1: list komutu
def list_products():
    if not os.path.exists(".stocktracker"):
        return "Not initialized. Run: python stocktracker.py init"
    f = open(".stocktracker/products.dat", "r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        return "No products found."
    result = ""
    for line in lines:
        parts = line.strip().split("|")
        if parts[5] == "1":
            result += f"[{parts[0]}] {parts[1]} | Quantity: {parts[2]} | Price: {parts[3]}\n"
    return result.strip()

# TASK 2: remove komutu
def remove_product(name, quantity):
    if not os.path.exists(".stocktracker"):
        return "Not initialized. Run: python stocktracker.py init"
    try:
        quantity = int(quantity)
    except:
        return "Invalid quantity"
    f = open(".stocktracker/products.dat", "r")
    lines = f.readlines()
    f.close()
    found = False
    new_lines = []
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == name:
            found = True
            new_qty = int(parts[2]) - quantity
            if new_qty < 0:
                return "Not enough stock"
            parts[2] = str(new_qty)
            new_lines.append("|".join(parts) + "\n")
        else:
            new_lines.append(line)
    if not found:
        return "Product not found"
    f = open(".stocktracker/products.dat", "w")
    f.writelines(new_lines)
    f.close()
    return f"Quantity decreased for: {name}"

# TASK 3: search komutu
def search_product(name):
    if not os.path.exists(".stocktracker"):
        return "Not initialized. Run: python stocktracker.py init"
    f = open(".stocktracker/products.dat", "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        parts = line.strip().split("|")
        if parts[1] == name:
            return f"[{parts[0]}] {parts[1]} | Quantity: {parts[2]} | Price: {parts[3]}"
    return "Product not found"

def not_implemented(command_name):
    return f"Command '{command_name}' will be implemented in future weeks."

# --- Ana Program ---

if len(sys.argv) < 2:
    print("Usage: python stocktracker.py <command> [args]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 5:
        print("Usage: python stocktracker.py add <name> <quantity> <price>")
    else:
        print(add_product(sys.argv[2], sys.argv[3], sys.argv[4]))
elif sys.argv[1] == "list":
    print(list_products())
elif sys.argv[1] == "remove":
    if len(sys.argv) < 4:
        print("Usage: python stocktracker.py remove <name> <quantity>")
    else:
        print(remove_product(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
        print("Usage: python stocktracker.py search <name>")
    else:
        print(search_product(sys.argv[2]))
elif sys.argv[1] in ["lowstock", "status"]:
    print(not_implemented(sys.argv[1]))
else:
    print(f"Unknown command: {sys.argv[1]}")
