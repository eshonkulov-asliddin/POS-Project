from tkinter import *
from tkinter import ttk


FONT = ("Arial", 14, "bold")
BUTTON = "#EFFFFD"
BUTTON_BG = "#9ADCFF"

def kiritish_oynasiga_otish():
    ombor_oynasi.destroy()
    import kiritish



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
ombor_oynasi.config(bg=BUTTON_BG)
ombor_oynasi.title('OMBOR')
ombor_oynasi.geometry("2000x1000")

# Add some style
style = ttk.Style()
#Pick a theme
style.theme_use("default")
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


# chiqish_btn = RoundedButton(button_frame, 90, 50, 12, 2, 'white', 'lightblue')
# chiqish_btn.create_text(45, 25, text="<------", fill="black", font=("Arial", 14, "bold"))
# chiqish_btn.grid(ipady=4, row=0, column=0, padx=10, pady=10)

# kiritish_btn = Button(button_frame, text="Kiritish  ⬇️", width=12, command=kiritish_oynasiga_otish)
# kiritish_btn.grid(ipady=12, row=0, column=0, pady=10, padx=(80, 0))
kiritish_btn = RoundedButton(button_frame, 120, 50, 12, 2, BUTTON, BUTTON_BG, command=kiritish_oynasiga_otish)
kiritish_btn.create_text(65, 25, text="Kiritish  ⬇️", fill="black", font=FONT)
kiritish_btn.grid(ipady=4, row=0, column=0, pady=10, padx=(80, 0))



# hisobot_btn = Button(button_frame, text="Hisobot  ⬆️", width=12)
# # hisobot_btn.grid(ipady=12, row=0, column=0, columnspan=2, pady=10, padx=(160, 0))
hisobot_btn = RoundedButton(button_frame, 120, 50, 12, 2, BUTTON, BUTTON_BG)
hisobot_btn.create_text(65, 25, text="Hisobot  ⬆️", fill="black", font=FONT)
hisobot_btn.grid(ipady=4, row=0, column=0, columnspan=2, pady=10, padx=(210, 0))

# Remove One
# sozlash_btn = Button(button_frame, text="Sozlash", width=12)
# sozlash_btn.grid(ipady=12, row=0, column=1, columnspan=3, pady=10, padx=(0, 80))
sozlash_btn = RoundedButton(button_frame, 120, 50, 12, 2, BUTTON, BUTTON_BG)
sozlash_btn.create_text(65, 25, text="Sozlash  🔐️", fill="black", font=FONT)
sozlash_btn.grid(ipady=4, row=0, column=1, columnspan=3, pady=10, padx=(0, 2))


foydalanuvchi_entry = Entry(button_frame, width=34)

# foydalanuvchi_entry.insert(END, ombor_login.user_name)
foydalanuvchi_entry.grid(row=0, column=6, padx=(1000, 0))
foydalanuvchi_positsiyasi_entry = Entry(button_frame, width=34)
foydalanuvchi_positsiyasi_entry.grid(row=0, rowspan=2, column=6, padx=(1000, 0), pady=(0, 45))

qidirish_entry = Entry(button_frame, width=70)
qidirish_entry.grid(ipady=6, row=1, column=1, columnspan=3, pady=(50, 0))


# qidirish_btn = Button(button_frame,text="QIDIRISH", height=2)
# qidirish_btn.grid(row=1, column=4, columnspan=5, padx=(0, 1130), pady=(50, 0))
qidirish_btn = RoundedButton(button_frame, 120, 50, 12, 2, BUTTON, BUTTON_BG)
qidirish_btn.create_text(65, 25, text="Qidirish", fill="black", font=FONT)
qidirish_btn.grid(ipady=4, row=1, column=4, columnspan=5, padx=(0, 1070), pady=(50, 0))






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
my_tree['columns'] = ("N", "Kod", "Nomlanishi", "Shtrix kod", "Kun vaqt", "Miqdor", "Olish narxi", "Sotish narxi")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("N", anchor=CENTER, width=50)
my_tree.column("Kod", anchor=CENTER, width=265)
my_tree.column("Nomlanishi", anchor=CENTER, width=265)
my_tree.column("Shtrix kod", anchor=CENTER, width=265)
my_tree.column("Kun vaqt", anchor=CENTER, width=265)
my_tree.column("Miqdor", anchor=CENTER, width=265)
my_tree.column("Olish narxi", anchor=CENTER, width=265)
my_tree.column("Sotish narxi", anchor=CENTER, width=238)


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
    ["2", "12345", "kola", "98765", "11.12.22", "2", "10 000", "11 000"],
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
count=0

for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7],), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6],record[7],), tags=('oddrow',))

    count += 1


'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("John", 1, "Peperroni"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Mary", "2", "Cheese"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("Tina", "3", "Ham"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Bob", "4", "Supreme"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Erin", "5", "Cheese"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Wes", "6", "Onion"))
'''
# # add child
# #my_tree.insert(parent='', index='end', iid=6, text="Child", values=("Steve", "1.2", "Peppers"))
# #my_tree.move('6', '0', '0')
#
#
#
# #add_frame = Frame(root)
# #add_frame.pack(pady=20)
#
# #Labels
# #nl = Label(add_frame, text="Name")
# #nl.grid(row=0, column=0)
#
# #il = Label(add_frame, text="ID")
# #il.grid(row=0, column=1)
#
# #tl = Label(add_frame, text="Topping")
# #tl.grid(row=0, column=2)
#
# #Entry boxes
#
# #framer = Frame(root)
# #framer.pack(pady=20)
#
# #
# # data_frame = LabelFrame(root, text="Mahsulot qo'shish", font=FONT)
# # data_frame.pack(fill="x", expand="yes", padx=20, pady=5)
# #
# # raqam = Label(data_frame, text="№")
# # raqam.grid(row=0, column=0, padx=10, pady=10)
# # raqam_entry = Entry(data_frame)
# # raqam_entry.grid(row=0, column=1, padx=10, pady=10)
# #
# # kod_label = Label(data_frame, text="Kod")
# # kod_label.grid(row=0, column=2, padx=10, pady=10)
# # kod_entry = Entry(data_frame)
# # kod_entry.grid(row=0, column=3, padx=10, pady=10)
# #
# # nomlanishi_label = Label(data_frame, text="Nomlanishi")
# # nomlanishi_label.grid(row=0, column=4, padx=10, pady=10)
# # nomlanishi_entry = Entry(data_frame)
# # nomlanishi_entry.grid(row=0, column=5, padx=10, pady=10)
# #
# # shtrix_kod_label = Label(data_frame, text="Shtrix kodi")
# # shtrix_kod_label.grid(row=0, column=6, padx=10, pady=10)
# # shtrix_kodi_entry = Entry(data_frame)
# # shtrix_kodi_entry.grid(row=0, column=7, padx=10, pady=10)
# #
# # kun_oy_yil_label = Label(data_frame, text="Kun/Oy/Yil")
# # kun_oy_yil_label.grid(row=1, column=0, padx=10, pady=10)
# # kun_oy_yil_entry = Entry(data_frame)
# # kun_oy_yil_entry.grid(row=1, column=1, padx=10, pady=10)
# #
# #
# # miqdor_label = Label(data_frame, text="Miqdor")
# # miqdor_label.grid(row=1, column=2, padx=10, pady=10)
# # miqdor_entry = Entry(data_frame)
# # miqdor_entry.grid(row=1, column=3, padx=10, pady=10)
# #
# # olish_narxi_label = Label(data_frame, text="Olish narxi")
# # olish_narxi_label.grid(row=1, column=4, padx=10, pady=10)
# # olish_narxi_entry = Entry(data_frame)
# # olish_narxi_entry.grid(row=1, column=5, padx=10, pady=10)
# #
# # sotish_narxi_label = Label(data_frame, text="Sotish narxi")
# # sotish_narxi_label.grid(row=1, column=6, padx=10, pady=10)
# # sotish_narxi_label = Entry(data_frame)
# # sotish_narxi_label.grid(row=1, column=7, padx=10, pady=10)
#
#
#
#
#
#
# #name_box = Entry(data_frame)
# #name_box.grid(row=1, column=0)
#
# #id_box = Entry(data_frame)
# #id_box.grid(row=1, column=1)
#
# #topping_box = Entry(data_frame)
# #topping_box.grid(row=1, column=2)
#
# # Add Record
# def add_record():
#     my_tree.tag_configure('oddrow', background="white")
#     my_tree.tag_configure('evenrow', background="white")
#
#     global count
#     if count % 2 == 0:
#         my_tree.insert(parent='', index='end', iid=count, text="", values=(raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(), shtrix_kodi_entry.get(), kun_oy_yil_entry.get(), miqdor_entry.get(), olish_narxi_entry.get(), sotish_narxi_label.get()), tags=('evenrow',))
#     else:
#         my_tree.insert(parent='', index='end', iid=count, text="", values=(raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(), shtrix_kodi_entry.get(), kun_oy_yil_entry.get(), miqdor_entry.get(), olish_narxi_entry.get(), sotish_narxi_label.get()), tags=('oddrow',))
#
#     count += 1
#
#     # Clear the boxes
#     raqam_entry.delete(0, END)
#     kod_entry.delete(0, END)
#     nomlanishi_entry.delete(0, END)
#     shtrix_kodi_entry.delete(0, END)
#     kun_oy_yil_entry.delete(0, END)
#     miqdor_entry.delete(0, END)
#     olish_narxi_entry.delete(0, END)
#     sotish_narxi_label.delete(0, END)
#
# # Remove all records
# def remove_all():
#     for record in my_tree.get_children():
#         my_tree.delete(record)
#
# # Remove one selected
# def remove_one():
#     x = my_tree.selection()[0]
#     my_tree.delete(x)
#
# # Remove many selected
# def remove_many():
#     x = my_tree.selection()
#     for record in x:
#         my_tree.delete(record)
#
# # Select Record
# def select_record():
#     # Clear entry boxes
#     raqam_entry.delete(0, END)
#     kod_entry.delete(0, END)
#     nomlanishi_entry.delete(0, END)
#     shtrix_kodi_entry.delete(0, END)
#     kun_oy_yil_entry.delete(0, END)
#     miqdor_entry.delete(0, END)
#     olish_narxi_entry.delete(0, END)
#     sotish_narxi_label.delete(0, END)
#
#
#     # Grab record number
#     selected = my_tree.focus()
#     # Grab record values
#     values = my_tree.item(selected, 'values')
#
#     #temp_label.config(text=values[0])
#
#     # output to entry boxes
#     raqam_entry.insert(0, values[0])
#     kod_entry.insert(0, values[1])
#     nomlanishi_entry.insert(0, values[2])
#     shtrix_kodi_entry.insert(0, values[3])
#     kun_oy_yil_entry.insert(0, values[4])
#     miqdor_entry.insert(0, values[5])
#     olish_narxi_entry.insert(0, values[6])
#     sotish_narxi_label.insert(0, values[7])
#
#
# # Save updated record
# def update_record():
#     # Grab record number
#     selected = my_tree.focus()
#     # Save new data
#     my_tree.item(selected, text="", values=(raqam_entry.get(), kod_entry.get(), nomlanishi_entry.get(), kun_oy_yil_entry.get(), miqdor_entry.get(), olish_narxi_entry.get(), sotish_narxi_label.get(),))
#
#     # Clear entry boxes
#     raqam_entry.delete(0, END)
#     kod_entry.delete(0, END)
#     nomlanishi_entry.delete(0, END)
#     kun_oy_yil_entry.delete(0, END)
#     miqdor_entry.delete(0, END)
#     olish_narxi_entry.delete(0, END)
#     sotish_narxi_label.delete(0, END)
#
# # Create Binding Click function
# def clicker(e):
#     select_record()
#
# # Move Row up
# def up():
#     rows = my_tree.selection()
#     for row in rows:
#         my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
#
# # Move Row Down
# def down():
#     rows = my_tree.selection()
#     for row in reversed(rows):
#         my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
#
#
#
# #Buttons
# #move_up = Button(root, text="Move Up", command=up)
# #move_up.pack(pady=20)
#
# #move_down = Button(root, text="Move Down", command=down)
# #move_down.pack(pady=10)
#
# #select_button = Button(root, text="Select Record", command=select_record)
# #select_button.pack(pady=10)
#
# #update_button = Button(root, text="Save Record", command=update_record)
# #update_button.pack(pady=10)
# #add_record = Button(root, text="Add Record", command=add_record)
# #add_record.pack(pady=10)
#
#
#
# #temp_label = Label(root, text="")
# #temp_label.pack(pady=20)
#
# # # Bindings
# # #my_tree.bind("<Double-1>", clicker)
# # my_tree.bind("<ButtonRelease-1>", clicker)
# #
# # button_frame = LabelFrame(root, text="BUYRUQLAR", font=FONT, bg="lightblue")
# # button_frame.pack(fill="x", expand="yes", padx=20)
# #
# #
# # update_button = Button(button_frame, text="Qatorni Yangilash", command=update_record)
# # update_button.grid(ipady=12, row=0, column=0, padx=10, pady=10)
# #
# # add_record = Button(button_frame, text="Qator qo'shish", command=add_record)
# # add_record.grid(ipady=12, row=0, column=1, pady=10, padx=10)
# #
# #
# #
# # # Remove all
# # remove_all = Button(button_frame, text="Hamma qatorni o'chirish", command=remove_all)
# # remove_all.grid(ipady=12, row=0, column=2, pady=10, padx=10)
# #
# # # Remove One
# # remove_one = Button(button_frame, text="Tanlangan bitta o'chirish", command=remove_one)
# # remove_one.grid(ipady=12, row=0, column=3, pady=10, padx=10)
# #
# # # Remove Many Selected
# # remove_many = Button(button_frame, text="Tanlangan ko'p qatorni o'chirish", command=remove_many)
# # remove_many.grid(ipady=12, row=0, column=4, pady=10, padx=10)
# #
# # move_up = Button(button_frame, text="Tepaga ko'tarish", command=up)
# # move_up.grid(ipady=12, pady=10, padx=10, row=0, column=5)
# #
# # move_down = Button(button_frame, text="Pastga tushurish", command=down)
# # move_down.grid(ipady=12, pady=10, padx=10, row=0, column=6)
# #
# # select_button = Button(button_frame, text="Qatorni tanlash", command=select_record, bg="yellow")
# # select_button.grid(ipady=12, pady=10, padx=10, row=0, column=7)

ombor_oynasi.mainloop()

