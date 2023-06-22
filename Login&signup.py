import re
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import Tk, Frame, Button, Label
from Application_Classes import User
from sql import con
from sql import c
from sql import insert_user

import tkinter.messagebox
import tkfontchooser
import ctypes as ct
import sqlite3


import re
import tkinter.messagebox


root = Tk()
root.geometry("1040x820")
root.eval("tk::PlaceWindow . center")
root.config()

iconimg = PhotoImage(file="NBA NEWS logo.png")
root.iconphoto(False,iconimg)
root.title("NBA NEWS")

font = tkfontchooser.Font(family="Mesquite Std")

def clear_widgets(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()



backgroundpic = Image.open("loading screen 8.png")
resized = backgroundpic.resize((1040, 820), Image.Resampling.LANCZOS)
newbkpic = ImageTk.PhotoImage(resized)

bklable = Label(root, image=newbkpic)
bklable.place(x=0, y=0, relwidth=1, relheight=1)

lgb = PhotoImage(file="login button.png")
sub = PhotoImage(file="signupbutton2.png")

abl = PhotoImage(file="arrowbuttonleft.png")
abr = PhotoImage(file="arrowbuttonright.png")

# atlantic division teams logos
celticsicon = PhotoImage(file="celticslogo.png")
netsicon = PhotoImage(file="netslogo.png")
knickssicon = PhotoImage(file="knickslogo.png")
philisicon = PhotoImage(file="phililogo.png")
raptorsicon = PhotoImage(file="raptorslogo.png")

# central division teams logos
bullsicon = PhotoImage(file="bullslogo.png")
cavsicon = PhotoImage(file="cavslogo.png")
pistonsicon = PhotoImage(file="pistonslogo.png")
pacersicon = PhotoImage(file="pacerslogo.png")
bucksicon = PhotoImage(file="buckslogo.png")


#southeast division teams logos
hawksicon = PhotoImage(file="hawkslogo.png")
hornetsicon = PhotoImage(file="hornetslogo.png")
heaticon = PhotoImage(file="heatlogo.png")
magicicon = PhotoImage(file="magiclogo.png")
wizardsicon = PhotoImage(file="wizardslogo.png")

#northwest division teams logo
nuggetsicon = PhotoImage(file="nuggetslogo.png")
timberwolvesicon = PhotoImage(file="timberwolveslogo.png")
okcicon = PhotoImage(file="okclogo.png")
blazersicon = PhotoImage(file="blazerlogo.png")
jazzicon = PhotoImage(file="jazzlogo.png")

#pacific division teams logo
warriorsicon = PhotoImage(file="warriorslogo.png")
clippersicon = PhotoImage(file="clipperslogo.png")
lakersicon = PhotoImage(file="lakerslogo.png")
sunsicon = PhotoImage(file="sunslogo.png")
kingsicon = PhotoImage(file="kingslogo.png")

#southwest division teams logos
mavericksicon = PhotoImage(file="magiclogo.png")
rocketsicon = PhotoImage(file="rocketslogo.png")
grizzliesicon = PhotoImage(file="grizzlieslogo.png")
pelicansicon = PhotoImage(file="pelicanslogo.png")
spursicon = PhotoImage(file="spurslogo.png")


def load_atlantic_divisionframe():

    clear_widgets(signup_frame)
    atlantic_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(atlantic_divisionframe, text="ATLANTIC DIVISION", font=(font, 15), bg="black", fg="orange")

    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda :load_southwest_divisionframe())


    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda :
                              load_central_divisionframe())

    backbutton = Button(atlantic_divisionframe, text="⚫ BACK ⚫", bg="black", fg="#E65C06", borderwidth=0, command= lambda : load_signup_frame())

    celtics_button = Button(atlantic_divisionframe, image=celticsicon, bg="black", borderwidth=0, activebackground="white")
    nets_button = Button(atlantic_divisionframe, image=netsicon, bg="black", borderwidth=0, activebackground="white")
    knicks_button = Button(atlantic_divisionframe, image=knickssicon, bg="black", borderwidth=0, activebackground="white")
    philis_button = Button(atlantic_divisionframe, image=philisicon, bg="black", borderwidth=0, activebackground="white")
    raptors_button = Button(atlantic_divisionframe, image=raptorsicon, bg="black", borderwidth=0, activebackground="white")

    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)

    division_name.grid(row=0, columnspan=3, pady=15)

    celtics_button.grid(row=1, column=1)
    nets_button.grid(row=1, column=2)
    knicks_button.grid(row=2, column=1)
    philis_button.grid(row=2, column=2)
    raptors_button.grid(row=3, columnspan=3)
    backbutton.grid(row=4, columnspan=3)

    atlantic_divisionframe.place(x=350, y=50, anchor=NW)


def load_central_divisionframe():

    clear_widgets(atlantic_divisionframe)
    central_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(central_divisionframe, text="CENTRAL DIVISION", font=(font, 15), bg="black", fg="orange")

    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda:
                             load_atlantic_divisionframe())

    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda:
                              load_southeast_divisionframe())

    bulls_button = Button(central_divisionframe, image=bullsicon, bg="black", borderwidth=0, activebackground="white")
    cavs_button = Button(central_divisionframe, image=cavsicon, bg="black", borderwidth=0, activebackground="white")
    pistons_button = Button(central_divisionframe, image=pistonsicon, bg="black", borderwidth=0, activebackground="white")
    pacers_button = Button(central_divisionframe, image=pacersicon, bg="black", borderwidth=0, activebackground="white")
    bucks_button = Button(central_divisionframe, image=bucksicon, bg="black", borderwidth=0, activebackground="white")

    backbutton = Button(central_divisionframe, text="⚫ BACK ⚫", bg="black", fg="#E65C06", borderwidth=0, command= lambda : load_signup_frame())

    backbutton.grid(row=4, columnspan=3)

    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)
    division_name.grid(row=0, columnspan=3, pady=15)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)

    bulls_button.grid(row=1, column=1)
    cavs_button.grid(row=1, column=2)
    pistons_button.grid(row=2, column=1)
    pacers_button.grid(row=2, column=2)
    bucks_button.grid(row=3, columnspan=3)



    central_divisionframe.place(x=350, y=50, anchor=NW)


def load_southeast_divisionframe():

    clear_widgets(signup_frame)
    southeast_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(southeast_divisionframe, text="SOUTHEAST DIVISION", font=(font, 15), bg="black", fg="orange")

    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda:
                             load_central_divisionframe())

    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda:
                              load_northwest_divisionframe())

    hawks_button = Button(southeast_divisionframe, image=hawksicon, bg="black", borderwidth=0, activebackground="white")
    hornets_button = Button(southeast_divisionframe, image=hornetsicon, bg="black", borderwidth=0, activebackground="white")
    heat_button = Button(southeast_divisionframe, image=heaticon, bg="black", borderwidth=0, activebackground="white")
    magic_button = Button(southeast_divisionframe, image=magicicon, bg="black", borderwidth=0, activebackground="white")
    wizards_button = Button(southeast_divisionframe, image=wizardsicon, bg="black", borderwidth=0, activebackground="white")


    backbutton = Button(southeast_divisionframe, text="⚫ BACK ⚫", bg="black", fg="#E65C06", borderwidth=0, command= lambda : [load_signup_frame(),
                                                                                                                             clear_widgets(southeast_divisionframe),
                                                                                                                             southeast_divisionframe.destroy(),
                                                                                                                             CFT_label.destroy(),
                                                                                                                             arrowbuttonright.destroy(),
                                                                                                                             arrowbuttonleft.destroy()])

    backbutton.grid(row=4, columnspan=3)


    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)
    division_name.grid(row=0, columnspan=3, pady=15)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)

    hawks_button.grid(row=1, column=1)
    hornets_button.grid(row=1, column=2)
    heat_button.grid(row=2, column=1)
    magic_button.grid(row=2, column=2)
    wizards_button.grid(row=3, columnspan=3)
    backbutton.grid(row=4, columnspan=3)

    southeast_divisionframe.place(x=350, y=50, anchor=NW)


def load_northwest_divisionframe():

    clear_widgets(signup_frame)
    northwest_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(northwest_divisionframe, text="NORTHWEST DIVISION", font=(font, 15), bg="black", fg="orange")


    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda:
                             load_southwest_divisionframe())

    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda:
                              load_pacific_divisionframe())

    nuggets_button = Button(northwest_divisionframe, image=nuggetsicon, bg="black", borderwidth=0, activebackground="white")
    timberwolves_button = Button(northwest_divisionframe, image=timberwolvesicon, bg="black", borderwidth=0, activebackground="white")
    thunder_button = Button(northwest_divisionframe, image=okcicon, bg="black", borderwidth=0, activebackground="white")
    blazers_button = Button(northwest_divisionframe, image=blazersicon, bg="black", borderwidth=0, activebackground="white")
    jazz_button = Button(northwest_divisionframe, image=jazzicon, bg="black", borderwidth=0, activebackground="white")


    backbutton = Button(northwest_divisionframe,
                        text="⚫ BACK ⚫",
                        bg="black", fg="#E65C06", borderwidth=0,
                        command=lambda : [load_signup_frame(),
                        clear_widgets(northwest_divisionframe),
                        northwest_divisionframe.destroy(),
                        CFT_label.destroy(),
                        arrowbuttonright.destroy(),
                        arrowbuttonleft.destroy()])

    backbutton.grid(row=4, columnspan=3)

    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)
    division_name.grid(row=0, columnspan=3, pady=15)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)

    nuggets_button.grid(row=1, column=1)
    timberwolves_button.grid(row=1, column=2)
    thunder_button.grid(row=2, column=1)
    blazers_button.grid(row=2, column=2)
    jazz_button.grid(row=3, columnspan=3)

    northwest_divisionframe.place(x=350, y=50, anchor=NW)


def load_pacific_divisionframe():

    clear_widgets(signup_frame)
    pacific_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(pacific_divisionframe, text="PACIFIC DIVISION", font=(font, 15), bg="black", fg="orange")


    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda:
                             load_northwest_divisionframe())

    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda:
                              load_southwest_divisionframe())

    warriors_button = Button(pacific_divisionframe, image=warriorsicon, bg="black", borderwidth=0, activebackground="white")
    clippers_button = Button(pacific_divisionframe, image=clippersicon, bg="black", borderwidth=0, activebackground="white")
    lakers_button = Button(pacific_divisionframe, image=lakersicon, bg="black", borderwidth=0, activebackground="white")
    suns_button = Button(pacific_divisionframe, image=sunsicon, bg="black", borderwidth=0, activebackground="white")
    kings_button = Button(pacific_divisionframe, image=kingsicon, bg="black", borderwidth=0, activebackground="white")

    backbutton = Button(pacific_divisionframe,
                        text="⚫ BACK ⚫",
                        bg="black", fg="#E65C06", borderwidth=0,
                        command=lambda : [load_signup_frame(),
                        clear_widgets(pacific_divisionframe),
                        pacific_divisionframe.destroy(),
                        CFT_label.destroy(),
                        arrowbuttonright.destroy(),
                        arrowbuttonleft.destroy()])

    backbutton.grid(row=4, columnspan=3)


    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)
    division_name.grid(row=0, columnspan=3, pady=15)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)

    warriors_button.grid(row=1, column=1)
    clippers_button.grid(row=1, column=2)
    lakers_button.grid(row=2, column=1)
    suns_button.grid(row=2, column=2)
    kings_button.grid(row=3, columnspan=3)

    pacific_divisionframe.place(x=350, y=50, anchor=NW)


def load_southwest_divisionframe():

    clear_widgets(signup_frame)
    southwest_divisionframe.tkraise()

    CFT_label = Label(root, text="Choose Your Favourite Team:", font=(font, 30), bg="black", fg="orange")
    division_name = Label(southwest_divisionframe, text="SOUTHWEST DIVISION", font=(font, 15), bg="black", fg="orange")

    arrowbuttonleft = Button(root,
                             image=abl,
                             bg="black",
                             activebackground="black",
                             borderwidth=0,
                             command=lambda:
                             load_pacific_divisionframe())

    arrowbuttonright = Button(root,
                              image=abr,
                              bg="black",
                              activebackground="black",
                              borderwidth=0,
                              command=lambda:
                              load_atlantic_divisionframe())

    mavericks_button = Button(southwest_divisionframe, image=mavericksicon, bg="black", borderwidth=0, activebackground="white")
    rockets_button = Button(southwest_divisionframe, image=rocketsicon, bg="black", borderwidth=0, activebackground="white")
    grizzlies_button = Button(southwest_divisionframe, image=grizzliesicon, bg="black", borderwidth=0, activebackground="white")
    pelicans_button = Button(southwest_divisionframe, image=pelicansicon, bg="black", borderwidth=0, activebackground="white")
    spurs_button = Button(southwest_divisionframe, image=spursicon, bg="black", borderwidth=0, activebackground="white")


    backbutton = Button(southwest_divisionframe,
                        text="⚫ BACK ⚫",
                        bg="black", fg="#E65C06", borderwidth=0,
                        command=lambda : [load_signup_frame(),
                        clear_widgets(southwest_divisionframe),
                        southwest_divisionframe.destroy(),
                        CFT_label.destroy(),
                        arrowbuttonright.destroy(),
                        arrowbuttonleft.destroy()])

    backbutton.grid(row=4, columnspan=3)


    CFT_label.grid(row=0, columnspan=3, padx=300, pady=10)
    division_name.grid(row=0, columnspan=3, pady=15)

    arrowbuttonleft.place(x=200, y=200)
    arrowbuttonright.place(x=800, y=200)


    mavericks_button.grid(row=1, column=1)
    rockets_button.grid(row=1, column=2)
    grizzlies_button.grid(row=2, column=1)
    pelicans_button.grid(row=2, column=2)
    spurs_button.grid(row=3, columnspan=3)

    southwest_divisionframe.place(x=350, y=50, anchor=NW)


def password_email_validator(pw, rpw, email, name, username):

    if len(pw) < 5:
        tkinter.messagebox.showinfo(title=f" '{pw}' Too short", message="Password too short, password must be more that 6 characters long")
        password_email_validator()

    elif not re.search('[!"£$%^&*()<>,._¬-]', pw):
        tkinter.messagebox.showinfo(title="Password to weak", message="Password too weak, add symbol to password")
        password_email_validator()

    elif not re.search('[1234567890]', pw):
        tkinter.messagebox.showinfo(title="Password to weak", message="Password too weak, add numbers to password")
        password_email_validator()

    elif not re.search('[ABCDEFGHIJKLMNOPQRSTUVWXYZ]', pw):
        tkinter.messagebox.showinfo(title="Password too weak", message="Password too weak, add upper case letters to your password")
        password_email_validator()

    elif rpw != pw:
        tkinter.messagebox.showinfo(title="Passwords dont match", message="The passwords you have entered do not match")
        password_email_validator()

    elif not re.search('@', email):
        tkinter.messagebox.showinfo(title="Invalid Email", message="Email address is invalid")
        password_email_validator()

    elif not re.search('.com' or '.co.uk', email):
        tkinter.messagebox.showinfo(title="Invalid Email", message="Email address is invalid")
        password_email_validator()

    else:

        tkinter.messagebox.showinfo(title="Password Created", message="Password Valid")
        load_atlantic_divisionframe()

        con = sqlite3.connect('classes.db')
        c = con.cursor()

        name = str(name)
        email = str(email)
        username = str(username)
        password = str(pw)


        def insert_user(n,e,u,p):
            with con:
                c.execute("INSERT INTO Users VALUES (:first, :email, :username, :password )",
                          {'first': name, 'email': email, 'username': username,
                           'password': password})
                con.commit()

        insert_user(name,email,username,password)


def load_login_frame():


    clear_widgets(frame1)
    login_frame.tkraise()

    usernamelabel = Label(login_frame, text="Enter Username: ", bg="black", fg="#E65C06", font=(font, 15))
    username_entry = Entry(login_frame, width=40, borderwidth=0)

    passwordlabel = Label(login_frame, text="Enter Password: ", bg="black", fg="#E65C06", font=(font, 15))
    password_entry = Entry(login_frame, width=40, borderwidth=0)

    loginbutton =Button(
        login_frame,
        text="⚫ Log In ⚫",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0)

    backbutton =Button(
        login_frame,
        text="Back",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0,
        command=lambda: [load_frame1(), clear_widgets(login_frame)])

    usernamelabel.grid(row=0, column=0)
    username_entry.grid(row=0, column=1)

    passwordlabel.grid(row=1, column=0)
    password_entry.grid(row=1, column=1)

    loginbutton.grid(row=2, columnspan=3, pady=10)
    backbutton.grid(row=3, columnspan=3, pady=0)


def load_signup_frame():

    clear_widgets(frame1)
    signup_frame.tkraise()

    namelabel = Label(signup_frame, text="Name: ", bg="black", fg="#E65C06", font=(font, 15))
    user_name = Entry(signup_frame, width=40, borderwidth=0)

    emaillabel = Label(signup_frame, text="Enter email: ", bg="black", fg="#E65C06", font=(font, 15))
    user_email = Entry(signup_frame, width=40, borderwidth=0)

    usernamelabel = Label(signup_frame, text="Create your username: ", bg="black", fg="#E65C06", font=(font, 15))
    username = Entry(signup_frame, width=40, borderwidth=0)

    passwordlabel = Label(signup_frame, text="Create password: ", bg="black", fg="#E65C06", font=(font, 15))
    password_entry = Entry(signup_frame, width=40, borderwidth=0)

    repasswordlabel = Label(signup_frame, text="Re-enter password: ", bg="black", fg="#E65C06", font=(font, 15))
    repassword_entry = Entry(signup_frame, width=40, borderwidth=0)


    createuserbutton =Button(
        signup_frame,
        text="⚫ Create Account ⚫",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0,
        command=lambda: [password_email_validator(password_entry.get()
                                                  , repassword_entry.get(), user_email.get(), user_name.get(), username.get()), load_atlantic_divisionframe()])

    backbutton =Button(
        signup_frame,
        text="Back",
        font=(font, 15),
        cursor="hand2",
        bg="black",
        fg="#E65C06",
        borderwidth=0,
        command=lambda:[load_frame1(), clear_widgets(signup_frame)])

    namelabel.grid(row=0, column=0)
    user_name.grid(row=0, column=1)

    emaillabel.grid(row=1, column=0)
    user_email.grid(row=1, column=1)

    usernamelabel.grid(row=2, column=0)
    username.grid(row=2, column=1)

    passwordlabel.grid(row=3, column=0)
    password_entry.grid(row=3, column=1)

    repasswordlabel.grid(row=4, column=0)
    repassword_entry.grid(row=4, column=1)

    createuserbutton.grid(row=5, columnspan=3, pady=20)
    backbutton.grid(row=6, columnspan=3)

    new_user = User(user_name.get(), user_email.get(), username.get(), password_entry.get())


def load_frame1():

    frame1.tkraise()

    login_button = Button(frame1, image=lgb, bg="black", borderwidth=0, activebackground="black", command=lambda: load_login_frame())
    login_button.grid(row=0, columnspan=3, pady=15)

    signup_button = Button(frame1, image=sub, bg="black", borderwidth=0, activebackground="black", command=lambda : load_signup_frame())
    signup_button.grid(row=1, columnspan=3)


frame1 = Frame(root, bg="black")
login_frame = Frame(root, bg="black")
signup_frame = Frame(root, bg="black")

atlantic_divisionframe = Frame(root, bg="black")
central_divisionframe = Frame(root, bg="black")
southeast_divisionframe = Frame(root, bg="black")
northwest_divisionframe = Frame(root, bg="black")
pacific_divisionframe = Frame(root, bg="black")
southwest_divisionframe = Frame(root, bg="black")



for frame in (frame1, login_frame, signup_frame):
    frame.place(x=365, y=410, anchor=NW) # sets frame in the middle of the window


frame1.propagate(False)
login_frame.propagate(False)
signup_frame.propagate(False)

atlantic_divisionframe.propagate(False)
central_divisionframe.propagate(False)
southeast_divisionframe.propagate(False)
northwest_divisionframe.propagate(False)
pacific_divisionframe.propagate(False)
southwest_divisionframe.propagate(False)


load_frame1()

root.mainloop()