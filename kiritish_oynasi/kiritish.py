from tkinter import *
from tkinter import ttk

FONT = ("Arial", 14, "bold")
BUTTON = "#EFFFFD"
BUTTON_BG = "#9ADCFF"
def ombor_oynasiga_otish():
    kiritish_oynasi.destroy()
    import ombor


class RoundedButton(Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
        Canvas.__init__(self, parent, borderwidth=0,
                        relief="flat", highlightthickness=0, bg=bg)
        self.command = command

        if cornerradius > 0.5 * width:
            print("Error: cornerradius is greater than width.")
            return None

        if cornerradius > 0.5 * height:
            print("Error: cornerradius is greater than height.")
            return None

        rad = 2 * cornerradius

        def shape():
            self.create_polygon((padding, height - cornerradius - padding, padding, cornerradius + padding,
                                 padding + cornerradius, padding, width - padding - cornerradius, padding,
                                 width - padding, cornerradius + padding, width - padding,
                                 height - cornerradius - padding, width - padding - cornerradius, height - padding,
                                 padding + cornerradius, height - padding), fill=color, outline=color)
            self.create_arc((padding, padding + rad, padding + rad, padding), start=90, extent=90, fill=color,
                            outline=color)
            self.create_arc((width - padding - rad, padding, width - padding, padding + rad), start=0, extent=90,
                            fill=color, outline=color)
            self.create_arc((width - padding, height - rad - padding, width - padding - rad, height - padding),
                            start=270, extent=90, fill=color, outline=color)
            self.create_arc((padding, height - padding - rad, padding + rad, height - padding), start=180,
                            extent=90, fill=color, outline=color)

        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0)
        height = (y1 - y0)
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

kiritish_oynasi = Tk()
kiritish_oynasi.title('Kiritish Oynasi')
kiritish_oynasi.config(bg=BUTTON_BG)
kiritish_oynasi.geometry("1900x1050")

# Add some style
style = ttk.Style()
# Pick a theme
style.theme_use("default")
# Configure our treeview colors

style.configure("Treeview",
                background=BUTTON,
                foreground="black",
                rowheight=35,
                fieldbackground=BUTTON
                )
# Change selected color
style.map('Treeview',
          background=[('selected', '#347083')])

style.configure('Treeview.Heading', background=BUTTON, foreground="black")

button_frame = LabelFrame(kiritish_oynasi, font=FONT, bg=BUTTON_BG, border=0)
button_frame.pack(fill="x", expand="yes", padx=20)

chiqish_btn = RoundedButton(button_frame, 90, 50, 12, 2, BUTTON, BUTTON_BG, command=ombor_oynasiga_otish)
chiqish_btn.create_text(45, 25, text="<------", fill="black", font=FONT)
chiqish_btn.grid(ipady=4, row=0, column=0, padx=10, pady=10)

saqlash_btn = RoundedButton(button_frame, 90, 50, 12, 2, BUTTON, BUTTON_BG)
saqlash_btn.create_text(45, 25, text="Saqlash", fill="black", font=FONT)
saqlash_btn.grid(ipady=4, row=0, column=1, pady=12, padx=10)

ochirish_btn = RoundedButton(button_frame, 90, 50, 12, 2, BUTTON, BUTTON_BG)
ochirish_btn.create_text(45, 25, text="O'chirish", fill="black", font=FONT)
ochirish_btn.grid(ipady=4, row=0, column=2, pady=10, padx=10)

# Remove One
yangilash_btn = RoundedButton(button_frame, 90, 50, 12, 2, BUTTON, BUTTON_BG)
yangilash_btn.create_text(45, 25, text="Yangilash", fill="black", font=FONT)
yangilash_btn.grid(ipady=4, row=0, column=3, pady=10, padx=10)

# Remove Many Selected

# Create Treeview Frame
tree_frame = Frame(kiritish_oynasi)
tree_frame.pack(pady=10)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=9)
# Pack to the screen
my_tree.pack()

# Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("N", "Kod", "Nomlanishi", "Shtrix kod", "Kun vaqt", "Miqdor", "Olish narxi", "Sotish narxi")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("N", anchor=CENTER, width=140)
my_tree.column("Kod", anchor=CENTER, width=140)
my_tree.column("Nomlanishi", anchor=CENTER, width=100)
my_tree.column("Shtrix kod", anchor=CENTER, width=140)
my_tree.column("Kun vaqt", anchor=CENTER, width=140)
my_tree.column("Miqdor", anchor=CENTER, width=140)
my_tree.column("Olish narxi", anchor=CENTER, width=140)
my_tree.column("Sotish narxi", anchor=CENTER, width=140)

# Create Headings
my_tree.heading("#0", text="", anchor=CENTER)
my_tree.heading("N", text="N", anchor=CENTER)
my_tree.heading("Kod", text="Kod", anchor=CENTER)
my_tree.heading("Nomlanishi", text="Nomlanishi", anchor=CENTER)
my_tree.heading("Shtrix kod", text="Shtrix kod", anchor=CENTER)
my_tree.heading("Kun vaqt", text="Kun/Oy/Yil", anchor=CENTER)
my_tree.heading("Miqdor", text="Miqdor", anchor=CENTER)
my_tree.heading("Olish narxi", text="Olish narxi", anchor=CENTER)
my_tree.heading("Sotish narxi", text="Sotish narxi", anchor=CENTER)

# Add Data
data = [
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
    ["1", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],

]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="white")

global count
count = 0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(
        record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(
        record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],), tags=('oddrow',))

    count += 1

'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''
# add child
# my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
# my_tree.move('6', '0', '0')

# add_frame = Frame(root)
# add_frame.pack(pady=20)

# Labels
# nl = Label(add_frame, text="Name")
# nl.grid(row=0, column=0)

# il = Label(add_frame, text="ID")
# il.grid(row=0, column=1)

# tl = Label(add_frame, text="Topping")
# tl.grid(row=0, column=2)

# Entry boxes

# framer = Frame(root)
# framer.pack(pady=20)
FONT_ENTRY = 12
data_frame = LabelFrame(kiritish_oynasi, text="Mahsulot qo'shish", font=FONT,fg="white", bg=BUTTON_BG, border=0)
data_frame.pack(fill="x", expand="yes", padx=20, pady=5)

raqam = Label(data_frame, text="№", font=12, bg=BUTTON_BG)
raqam.grid(row=0, column=0, padx=10, pady=10)
raqam_entry = Entry(data_frame, font=FONT_ENTRY)
raqam_entry.grid(ipadx=20,ipady=4, row=0, column=1, padx=10, pady=10)

kod_label = Label(data_frame, text="Kod", font=12, bg=BUTTON_BG)
kod_label.grid(row=0, column=2, padx=10, pady=10)
kod_entry = Entry(data_frame, font=FONT_ENTRY)
kod_entry.grid(ipadx=20, ipady=4, row=0, column=3, padx=10, pady=10)

nomlanishi_label = Label(data_frame, text="Nomlanishi", font=12, bg=BUTTON_BG)
nomlanishi_label.grid(row=0, column=4, padx=10, pady=10)
nomlanishi_entry = Entry(data_frame, font=FONT_ENTRY)
nomlanishi_entry.grid(ipadx=20, ipady=4, row=0, column=5, padx=10, pady=10)

shtrix_kod_label = Label(data_frame, text="Shtrix kodi", font=12, bg=BUTTON_BG)
shtrix_kod_label.grid(row=0, column=6, padx=10, pady=10)
shtrix_kodi_entry = Entry(data_frame, font=FONT_ENTRY)
shtrix_kodi_entry.grid(ipadx=20, ipady=4, row=0, column=7, padx=10, pady=10)

kun_oy_yil_label = Label(data_frame, text="Kun/Oy/Yil", font=12, bg=BUTTON_BG)
kun_oy_yil_label.grid(row=1, column=0, padx=10, pady=10)
kun_oy_yil_entry = Entry(data_frame, font=FONT_ENTRY)
kun_oy_yil_entry.grid(ipadx=20, ipady=4, row=1, column=1, padx=10, pady=10)

miqdor_label = Label(data_frame, text="Miqdor", font=12, bg=BUTTON_BG)
miqdor_label.grid(row=1, column=2, padx=10, pady=10)
miqdor_entry = Entry(data_frame, font=FONT_ENTRY)
miqdor_entry.grid(ipadx=20, ipady=4, row=1, column=3, padx=10, pady=10)

olish_narxi_label = Label(data_frame, text="Olish narxi", font=12, bg=BUTTON_BG)
olish_narxi_label.grid(row=1, column=4, padx=10, pady=10)
olish_narxi_entry = Entry(data_frame, font=FONT_ENTRY)
olish_narxi_entry.grid(ipadx=20, ipady=4, row=1, column=5, padx=10, pady=10)

sotish_narxi_label = Label(data_frame, text="Sotish narxi", font=12, bg=BUTTON_BG)
sotish_narxi_label.grid(row=1, column=6, padx=10, pady=10)
sotish_narxi_label = Entry(data_frame, font=FONT_ENTRY)
sotish_narxi_label.grid(ipadx=20, ipady=4, row=1, column=7, padx=10, pady=10)

# name_box = Entry(data_frame)
# name_box.grid(row=1, column=0)

# id_box = Entry(data_frame)
# id_box.grid(row=1, column=1)

# topping_box = Entry(data_frame)
# topping_box.grid(row=1, column=2)

# Add Record
def add_record():
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="white")

    global count
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(
        raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(), shtrix_kodi_entry.get(), kun_oy_yil_entry.get(),
        miqdor_entry.get(), olish_narxi_entry.get(), sotish_narxi_label.get()), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(
        raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(), shtrix_kodi_entry.get(), kun_oy_yil_entry.get(),
        miqdor_entry.get(), olish_narxi_entry.get(), sotish_narxi_label.get()), tags=('oddrow',))

    count += 1

    # Clear the boxes
    raqam_entry.delete(0, END)
    kod_entry.delete(0, END)
    nomlanishi_entry.delete(0, END)
    shtrix_kodi_entry.delete(0, END)
    kun_oy_yil_entry.delete(0, END)
    miqdor_entry.delete(0, END)
    olish_narxi_entry.delete(0, END)
    sotish_narxi_label.delete(0, END)

# Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)

# Remove one selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

# Remove many selected
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)

# Select Record
def select_record():
    # Clear entry boxes
    raqam_entry.delete(0, END)
    kod_entry.delete(0, END)
    nomlanishi_entry.delete(0, END)
    shtrix_kodi_entry.delete(0, END)
    kun_oy_yil_entry.delete(0, END)
    miqdor_entry.delete(0, END)
    olish_narxi_entry.delete(0, END)
    sotish_narxi_label.delete(0, END)

    # Grab record number
    selected = my_tree.focus()
    # Grab record values
    values = my_tree.item(selected, 'values')

    # temp_label.config(text=values[0])

    # output to entry boxes
    raqam_entry.insert(0, values[0])
    kod_entry.insert(0, values[1])
    nomlanishi_entry.insert(0, values[2])
    shtrix_kodi_entry.insert(0, values[3])
    kun_oy_yil_entry.insert(0, values[4])
    miqdor_entry.insert(0, values[5])
    olish_narxi_entry.insert(0, values[6])
    sotish_narxi_label.insert(0, values[7])

# Save updated record
def update_record():
    # Grab record number
    selected = my_tree.focus()
    # Save new data
    my_tree.item(selected, text="", values=(
    raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(),shtrix_kodi_entry.get(), kun_oy_yil_entry.get(), miqdor_entry.get(),
    olish_narxi_entry.get(), sotish_narxi_label.get(),))

    # Clear entry boxes
    raqam_entry.delete(0, END)
    kod_entry.delete(0, END)
    nomlanishi_entry.delete(0, END)
    shtrix_kodi_entry.delete(0, END)
    kun_oy_yil_entry.delete(0, END)
    miqdor_entry.delete(0, END)
    olish_narxi_entry.delete(0, END)
    sotish_narxi_label.delete(0, END)

# Create Binding Click function
def clicker(e):
    select_record()

# Move Row up
def up():
    rows = my_tree.selection()
    for row in rows:
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) - 1)

# Move Row Down
def down():
    rows = my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row, my_tree.parent(row), my_tree.index(row) + 1)

# Buttons
# move_up = Button(root, text="Move Up", command=up)
# move_up.pack(pady=20)

# move_down = Button(root, text="Move Down", command=down)
# move_down.pack(pady=10)

# select_button = Button(root, text="Select Record", command=select_record)
# select_button.pack(pady=10)

# update_button = Button(root, text="Save Record", command=update_record)
# update_button.pack(pady=10)
# add_record = Button(root, text="Add Record", command=add_record)
# add_record.pack(pady=10)

# temp_label = Label(root, text="")
# temp_label.pack(pady=20)

# Bindings
# my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)

button_frame = LabelFrame(kiritish_oynasi, text="BUYRUQLAR", font=FONT, fg="white", bg=BUTTON_BG, border=0)
button_frame.pack(fill="x", expand="yes", padx=20)

update_record =RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=update_record)
update_record.create_text(85, 40, text="Qatorni Yangilash", fill="black", font=FONT)
update_record.grid(ipady=4, pady=10, padx=10, row=0, column=0)

add_record = RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=add_record)
add_record.create_text(85, 40, text="Qatorni qo'shish", fill="black", font=FONT)
add_record.grid(ipady=4, pady=10, padx=10, row=0, column=1)

# Remove all
remove_all =RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=update_record)
remove_all.create_text(85, 40, text="Hamma qatorni \no'chirish", fill="black", font=FONT)
remove_all.grid(ipady=4, pady=10, padx=10, row=0, column=2)

# Remove One
remove_one = RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=remove_one)
remove_one.create_text(85, 40, text="Tanlangan bitta \nqatorni o'chirish", fill="black", font=FONT)
remove_one.grid(ipady=4, row=0, column=3, pady=10, padx=10)

# Remove Many Selected
remove_one = RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=remove_many)
remove_one.create_text(85, 40, text="Tanlangan ko'p \nqatorni o'chirish", fill="black", font=FONT)
remove_one.grid(ipady=4, row=0, column=4, pady=10, padx=10)


move_up =RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=up)
move_up.create_text(85, 40, text="Tepage ko'tarish", fill="black", font=FONT)
move_up.grid(ipady=4, pady=10, padx=10, row=0, column=5)

move_down =RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=down)
move_down.create_text(85, 40, text="Pastga tushurish", fill="black", font=FONT)
move_down.grid(ipady=4, pady=10, padx=10, row=0, column=6)

#Because of my function name and button sam i added d(recordd).Without this selecting all will not work
select_recordd =RoundedButton(button_frame, 170, 80, 12, 2, BUTTON, BUTTON_BG, command=select_record)
select_recordd.create_text(85, 40, text="Qatorni tanlash", fill="black", font=FONT)
select_recordd.grid(ipady=4, pady=10, padx=10, row=0, column=7)

kiritish_oynasi.mainloop()
