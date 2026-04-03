import tkinter
import math

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["/", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#969696"
color_black = "#1A1A1A"
color_dark_gray = "#6A1919"
color_orange = "#DB1919"
color_white = "white"

window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Arial", 45), background=color_black,
                      foreground=color_white, anchor="e", width=column_count)
label.grid(row=0, column=0, columnspan=column_count, sticky="we")

expression = ""

def button_clicked(value):
    global expression

    if value == "AC":
        expression = ""
        label["text"] = "0"

    elif value == "+/-":
        if expression:
            if expression.startswith("-"):
                expression = expression[1:]
            else:
                expression = "-" + expression
            label["text"] = expression

    elif value == "%":
        try:
            expr = expression.replace("x", "*")
            result = str(eval(expr))
            result = str(float(result) / 100)
            expression = result
            label["text"] = remove_zero_decimal(float(result))
        except:
            label["text"] = "Error"
            expression = ""

    elif value == "√":  # square root
        try:
            if expression == "":
                return
            num = float(expression)
            if num < 0:
                label["text"] = "Error"
                expression = ""
            else:
                result = math.sqrt(num)
                expression = str(result)
                label["text"] = remove_zero_decimal(result)
        except:
            label["text"] = "Error"
            expression = ""

    elif value == "=":
        try:
            expr = expression.replace("x", "*")
            result = str(eval(expr))
            expression = result
            label["text"] = remove_zero_decimal(float(result))
        except:
            label["text"] = "Error"
            expression = ""

    else:
        if label["text"] == "0" and value not in [".", "+", "-", "x", "/"]:
            expression = value
        else:
            expression += value
        label["text"] = expression

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("Arial", 30),
                                width=3, height=1,
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        button.grid(row=row + 1, column=column)

frame.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
