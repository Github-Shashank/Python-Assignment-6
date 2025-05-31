from tkinter import *
import tkinter.messagebox

window = Tk()
window.title("Calculator")
window.geometry("320x250")

e = Entry(window,width=49,borderwidth=10)
e.place(x=0,y=0)

def click(n):
    previous_value = e.get()
    e.delete(0,END)
    e.insert(0,previous_value+str(n))
    pass

b = Button(window,text="1",width=12,command=lambda:click(1))
b.place(x=10,y=50)

b = Button(window,text="2",width=12,command=lambda:click(2))
b.place(x=110,y=50)

b = Button(window,text="3",width=12,command=lambda:click(3))
b.place(x=210,y=50)

b = Button(window,text="4",width=12,command=lambda:click(4))
b.place(x=10,y=80)

b = Button(window,text="5",width=12,command=lambda:click(5))
b.place(x=110,y=80)

b = Button(window,text="6",width=12,command=lambda:click(6))
b.place(x=210,y=80)

b = Button(window,text="7",width=12,command=lambda:click(7))
b.place(x=10,y=110)

b = Button(window,text="8",width=12,command=lambda:click(8))
b.place(x=110,y=110)

b = Button(window,text="9",width=12,command=lambda:click(9))
b.place(x=210,y=110)

b = Button(window,text="0",width=12,command=lambda:click(0))
b.place(x=10,y=140)

def add():
    global pre_val,opr
    pre_val = int(e.get())
    opr = 'add'
    e.delete(0,END)

b = Button(window,text="+",width=12,command=lambda:add())
b.place(x=110,y=140)

def sub():
    global pre_val,opr
    pre_val = int(e.get())
    opr = 'sub'
    e.delete(0,END)

b = Button(window,text="-",width=12,command=lambda:sub())
b.place(x=210,y=140)

def mul():
    global pre_val,opr
    pre_val = int(e.get())
    opr = 'mul'
    e.delete(0,END)

b = Button(window,text="*",width=12,command=lambda:mul())
b.place(x=10,y=170)

def div():
    global pre_val,opr
    pre_val = int(e.get())
    opr = 'div'
    e.delete(0,END)

b = Button(window,text="/",width=12,command=lambda:div())
b.place(x=110,y=170)


def equal(): 
    global pre_val,opr
    cur_val = int(e.get())
    e.delete(0,END)
    if cur_val == 0 and opr == "div":
        tkinter.messagebox.showwarning("ZeroDivisionError","Cannot divide by zero")
    else:
        if opr == "add":
            e.insert(0,pre_val + cur_val)
        elif opr == "sub":
            e.insert(0,pre_val - cur_val)
        elif opr == "mul":
            e.insert(0,pre_val * cur_val)
        elif opr == "div":
            e.insert(0,pre_val / cur_val)

b = Button(window,text="=",width=12,command=lambda:equal())
b.place(x=210,y=170)

def clear():
    e.delete(0,END)

b = Button(window,text="Clear",width=20,command=lambda:clear())
b.place(x=80,y=200)

mainloop()