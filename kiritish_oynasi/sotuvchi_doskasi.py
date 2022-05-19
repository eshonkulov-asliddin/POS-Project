from tkinter import *
from PIL import ImageTk, Image


def calculatorga_otish():
    from calculator import Calculator
    calculator = Calculator()

FONT = ("Arial", 14, "bold")
BUTTON = "#EFFFFD"
BUTTON_BG = "#9ADCFF"

window = Tk()
window.config(bg=BUTTON_BG)
window.title('OMBOR')
window.geometry("2000x1000")


for i in range(1, 11):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)



#Code Entry
entry = Entry(width=65, font=('Century 12'))
entry.grid(ipadx=12, ipady=20, padx=(0, 47))


#calculator icon
img_cal = Image.open("images/calculator_icon.png")
resized_cal = img_cal.resize((140, 130), Image.ANTIALIAS)

new_img_cal = ImageTk.PhotoImage(resized_cal)

my_label = Button(image=new_img_cal, bg=BUTTON_BG, border=0, command=calculatorga_otish)
my_label.grid(row=0, column=2, padx=(283, 0))

#increase icon
img_rise = Image.open("images/increase.png")
resized_rise = img_rise.resize((140, 130), Image.ANTIALIAS)

new_img_rise = ImageTk.PhotoImage(resized_rise)

increase_btn = Button(image=new_img_rise, bg=BUTTON_BG, border=0)
increase_btn.grid(row=0, column=2, padx=(653, 0), pady=(0, 23))

#man icon
img_user = Image.open("images/user.png")
resized_user = img_user.resize((140, 130), Image.ANTIALIAS)

new_img_user = ImageTk.PhotoImage(resized_user)

user_btn = Button(image=new_img_user, bg=BUTTON_BG, border=0)
user_btn.grid(row=0, column=2, padx=(1053, 0), pady=(0, 23))
#Entries
for i in range(1, 9):
    num = 0
    entry = Entry(width=65, font=('Century 12'))
    entry.insert(END, f"{i}  ")
    entry.grid(ipady=12, ipadx=12, pady=3, padx=(0, 50))

#label
label_text = Label(text="SOTUVCHI: RAHIMOV SANJAR", font=('Century', 18, "bold"), bg=BUTTON_BG)
label_text.grid(row=0, column=1, columnspan=2, pady=(70, 78), padx=(0, 593))


# button_img = PhotoImage(file='png-transparent-coca-cola-fizzy-drinks-cocacola-diet-coke-cocacola-zero-sugar-cocacola-life-coca-cola-drink-supermarket.png', width=900)
# product_entry = Entry()
# product_entry.grid(ipadx=600, ipady=390, column=1, columnspan=4, row=1, rowspan=29, pady=(0, 200))
button_frame = Frame(width=2145, height=1923, bg="white")
button_frame.grid(row=1, rowspan=9,  column=2, padx=(0, 165), pady=(0, 54))
button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)
#first row
for i in range(1, 5):
    button = Button(button_frame, width=35, height=14, bg="red")
    button.grid(column=i, row=1, padx=10, pady=10)
    button.rowconfigure(i, weight=1)
    button.columnconfigure(0, weight=1)

#second row
for i in range(1, 5):
    button = Button(button_frame, width=35, height=14, bg="red")
    button.grid(column=i, row=2, padx=10, pady=10)
    button.rowconfigure(i, weight=1)
    button.columnconfigure(0, weight=1)
#Third row
for i in range(1, 5):
    button = Button(button_frame,width=35, height=14, bg="red")
    button.grid(column=i, row=3, padx=10, pady=10)
    button.rowconfigure(i, weight=1)
    button.columnconfigure(0, weight=1)
    #Overall price
# overall = Entry(width=35, font=('Century 12'))
# overall.grid(ipady=32, ipadx=12, padx=(0, 50), pady=5, column=0, row=8, rowspan=9)
# text = Text(height=11, width=69, bg="#FF8AAE")
# text.insert(END, "\n\nOVERALL PRICE")
# text.config(font=("Arial", 11, "bold"))
# text.grid(column=0, row=9, rowspan=9, padx=(0, 110), pady=(45, 0))
overall_price_frame = Frame(width=579, height=171, bg="darkblue")
overall_price_frame.grid(column=0, row=9, padx=(0, 84))

entry = Entry(width=53)
entry.grid(ipady=23, row=9, column=0, padx=(0, 340), pady=(105, 0))


window.mainloop()