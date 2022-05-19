from tkinter import *


def ombor_oynasiga_otish():
    root.destroy()
    import ombor

def user():
    user_name = username_1.get()
    return user_name



root = Tk()

# Main window of Application
root.title("Please Login")
root.geometry("1900x1050")
root.config(background='lightblue', borderwidth=8)

for i in range(3):
    # root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)

# Creating Label Widget
myLabel1 = Label(root, text="Username :", background='lightblue', font="bold")
myLabel2 = Label(root, text="Password :", background='lightblue', font="bold")
# Entry fields
username_1 = Entry(root, width=54)
user_name = username_1.get()
password_1 = Entry(root, show='*', width=54)

# Putting labels onto screen

myLabel1.grid(row=0, column=1, pady=(400, 0), padx=(0, 500))
myLabel2.grid(row=1, column=1, padx=(0, 500))

# Entry field Locations
username_1.grid(row=0, column=1, pady=(400, 5), ipady=5)
password_1.grid(row=1, column=1, ipady=5)



loginButton1 = Button(root, text="Login", height=1, font="bold", command=ombor_oynasiga_otish)
cancelButton3 = Button(root, text="Cancel", height=1, font="bold", command=quit)

# Putting buttons onto screen

loginButton1.grid(row=6, column=1, padx=(0, 65), pady=10)
cancelButton3.grid(row=6, column=1, padx=(65, 0), pady=10)

# New window
#
root.mainloop()
