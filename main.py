
from tkinter import *
from PIL import Image, ImageTk
import os

creds = 'tempfile.temp'  # This just sets the variable creds to 'tempfile.temp'

def Signup():  # This is the signup definition,
    global pwordE  # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots

    roots = Tk()  # This creates the window, just a blank one.
    roots.title('Signup')  # This renames the title of said window to 'signup'
    intruction = Label(roots,
                       text='Please Enter new Credidentials\n')  # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0,
                    sticky=E)  # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)

    nameL = Label(roots, text='New Username: ')  # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ')  # ^^
    nameL.grid(row=1, column=0,
               sticky=W)  # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W)  # ^^

    nameE = Entry(roots)  # This now puts a text box waiting for input.
    pwordE = Entry(roots,
                   show='*')  # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1)  # You know what this does now :D
    pwordE.grid(row=2, column=1)  # ^^

    signupButton = Button(roots, text='Signup',
                          command=FSSignup)  # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()  # This just makes the window keep open, we will destroy it soon


def FSSignup():
    with open(creds, 'w') as f:  # Creates a document using the variable we made at the top.
        f.write(
            nameE.get())  # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n')  # Splits the line so both variables are on different lines.
        f.write(pwordE.get())  # Same as nameE just with pword var
        f.close()  # Closes the file

    roots.destroy()  # This will destroy the signup window. :)
    Login()  # This will move us onto the login definition :D


def Login():
    global nameEL
    global pwordEL  # More globals :D
    global rootA

    rootA = Tk()  # This now makes a new window.
    rootA.geometry('1100x666')
    rootA.title('Login')  # This makes the window title 'login'

    intruction = Label(rootA, text='Please Login\n')  # More labels to tell us what they do
    intruction.grid(sticky=E)  # Blahdy Blah

    backgroundimg = PhotoImage(file="LogInBackground.png")
    background = Label(rootA, text='Username: ')  # More labels
    background.config(image=backgroundimg, borderwidth=0, bg = "black")
    background.place(x=0, y=0)

    username = PhotoImage(file="Username.png")
    nameL = Label(rootA, text='Username: ')  # More labels
    nameL.config(image=username, borderwidth=0, bg = "#303030")
    pwordL = Label(rootA, text='Password: ')  # ^
    password = PhotoImage(file="Password.png")
    pwordL.config(image=password, borderwidth=0, bg = "#303030")
    nameL.place(x=360.5, y=384.5)
    pwordL.place(x=361.5, y=444.5)

    nameEL = Entry(rootA, font = "Times 28 bold", width=9)  # The entry input
    nameEL.config(borderwidth=0, bg = "#303030")
    pwordEL = Entry(rootA, show='*', font = "Times 28 bold", width=9)
    pwordEL.config(borderwidth=0, bg = "#303030")
    nameEL.place(x=468.5, y=384.5)
    pwordEL.place(x=468.5, y=444.5)


    loginB = Button(rootA, text='Login',
                    command=CheckLogin)  # This makes the login button, which will go to the CheckLogin def.
    img = PhotoImage(file="LogInButton.png")  # Button image
    loginB.config(image=img, borderwidth=0, bg = "green")
    loginB.place(x=360.5, y=503.5)

    rmuser = Button(rootA, text='Delete User', fg='red',
                    command=DelUser)  # This makes the deluser button. blah go to the deluser def.
    rmuser.config(borderwidth=0, bg = "black")
    rmuser.place(x=468, y=550)
    rootA.mainloop()


def CheckLogin():
    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    if nameEL.get() == uname and pwordEL.get() == pword:  # Checks to see if you entered the correct data.
        mainMenu()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('1100x666')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        rootA.destroy()
        r.mainloop()


def mainMenu():
    r = Tk()
    r.title('SYS64 Portal')
    r.geometry('1100x666')
    backgroundimgportal = PhotoImage(file="error.png")
    background = Label(r, text='Username: ')  # More labels
    background.config(image=backgroundimgportal, borderwidth=0, bg="black")
    background.place(x=0, y=0)
    rlbl = Label(r, text='\nWelcome to the Portal!')
    rlbl.pack()
    rootA.destroy()
    r.mainloop()


def invalidLogin():
    r = Tk()
    r.title('D:')
    r.geometry('1100x666')
    rlbl = Label(r, text='\nWelcome to the Portal!')
    rlbl.pack()
    rootA.destroy()
    r.mainloop()


def DelUser():
    os.remove(creds)  # Removes the file
    rootA.destroy()  # Destroys the login window
    Signup()  # And goes back to the start!


if os.path.isfile(creds):
    Login()
else:  # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
