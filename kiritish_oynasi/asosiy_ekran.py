from tkinter import *
import tkinter as tk
root = Tk()
root.config(bg="#AEFEFF")
# window = Tk()
# window.title("kiritish oynasi")
# # window.minsize(width=800, height=600)
# window.config(bg="#AEFEFF")

def ombor_login():
    root.destroy()
    import ombor_login

def sotuvchi_login():
    root.destroy()
    import sotuvchi_login

def online_hisobot_login():
    root.destroy()
    import online_hisobot_login

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

#Canvas widget
canvas = tk.Canvas(root, width=1900, height=1050, bg="#AEFEFF")
canvas.grid()

#window responsive
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#Buttons
ombor_btn = RoundedButton(root, 250, 180, 25, 2, '#5C527F', '#AEFEFF', command=ombor_login)
ombor_btn.create_text(125, 95, text="Ombor", fill="white", font=("Arial", 14, "bold"))
ombor_btn.rowconfigure(1, weight=1)
ombor_btn.columnconfigure(0, weight=1)
ombor_btn.grid(row=0, column=0, padx=(0, 255), pady=(50, 200))

sotuvchi_btn = RoundedButton(root, 250, 180, 25, 2, '#5C527F', '#AEFEFF', command=sotuvchi_login)
sotuvchi_btn.create_text(125, 95, text="Sotuvchi", fill="white", font=("Arial", 14, "bold"))
sotuvchi_btn.grid(row=0, column=0, padx=(255, 0), pady=(50, 200))

online_hisobot_btn = RoundedButton(root, 520, 100, 25, 2, '#5C527F', '#AEFEFF', command=online_hisobot_login)
online_hisobot_btn.create_text(250, 50, text="Online hisobot", fill="white", font=("Arial", 14, "bold"))
online_hisobot_btn.grid(row=0,column=0, pady=(150, 0))

root.update()
print(root.grid_bbox(0,0,1,1))
root.mainloop()
