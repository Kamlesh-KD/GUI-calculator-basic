from tkinter import *
root=Tk()
root.title('My Calculator')

e=Entry(root, width=40, borderwidth=7)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(num):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(num))

def clear():
    e.delete(0, END)

def add():
    first_num=e.get()
    global operation
    operation='addition'
    global fn
    fn=float(first_num)
    e.delete(0, END)

def sub():
    first_num=e.get()
    global operation
    operation='subtraction'
    global fn
    fn=float(first_num)
    e.delete(0, END)

def div():
    first_num=e.get()
    global operation
    operation='division'
    global fn
    fn=float(first_num)
    e.delete(0, END)

def mul():
    first_num=e.get()
    global operation
    operation='multiplication'
    global fn
    fn=float(first_num)
    e.delete(0, END)

def equal():
    second_num=e.get()
    e.delete(0, END)
    global fn
    if operation=='addition':
        e.insert(0, fn + float(second_num))
        fn=fn+float(second_num)
    elif operation=='subtraction':
        e.insert(0, fn - float(second_num))
        fn=fn-float(second_num)
    elif operation=='multiplication':
        e.insert(0, fn * float(second_num))
        fn=fn*float(second_num)
    elif operation=='division':
        e.insert(0, fn / float(second_num))
        fn=fn/float(second_num)

button1 = Button(root, text='1', padx=20, pady=20, command=lambda: click(1))
button2 = Button(root, text='2', padx=20, pady=20, command=lambda: click(2))
button3 = Button(root, text='3', padx=20, pady=20, command=lambda: click(3))
button4 = Button(root, text='4', padx=20, pady=20, command=lambda: click(4))
button5 = Button(root, text='5', padx=20, pady=20, command=lambda: click(5))
button6 = Button(root, text='6', padx=20, pady=20, command=lambda: click(6))
button7 = Button(root, text='7', padx=20, pady=20, command=lambda: click(7))
button8 = Button(root, text='8', padx=20, pady=20, command=lambda: click(8))
button9 = Button(root, text='9', padx=20, pady=20, command=lambda: click(9))
button0 = Button(root, text='0', padx=20, pady=20, command=lambda: click(0))
buttondot=Button(root, text='.', padx=20, pady=20, command=lambda: click('.'))

buttonclear = Button(root, text='cls', padx=20, pady=20, command=clear)
buttonadd = Button(root, text='+', padx=20, pady=20, command=add)
buttonsub = Button(root, text='-', padx=20, pady=20, command=sub)
buttonmul = Button(root, text='*', padx=20, pady=20, command=mul)
buttondiv = Button(root, text='/', padx=20, pady=20, command=div)
buttonequal = Button(root, text='=', padx=100, pady=20, command=equal)

button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
buttonmul.grid(row=4, column=3)

button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
buttonsub.grid(row=3, column=3)

button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
buttonadd.grid(row=2, column=3)

button0.grid(row=5, column=0)
buttonclear.grid(row=5, column=1)
buttondiv.grid(row=5, column=2)
buttondot.grid(row=5, column=3)

buttonequal.grid(row=6, columnspan=4)


root.mainloop()
