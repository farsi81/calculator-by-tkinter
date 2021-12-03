from tkinter import *
import tkinter.messagebox

root = Tk()
# =================== settings ===================

root.geometry("620x220")
root.resizable(width=False, height=False)
root.title("Calculator")
color = "gray"
root.configure(bg=color)
font = "BOLd"

# =================== variables ===================
num1 = StringVar()
num2 = StringVar()
res_value = StringVar()

# =================== frames ===================

top_first = Frame(root, width=400, height=50, bg=color)
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg=color)
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg=color)
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg=color)
top_forth.pack(side=TOP)


# =================== Functions ===================


def errorMsg(ms):
    if ms == "error":
        tkinter.messagebox.showerror("Error", "something went wrong !")
    elif ms == "error division zero":
        tkinter.messagebox.showerror("Division Error", "can not divide by 0")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res_value.set(value)
    except:
        errorMsg("error")


def div():
    if num2.get() == "0":
        errorMsg("error division zero")
    elif num2.get() != 0:
        try:
            value = float(num1.get()) / float(num2.get())
            res_value.set(value)
        except:
            errorMsg("error")


# =================== buttons ===================

btn_plus = Button(top_third, text="+", width=12, height=1, highlightbackground=color, font=font,
                  command=lambda: plus()). \
    pack(side=LEFT, padx=5, pady=5)

btn_minus = Button(top_third, text="-", width=12, height=1, highlightbackground=color, font=font,
                   command=lambda: minus()). \
    pack(side=LEFT, padx=5, pady=5)

btn_mul = Button(top_third, text="*", width=12, height=1, highlightbackground=color, font=font,
                 command=lambda: mul()). \
    pack(side=LEFT, padx=5, pady=5)

btn_div = Button(top_third, text="/", width=12, height=1, highlightbackground=color, font=font,
                 command=lambda: div()). \
    pack(side=LEFT, padx=5, pady=5)

# =================== entries and labels ===================

label_first_num = Label(top_first, text="insert first number ===> ", bg=color, font=font)
label_first_num.pack(side=LEFT, padx=10, pady=10)

first_num = Entry(top_first, textvariable=num1, highlightbackground=color, font=font).pack(side=LEFT, padx=10, pady=10)

label_second_num = Label(top_second, text="insert second number ===> ", bg=color, font=font)
label_second_num.pack(side=LEFT, padx=5, pady=5)

second_num = Entry(top_second, textvariable=num2, highlightbackground=color, font=font).pack(side=LEFT, padx=10,
                                                                                             pady=10)

label_result_num = Label(top_forth, text="RESULT ===> ", bg=color, font=font)
label_result_num.pack(side=LEFT, padx=10, pady=10)

result_num = Entry(top_forth, textvariable=res_value, highlightbackground=color, font=font).pack(side=LEFT, padx=10,
                                                                                                 pady=10)

# =================== * ===================
root.mainloop()
