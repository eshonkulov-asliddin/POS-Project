from tkinter import *
from tkinter import ttk


FONT = ("Arial", 14, "bold")
BUTTON = "#EFFFFD"
BUTTON_BG = "#9ADCFF"



class RoundedButton(Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        Canvas.__init__(self, parent, borderwidth=0,
            relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5*width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5*height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2*cornerradius
        def shape():
            self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
            self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


        id = shape()
        (x0,y0,x1,y1)  = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

FONT = ("Arial", 12)

ombor_oynasi = Tk()
ombor_oynasi.config(bg="lightblue")
ombor_oynasi.title('OMBOR')
ombor_oynasi.geometry("2000x1000")

# Add some style
style = ttk.Style()
#Pick a theme
style.theme_use("clam")
# Configure our treeview colors

style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=50,
    fieldbackground="#D3D3D3"
    )
# Change selected color
style.map('Treeview',
    background=[('selected', '#347083')])


button_frame = LabelFrame(ombor_oynasi, font=FONT, bg=BUTTON_BG, highlightthickness=0, border=0)
button_frame.pack(fill="x", expand="yes", padx=20)


# Remove One

sozlash_btn = RoundedButton(button_frame, 160, 60, 12, 2, BUTTON, BUTTON_BG)
sozlash_btn.create_text(75, 30, text="Sozlash", fill="black", font=FONT)
sozlash_btn.grid(ipady=4, row=0, column=2, columnspan=3, pady=(95, 0), padx=(390, 10))


# foydalanuvchi_entry = Entry(button_frame, width=34)
#
# # foydalanuvchi_entry.insert(END, ombor_login.user_name)
# foydalanuvchi_entry.grid(row=0, column=6, padx=(1000, 0))
kun_oy_yil_entry = Entry(button_frame, width=20, font=5)
kun_oy_yil_entry.grid(ipady=7,row=0, rowspan=2, column=5, padx=(0, 120), pady=(0, 45))

dan_entry = Entry(button_frame, width=10, font=5)
dan_entry.insert(END, '    dan')
dan_entry.grid(ipady=7, row=0, rowspan=2, column=5, columnspan=7,  padx=(0, 90), pady=(0, 45))

kun_oy_yil_entry = Entry(button_frame, width=20, font=5)
kun_oy_yil_entry.grid(ipady=7, row=1, rowspan=2, column=5, padx=(0, 120), pady=(0, 145))

gacha_entry = Entry(button_frame, width=10, font=5)
gacha_entry.insert(END, "    gacha")
gacha_entry.grid(ipady=7,row=1, rowspan=2, column=5, columnspan=7,  padx=(0, 90), pady=(0, 145))

qidirish_entry = Entry(button_frame, width=120, font=23)
qidirish_entry.grid(ipady=6, row=1, column=0, columnspan=3, pady=(10, 0))
qidirish_entry.focus()

# qidirish_btn = Button(button_frame,text="QIDIRISH", height=2)
# qidirish_btn.grid(row=1, column=3, columnspan=5, padx=(20, 888), pady=(10, 0))


qidirish_btn = RoundedButton(button_frame, 160, 60, 12, 2, BUTTON, BUTTON_BG)
qidirish_btn.create_text(75, 30, text="Qidirish", fill="black", font=FONT)
qidirish_btn.grid(ipady=4, row=1, column=3, columnspan=5, padx=(20, 888), pady=(10, 0))





# Create Treeview Frame
hisobot_frame = Frame(ombor_oynasi)
hisobot_frame.pack(pady=(0, 240))

# Treeview Scrollbar
hisobot_scroll = Scrollbar(hisobot_frame, width=10)
hisobot_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(hisobot_frame, yscrollcommand=hisobot_scroll.set, selectmode=EXTENDED)
# Pack to the screen
my_tree.pack()

#Configure the scrollbar
hisobot_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("N", "Kod", "Nomlanishi", "Shtrix kod", "Kun vaqt", "Miqdor", "Olish narxi",
     "Olish narxi jami", "Sotish miqdori", "Sotish vaqti", "Sotish narxi", "Sotish narxi jami", "Qoldiq", "O'sish", "O'sish narxda")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("N", anchor=CENTER, width=50)
my_tree.column("Kod", anchor=CENTER, width=133)
my_tree.column("Nomlanishi", anchor=CENTER, width=133)
my_tree.column("Shtrix kod", anchor=CENTER, width=133)
my_tree.column("Kun vaqt", anchor=CENTER, width=130)
my_tree.column("Miqdor", anchor=CENTER, width=130)
my_tree.column("Olish narxi", anchor=CENTER, width=130)
my_tree.column("Olish narxi jami", anchor=CENTER, width=130)
my_tree.column("Sotish miqdori", anchor=CENTER, width=130)
my_tree.column("Sotish vaqti", anchor=CENTER, width=130)
my_tree.column("Sotish narxi", anchor=CENTER, width=130)
my_tree.column("Sotish narxi jami", anchor=CENTER, width=130)
my_tree.column("Qoldiq", anchor=CENTER, width=130)
my_tree.column("O'sish", anchor=CENTER, width=130)
my_tree.column("O'sish narxda", anchor=CENTER, width=130)


# Create Headings
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("N", text="N", anchor=CENTER)
my_tree.heading("Kod", text="Kod", anchor=CENTER)
my_tree.heading("Nomlanishi", text="Nomlanishi", anchor=CENTER)
my_tree.heading("Shtrix kod", text="Shtrix kod", anchor=CENTER)
my_tree.heading("Kun vaqt", text="Kun/Oy/Yil", anchor=CENTER)
my_tree.heading("Miqdor", text="Miqdor", anchor=CENTER)
my_tree.heading("Olish narxi", text="Olish narxi", anchor=CENTER)
my_tree.heading("Olish narxi jami", text="Olish narxi jami", anchor=CENTER)
my_tree.heading("Sotish miqdori", text="Sotish miqdori", anchor=CENTER)
my_tree.heading("Sotish vaqti", text="Sotish vaqti", anchor=CENTER)
my_tree.heading("Sotish narxi", text="Sotish narxi", anchor=CENTER)
my_tree.heading("Sotish narxi jami", text="Sotish narxi jami", anchor=CENTER)
my_tree.heading("Qoldiq", text="Qoldiq", anchor=CENTER)
my_tree.heading("O'sish", text="O'sish", anchor=CENTER)
my_tree.heading("O'sish narxda", text="O'sish narxda", anchor=CENTER)

# Add Data
data = [
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000", "11 000"],



]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="white")

global count
count=0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11],record[12],record[13],record[14]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11],record[12],record[13],record[14]), tags=('oddrow',))
    count += 1




ombor_oynasi.mainloop()

