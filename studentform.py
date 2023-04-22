from tkinter import*
base = Tk()
base.geometry('500x500')
base.title("Student form")

L1=Label(base,text="Student form",width=20,font=("bold",10))
L1.place(x=90,y=63)

L2=Label(base,text="Name",width=20,font=("bold",10))
L2.place(x=90,y=93)
e1=Entry(base)
e1.place(x=240,y=93)

L3=Label(base,text="Phonenumber",width=20,font=("bold",10))
L3.place(x=90,y=123)
e2=Entry(base)
e2.place(x=240,y=123)

L4=Label(base,text="E-mail",width=20,font=("bold",10))
L4.place(x=90,y=153)
e3=Entry(base)
e3.place(x=240,y=153)

L6=Label(base,text="Gender",width=20,font=("bold",10))
L6.place(x=90,y=183)
vars = IntVar()
Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=200, y=183)
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=260,y=183)
Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=320,y=183)

L6=Label(base,text="Age",width=20,font=("bold",10))
L6.place(x=90,y=213)
e4=Entry(base)
e4.place(x=240,y=213)

Button(base,text="Submit",width=20,font=("bold",20)).place(x=340,y=260)

base.mainloop()

print("Registered Sucessfully")