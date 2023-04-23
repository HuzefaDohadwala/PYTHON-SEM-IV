from tkinter import *

def get_value():
    value= e1.get() + '\n'+ e2.get() + '\n'+ e3.get() + '\n'+ e4.get() + str(vars.get())
    l6 = Label(root,text=value)
    l6.place(x=700,y=200)

root = Tk()
root.title("Student Form")

l1 = Label(root,text="Student from")
l1.place(x=600,y=10)

l2 = Label(root,text="Name")
l2.place(x=400,y=40)
e1 = Entry(root)
e1.place(x=500,y=40)

l3 = Label(root,text="Phone number")
l3.place(x=400,y=70)
e2 = Entry(root)
e2.place(x=500,y=70)

l4 = Label(root,text="E-mail")
l4.place(x=400,y=110)
e3 = Entry(root)
e3.place(x=500,y=110)

l5 = Label(root,text="Age")
l5.place(x=400,y=150)
e4 = Entry(root)
e4.place(x=500,y=150)

vars =StringVar()
Radiobutton(root,text="Male",variable=vars,value="male").place(x=500,y=175)
Radiobutton(root,text="Female",variable=vars,value="Female").place(x=550,y=175)

b1 = Button(root,text="Submit",command=get_value)
b1.place(x=600 , y = 200)

root.mainloop()