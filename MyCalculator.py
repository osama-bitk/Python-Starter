from tkinter import *
from functools import partial


def button_pressed(value):
    expression_field_value.set(expression_field_value.get() + str(value))


def equal_pressed():
    try:
        result = eval(expression_field_value.get())
        expression_field_value.set(result)
    except ZeroDivisionError:
        expression_field_value.set("Math Error")
    except SyntaxError:
        expression_field_value.set("Syntax Error")


def aclear_pressed():
    expression_field_value.set("")


if __name__ == "__main__":
    window = Tk()
    window.title("Osama's Calculator")

    expression_field_value = StringVar()
    expression_field = Entry(window, width=60, textvariable=expression_field_value)
    expression_field.grid(row=0, column=0, columnspan=4)

    button_rows = [
        ["1", "2", "3", "*"],
        ["4", "5", "6", "-"],
        ["7", "8", "9", "+"],
        ["0", "/"]
    ]

    for row, buttons in enumerate(button_rows):  # when row = 1, buttons = ["1", "2", "3", "*"]
        for col, button_value in enumerate(buttons):
            when_pressed = partial(button_pressed, button_value)
            button1 = Button(window, text=button_value, height=3, width=3, borderwidth=1, command=when_pressed)
            button1.grid(row=row+1, column=col if button_value != "/" else 3, sticky="ew")

    aclear = Button(window, text='AC', height=3, width=3, borderwidth=1, command=aclear_pressed)
    aclear.grid(row=4, column=1, sticky="ew")

    equal = Button(window, text='=', height=3, width=3, borderwidth=1, command=equal_pressed)
    equal.grid(row=4, column=2, sticky="ew")

    window.mainloop()
