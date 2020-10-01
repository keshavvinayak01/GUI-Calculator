from tkinter import *
import parser

root = Tk()

root.title('Calculator')
root.geometry("368x280")
root.maxsize(368,280)
root.minsize(368,280)

root.config(bg="grey")
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def clear_all():
    display.delete(0, END)


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def calcFact():
    try:
        number = int(display.get())
        res = 1
        for i in range(1, number + 1):
            res *= i
        clear_all()
        display.insert(0, res)

    except Exception:
        clear_all()
        display.insert(0, "Error")


display = Entry(root,font=("Helvetica", 19), borderwidth=5, relief=SUNKEN, justify=RIGHT)

display.grid(row=1, columnspan=6, sticky=W + E,padx=5,pady=5)
# adding buttons to the calculator
Button(root, text="1", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(1)).grid(row=2, column=0,ipadx=8,padx=2,pady=2)
Button(root, text="2", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(2)).grid(row=2, column=1,ipadx=8,padx=2,pady=2)
Button(root, text="3", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(3)).grid(row=2, column=2,ipadx=8,padx=2,pady=2)

Button(root, text="4", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(4)).grid(row=3, column=0,ipadx=8,padx=2,pady=2)
Button(root, text="5", bg='cyan',font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(5)).grid(row=3, column=1,ipadx=8,padx=2,pady=2)
Button(root,  text="6", bg='cyan',font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(6)).grid(row=3, column=2,ipadx=8,padx=2,pady=2)

Button(root, text="7", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(7)).grid(row=4, column=0,ipadx=8,padx=2,pady=2)
Button(root, text="8", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(8)).grid(row=4, column=1,ipadx=8,padx=2,pady=2)
Button(root,  text="9",bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(9)).grid(row=4, column=2,ipadx=8,padx=2,pady=2)

Button(root, text="AC", font=("arial", 16),fg='white',bg='#EF5350', borderwidth=5, command=lambda: clear_all()).grid(row=5, column=0,padx=2,pady=2,ipady=2,ipadx=2)
Button(root, text="0", bg='cyan', font=("Helvetica", 18), borderwidth=5, command=lambda: get_variables(0)).grid(row=5, column=1,ipadx=8,padx=2,pady=2)
Button(root, text="=", bg='orange', font=("Helvetica", 18), borderwidth=5, command=lambda: calculate()).grid(row=5, column=2,ipadx=8,padx=2,pady=2)

Button(root, text="+", fg='yellow',bg='#232b2b', font=("Helvetica", 18), borderwidth=5, command=lambda: get_operation("+")).grid(row=2, column=3,ipadx=8,padx=2,pady=2)
Button(root, text="-", fg='yellow',bg='#232b2b',font=("Helvetica", 18), borderwidth=5, command=lambda: get_operation("-")).grid(row=3, column=3,ipadx=11,padx=2,pady=2)
Button(root, text="x", fg='yellow',bg='#232b2b',font=("Helvetica", 18), borderwidth=5, command=lambda: get_operation("*")).grid(row=4, column=3,ipadx=9,padx=2,pady=2)
Button(root, text="/", fg='yellow',bg='#232b2b',font=("Helvetica", 18), borderwidth=5, command=lambda: get_operation("/")).grid(row=5, column=3,ipadx=11,padx=2,pady=2)

Button(root, text="pi",font=("Helvetica", 17), borderwidth=5, command=lambda: get_operation("3.14")).grid(row=2, column=4,ipadx=8,padx=2,pady=2)
Button(root, text="%", font=("Helvetica", 16), borderwidth=5,command=lambda: get_operation("%")).grid(row=3, column=4,ipadx=8,ipady=3,padx=2,pady=2)
Button(root, text="(",font=("Helvetica", 18), borderwidth=5, command=lambda: get_operation("(")).grid(row=4, column=4,ipadx=12,padx=2,pady=2)
Button(root, text="exp",font=("Helvetica bold", 10), borderwidth=5, command=lambda: get_operation("**")).grid(row=5, column=4,ipadx=9,ipady=9,padx=2,pady=2)

Button(root, text="<-",font=("Helvetica", 16), borderwidth=5, command=lambda: undo()).grid(row=2, column=5,ipadx=8,ipady=2,padx=2,pady=2)
Button(root, text="x!",font=("Helvetica", 16), borderwidth=5, command=lambda: calcFact()).grid(row=3, column=5,ipadx=8,ipady=2,padx=2,pady=2)
Button(root, text=")", font=("Helvetica", 18), borderwidth=5,command=lambda: get_operation(")")).grid(row=4, column=5,ipadx=10,padx=2,pady=2)
Button(root, text="^2",font=("Helvetica", 12), borderwidth=5, command=lambda: get_operation("**2")).grid(row=5, column=5,ipadx=9,ipady=7,padx=2,pady=2)

root.mainloop()
