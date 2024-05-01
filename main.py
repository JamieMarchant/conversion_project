from tkinter import *


window = Tk()
window.title("Converter")
window.minsize(width=300, height=100)
window.config(padx=100)


def calculate():
    miles = input.get()
    km_convert = round(float(miles) * 1.609, 2)
    output.config(text=f"{km_convert}")


input = Entry(width=10)
input.get()
input.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=1, row=1)

output = Label(text="0")
output.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=2, row=2)


window.mainloop()
