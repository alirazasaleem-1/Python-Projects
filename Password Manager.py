# Password Manager
from cryptography.fernet import Fernet 
import getpass 
import os
file = "key.key"
path = os.path.join(os.getcwd(), file)
password_path = os.path.join(os.getcwd(), "passwords.txt")

# ------ Key Handling ------
def load_key():
    if not os.path.exists(path):
        key = Fernet.generate_key()
        with open(path, "wb") as f:
            f.write(key)
    else:
        with open(path, "rb") as f:
            key = f.read()
    return key

key = load_key()
fernet = Fernet(key)

# ----- Save Passwords -----
def add_password():
    site = input("🌐 Site Name: ").strip()
    username = input("🧑 Enter Username: ").strip()
    password = getpass.getpass("🔑 Enter the Password: ").strip()
    if not site or not username or not password:
        print("❌ All fields are required. ")
        return 
    
    data = f"{site} | {username} | {password}"
    encrypted = fernet.encrypt(data.encode())

    with open(password_path, "ab") as f:
        f.write(encrypted + b"\n")

    print("✅ Password Saved Successfully.")

# ----- View Passwords -----
def view_passwords():
    
    if not os.path.exists(password_path):
        print("⚠ No Passwords Saved Yet. ")
        return 
    
    print("\n🔒 Stored Passwords: \n")

    with open(password_path, "rb") as f:
        for line in f:
            try:
                decrypt = fernet.decrypt(line.strip()).decode()
                print(decrypt)
            except Exception as e:
                print(f"❌ Error reading a line. Error: {e} ")

# ----- Search Password -----
def search_password():
    if not os.path.exists(password_path):
        print("⚠ No Passwords Saved Yet. ")
        return 
    
    found = False 
    site_search = input("🔍 Enter site to search: ").strip()
    with open (password_path, "rb") as f:
        for line in f:
            try:
                decrypted = fernet.decrypt(line.strip()).decode()

                parts = decrypted.split(" | ")
                if len(parts) < 3:
                    continue 
                site = parts[0]
                if site_search.lower() == site.lower():
                    print(decrypted)
                    found = True
            except:
                    continue 
        if not found:
             print("❌ No Match Found. ")

# ----- MENU -----
def menu():
    while True:
        print("\n=============================")
        print("🔐 Password Manager CLI")
        print("=============================")
        print("1. Add Password ")
        print("2. View Password ")
        print("3. Search Password ")
        print("4. Exit ")

        choice = input("Choose: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("Good Bye Bro! ")
            break 
        else:
            print("❌ Invalid Option. ")

# ------------ Run -------------
menu()