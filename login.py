#Login.py
import tkinter as tk
import sqlite3
from tkinter import messagebox
import share_incident

# Function to create database and table
def create_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    conn.commit()
    conn.close()

# Function to check if username already exists
def check_existing_username(username):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Function to handle sign-up
def sign_up():
    username = username_entry.get()
    password = password_entry.get()

    if check_existing_username(username):
        messagebox.showerror("Error", "Username already exists!")
    else:
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Sign-up successful!")

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        share_incident.si()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Main window
root = tk.Tk()
root.title("Sign-up and Login")

# Create database table
create_table()

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=25, pady=15, sticky="e")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=25, pady=15)

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=25, pady=5, sticky="e")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=25, pady=5)

# Sign-up button
signup_button = tk.Button(root, text="Sign-up", command=sign_up)
signup_button.grid(row=2, column=0, columnspan=2, pady=10)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()