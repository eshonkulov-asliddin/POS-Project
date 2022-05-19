from tkinter import *
from tkinter import ttk


class NewWindow(Toplevel):

    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Qidirish")
        self.config(bg="deep sky blue")
        self.geometry("1000x400")


        # Qidirish
        text = Text(self, height=2, width=50)
        text.insert(END, "")
        text.grid(row=1, column=0, columnspan=1, pady=(40, 50), padx=(0, 20))

        button = Button(self, text="Qidirish")
        button.config(width=14, height=2)
        button.grid(row=1, column=0, columnspan=2, pady=(5, 20), padx=(510, 0))

        button = Button(self, text="Tanlash")
        button.config(width=19, height=2)
        button.grid(row=0, column=0, columnspan=3, pady=(15, 20), padx=(0, 804))

        label = Label(self, text=" ⬅️")
        label.config(fg="black", font=70)
        label.grid(row=0, column=0, padx=(0, 904))

        # Table
        style = ttk.Style()
        style.theme_use('clam')

        # Add a Treeview widget
        tree = ttk.Treeview(self, column=("№", "Код", "Названия", "Штрих-код", "Сумма"), show='headings', height=5)
        tree.column("# 1", anchor=CENTER)
        tree.heading("# 1", text="№")
        tree.column("# 2", anchor=CENTER)
        tree.heading("# 2", text="Код")
        tree.column("# 3", anchor=CENTER)
        tree.heading("# 3", text="Названия")
        tree.column("# 4", anchor=CENTER)
        tree.heading("# 4", text="Штрих-код")
        tree.column("# 5", anchor=CENTER)
        tree.heading("# 5", text="Сумма")



        # Insert the data in Treeview widget
        tree.insert('', 'end', text="1", values=('1', '10', 'a', '12345', '1 125 000'))
        tree.insert('', 'end', text="1", values=('2', '11', 'b', '22345', '10 125'))
        tree.insert('', 'end', text="1", values=('3', '12', 'c', '32345', '10 125 000'))
        tree.insert('', 'end', text="1", values=('4', '13', 'd', '42345', '125 000'))

        tree.grid(row=2)
        self.mainloop()



