from customtkinter import *
from PIL import Image

# create app
app = CTk()
app.geometry('800x600')
app.resizable(False, False)
# image file
image = Image.open('8fdc3b8300604ed2af0e86142dc47443.png')
# creating the image object
background_image = CTkImage(
    image,
    size=(800, 580)
)
# creating the label
image_label = CTkLabel(
    app,
    text='',
    image=background_image
)
image_label.pack()
# creating a frame
frame = CTkFrame(
    app,
    width=390,
    height=580,
    border_width=30,
    border_color='#FFFFF7',
    corner_radius=8,
    fg_color='#FFFFF7',
)
frame.place(x=410, y=0)
# creating header
header = CTkLabel(
    master=frame,
    text='Welcome Back!',
    text_color='purple',
    font=('CComic Sans MS', 30, 'bold'),
)
header.place(x=25, y=84)
footer = CTkLabel(
    master=frame,
    text='sign in to your account',
    text_color='#808080',
    font=('CComic Sans MS', 15, 'bold')
)
footer.place(x=26, y=124)
# creating email label
email_image = Image.open('postcard.png')
image_email = CTkImage(
    email_image,
    size=(20, 20)
)
email = CTkLabel(
    master=frame,
    text='',
    image=image_email,
    width=5,
    height=5,
)
email.place(x=25, y=202)
email_label = CTkLabel(
    master=frame,
    text='Email:',
    text_color='purple',
    font=('Calibri', 15, 'bold')
)
email_label.place(x=50, y=198)
# placing an entr to receive input
entry_email = CTkEntry(
    master=frame,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple'
)
entry_email.place(x=25, y=225)
# creating password section
pas_image = Image.open('4585570.png')
pass_image = CTkImage(
    pas_image,
    size=(20, 20)
)
password = CTkLabel(
    master=frame,
    text='',
    image=pass_image
)
password.place(x=25, y=285)
password_label = CTkLabel(
    master=frame,
    text='Password:',
    text_color='purple',
    font=('Calibri', 15, 'bold')
)
password_label.place(x=50, y=287)
entry_password = CTkEntry(
    master=frame,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple'
)
entry_password.place(x=25, y=315)
# creating the login button
login = Image.open('google.png')
Log = CTkImage(
    login
)
Login = CTkButton(
    master=frame,
    text='Login',
    text_color='white',
    fg_color='purple',
    width=300,
    height=35,
    font=('Calibri', 15, 'bold')
)
Login.place(x=25, y=400)
google = CTkButton(
    master=frame,
    text='Continue With Google',
    text_color='purple',
    fg_color='#d3d3d3',
    width=300,
    height=35,
    image=Log,
    font=('Calibri', 13, 'bold'),
    hover_color='#C0C0C0'
)
google.place(x=25, y=450)
# App loop
app.mainloop()
