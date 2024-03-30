import customtkinter as ctk
from tkinter import messagebox


# function to create a new window
def open_back_window():
    App = ctk.CTkToplevel()
    App.title("Back-End")
    App.geometry('800x600')
    App.resizable(False, False)
