from tkinter import *


def button_click():
    miles = float(input.get())
    km = round(1.609 * miles,2)
    my_label3.config(text=f"{km}")

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

my_label = Label(text="is equal to")
my_label.grid(column=0, row=1)
my_label1 = Label(text="Miles")
my_label1.grid(column=3, row=0)
my_label2 = Label(text="km")
my_label2.grid(column=3, row=1)
my_label3 = Label(text= "0")
my_label3.grid(column=1, row=1)

button = Button(text="Calculate",command=button_click)
button.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1, row=0)







window.mainloop()