import sqlite3
import hashlib
from tkinter import messagebox
from SystemMODULE import open_back_window


# this function will store user information to a database
# create a connection
connection = sqlite3.connect('userdata.db')
curser = connection.cursor()
# create table on the database if it does not already exist
curser.execute("""
   CREATE TABLE IF NOT EXISTS userdata (
       id INTEGER PRIMARY KEY,
       username VARCHAR(255) NOT NULL,
       password VARCHAR(255) NOT NULL
   )
""")


def _save_to_dataBase(username, password):
    # check if the information stored is not empty
    if username != '' and password != '':
        curser.execute('SELECT username FROM userdata WHERE username = ?', [username])
        if curser.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')
        else:
            # set database variables
            username1, password1 = username, hashlib.sha256(password.encode()).hexdigest()
            # add user to the database
            curser.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username1, password1))
            # update database
            connection.commit()
            messagebox.showinfo('Successful Sign-up', 'Account created successfully\nYou can now Login')
    else:
        messagebox.showerror('Missing Credentials', 'Cannot create account with empty credentials. Try again')


# this function will validate the credentials from the database
def _get_infor_from_database(username, password, App):
    if username != '' and password != '':
        curser.execute('SELECT password FROM userdata WHERE username = ?', [username])
        result = curser.fetchone()
        if result:
            attempted_password_hash = hashlib.sha256(password.encode()).hexdigest() # encode the password
            if attempted_password_hash == result[0]: # check if the encoded password matches the one the database
                open_back_window()
                App.withdraw()
            else:
                messagebox.showerror('Information Verifier', 'Invalid Credentials')
    else:
        messagebox.showerror('Information Verifier', 'User not found. Try again')

