# Password Generator
import random
import string
from tkinter import*
# bg = "#f0f0f0"

window = Tk()
window.title("Password Generator")
window.geometry("900x900")
window.resizable(False, False)

def check_strength(password_value, display_label):
    has_upper = any(c.isupper() for c in password_value)
    has_lower = any(c.islower() for c in password_value)
    has_digit = any(c.isdigit() for c in password_value)
    has_special = any(c in "!@#$%^&*()_+?><{}[]|" for c in password_value)

    score = sum([has_upper, has_lower, has_digit, has_special])
    if password_value=="":
        result = "Invalid Password"
        display_label.config(text=result, fg="red", bg="aqua")
    elif len(password_value) < 6:
        result = "⚠️Weak Password⚠️"
        display_label.config(text=result, fg="red", bg="aqua")
    elif score >= 4:
        result = "Very Strong Password👍"
        display_label.config(text=result, fg="green", bg="aqua")
    elif score == 3:
        result = "Moderate Password 🙂"
        display_label.config(text=result, fg="orange", bg="aqua")
    else:
        result = "⚠️Weak Password⚠️"
        display_label.config(text=result, fg="red", bg="aqua")
    
    


def generate_password():

    length_pass = length.get()

    chars = ""

    # Checkboxes (assumed IntVar: 1 = checked, 0 = unchecked)
    if uppercase.get() == 1:
        chars += string.ascii_uppercase

    if lowercase.get() == 1:
        chars += string.ascii_lowercase

    if number.get() == 1:
        chars += string.digits

    if symbol.get() == 1:
        chars += string.punctuation

    # If nothing selected
    if chars == "":
        display_pass.config(text="Select at least one option ❗")
        return

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length_pass))

    # 🔥 SHOW PASSWORD
    pass1.set(password)
    display_pass.config(text=f"Generated: {password}")


def copy_password():
    window.clipboard_clear()
    window.clipboard_append(pass1.get())


frame1 = Frame(window)
frame1.pack()
header  = Label(frame1, text="                      Password Generator                      ", fg = "yellow", bg = "blue", font="arial 25 bold")
header.pack(padx=0, pady=(35,0), fill=X)

frame2 = Frame(window)
frame2.pack()

canvas1 = Canvas(frame2, width=500, height=800, bg = "#b3ed3e")
canvas1.grid(row=0, column=0, pady = 50)

h1 = Label(canvas1, text = "Test Strength of your Password", font="arial 20 bold underline", bg="#b3ed3e")
h1.grid(row=0, column=0, pady=(10, 0), padx=15, columnspan=2)

question = Label(canvas1, text = "Enter your password below: ", font="arial 15 bold")
question.grid(row=1, column=0, pady=(30,0), padx=(0,0), columnspan=2)

pass1 = StringVar()
password = Entry(canvas1, textvariable=pass1, font="arial 15 bold", width=20)
password.grid(row=2, column=0, pady=(30,0), padx=0, columnspan=2)

button1 = Button(canvas1, text="Check", fg = "yellow", bg="#e01bfa", font="arial 18 bold", command=lambda: check_strength(pass1.get(), display_label))
button1.grid(row=3, column=0, pady=(30,5), columnspan=2)

display_label = Label(canvas1, text="", bg="#b3ed3e", font="arial 15 bold")
display_label.grid(row=4,column=0, padx=(0,0), pady=(30, 10), columnspan=2)



canvas2 = Canvas(frame2, width=500, height=800, bg = "aqua")
canvas2.grid(row=0, column=1, pady = 50)

h2 = Label(canvas2, text = "   PASSWORD GENERATOR   ", font="arial 20 bold underline", bg="aqua")
h2.grid(row=0, column=0, pady=(10, 0), padx=15, columnspan=2)

text = Label(canvas2, text = "Length: ", font="arial 14 bold", bg="aqua")
text.grid(row=1, column=0, pady=(10,5), columnspan=2)

length = IntVar()
long = Spinbox(canvas2, text="Length", from_=6, to=14, textvariable=length, width=20, font="arial 14 bold")
long.grid(row=2, column=0, padx=(0,0), pady=(4,0), columnspan=2)

uppercase = IntVar()
upper = Checkbutton(canvas2, text="Uppercase", variable=uppercase, bg="aqua", font="arial 14 bold")
upper.grid(row=3, column=0, padx=(0,0), pady=(10,0), columnspan=2)

lowercase = IntVar()
lower = Checkbutton(canvas2, text="Lowercase", variable=lowercase, bg="aqua", font="arial 14 bold")
lower.grid(row=4, column=0, padx=(0,0), pady=(10,0), columnspan=2)

symbol = IntVar()
spec = Checkbutton(canvas2, text="Symbols", variable=symbol, bg="aqua", font="arial 14 bold")
spec.grid(row=5, column=0, padx=(0,0), pady=(10,0), columnspan=2)

number = IntVar()
num = Checkbutton(canvas2, text="Number", variable=number, bg="aqua", font="arial 14 bold")
num.grid(row=6, column=0, padx=(0,0), pady=(10,0), columnspan=2)

button2 = Button(canvas2, text="Generate Password", fg = "white", bg="grey", font="arial 18 bold", command=generate_password)
button2.grid(row=7, column=0, padx=(0,0), pady=(10,10), columnspan=2)

display_pass = Label(canvas2, text="", font="arial 17 bold", bg="aqua")
display_pass.grid(row=8, column=0, padx=(0,0), pady=(10, 10), columnspan=2)

copy = Button(canvas2, text="Copy Password", fg="white", bg="green", font="arial 14 bold", command=copy_password)
copy.grid(row=9, column=0, columnspan=2, pady=10)


window.mainloop()
