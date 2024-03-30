from customtkinter import *
from PIL import Image
from savingdata import _save_to_dataBase, _get_infor_from_database

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
# making tabs for sign in and sign up
Tabs = CTkTabview(
    app,
    width=400,
    height=568,
    text_color='black',
    segmented_button_fg_color='purple',
    segmented_button_selected_color='purple',
    segmented_button_selected_hover_color='black',
    segmented_button_unselected_color='white',
    segmented_button_unselected_hover_color='black',
    bg_color='white',
    fg_color='white',
)
Tabs.place(x=395, y=2)
# creating a frame
frame = CTkFrame(
    Tabs.add('Sign-in'),
    width=390,
    height=510,
    border_width=30,
    border_color='#FFFFF7',
    corner_radius=8,
    fg_color='#FFFFF7',
)
frame.place(x=0, y=0)
# creating header
header = CTkLabel(
    master=frame,
    text='Welcome Back!',
    text_color='purple',
    font=('Comic Sans MS', 30, 'bold'),
)
header.place(x=25, y=24)
footer = CTkLabel(
    master=frame,
    text='sign in to your account',
    text_color='#808080',
    font=('Comic Sans MS', 15, 'bold')
)
footer.place(x=26, y=69)
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
email.place(x=25, y=150)
email_label = CTkLabel(
    master=frame,
    text='Email:',
    text_color='purple',
    font=('Comic Sans MS', 15, 'bold')
)
email_label.place(x=50, y=148)
# placing an entr to receive input
entry_email = CTkEntry(
    master=frame,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple',
    font=('Comic Sans MS', 14)
)
entry_email.place(x=25, y=178)
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
password.place(x=25, y=240)
password_label = CTkLabel(
    master=frame,
    text='Password:',
    text_color='purple',
    font=('Comic Sans MS', 15, 'bold')
)
password_label.place(x=50, y=244)
entry_password = CTkEntry(
    master=frame,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple',
    font=('Comic Sans MS', 14),
    show="*"
)
entry_password.place(x=25, y=275)
# creating the login button
login = Image.open('google.png')
Log = CTkImage(
    login
)


# function to get  the text typed password and username
def Information():
    username = entry_email.get().strip()
    password__ = entry_password.get().strip()
    _get_infor_from_database(username,password__, app)


Login = CTkButton(
    master=frame,
    text='Login',
    text_color='white',
    fg_color='purple',
    width=300,
    height=35,
    font=('Comic Sans MS', 15, 'bold'),
    command=Information
)
Login.place(x=25, y=350)
google = CTkButton(
    master=frame,
    text='Continue With Google',
    text_color='purple',
    fg_color='#d3d3d3',
    width=300,
    height=35,
    image=Log,
    font=('Comic Sans MS', 13, 'bold'),
    hover_color='#C0C0C0'
)
google.place(x=25, y=420)

# creating the sign-up frame
frame2 = CTkFrame(
    Tabs.add('Sign-up'),
    width=390,
    height=510,
    border_width=30,
    border_color='#FFFFF7',
    corner_radius=8,
    fg_color='#FFFFF7',
)
frame2.place(x=0, y=0)
welcome = CTkLabel(
    master=frame2,
    text='Welcome!',
    text_color='purple',
    font=('Comic Sans MS', 30, 'bold'),
)
welcome.place(x=25, y=24)
footer2 = CTkLabel(
    master=frame2,
    text='sign up a new account',
    text_color='#808080',
    font=('Comic Sans MS', 15, 'bold')
)
footer2.place(x=26, y=69)
# creating email label
email_image2 = Image.open('postcard.png')
image_email2 = CTkImage(
    email_image2,
    size=(20, 20)
)
email2 = CTkLabel(
    master=frame2,
    text='',
    image=image_email2,
    width=5,
    height=5,
)
email2.place(x=25, y=150)
email_label2 = CTkLabel(
    master=frame2,
    text='Email:',
    text_color='purple',
    font=('Comic Sans MS', 15, 'bold')
)
email_label2.place(x=50, y=148)
# placing an entr to receive input
entry_email2 = CTkEntry(
    master=frame2,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple',
    font=('Comic Sans MS', 14)
)
entry_email2.place(x=25, y=178)
# creating password section
pas_image2 = Image.open('4585570.png')
pass_image2 = CTkImage(
    pas_image2,
    size=(20, 20)
)
password2 = CTkLabel(
    master=frame2,
    text='',
    image=pass_image2
)
password2.place(x=25, y=240)
password_label2 = CTkLabel(
    master=frame2,
    text='Password:',
    text_color='purple',
    font=('Comic Sans MS', 15, 'bold')
)
password_label2.place(x=50, y=244)
entry_password2 = CTkEntry(
    master=frame2,
    width=300,
    height=35,
    corner_radius=5,
    fg_color='#F2F3F5',
    border_width=2,
    border_color='purple',
    text_color='purple',
    font=('Comic Sans MS', 14),
)
entry_password2.place(x=25, y=275)
# creating the login button
login2 = Image.open('google.png')
Log2 = CTkImage(
    login2
)


# function to get  the text typed password and username
def save_information():
    username = entry_email2.get().strip()
    password__ = entry_password2.get().strip()
    _save_to_dataBase(username, password__)


Login2 = CTkButton(
    master=frame2,
    text='Sign-up',
    text_color='white',
    fg_color='purple',
    width=300,
    height=35,
    font=('Comic Sans MS', 15, 'bold'),
    command=save_information
)
Login2.place(x=25, y=350)
google2 = CTkButton(
    master=frame2,
    text='Continue With Google',
    text_color='purple',
    fg_color='#d3d3d3',
    width=300,
    height=35,
    image=Log2,
    font=('Comic Sans MS', 13, 'bold'),
    hover_color='#C0C0C0'
)
google2.place(x=25, y=420)
# App loop
app.mainloop()
