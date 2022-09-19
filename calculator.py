from tkinter import*
root=Tk()
root.title("Calculator")
e=Entry(root,width=50,borderwidth=10)
e.grid(row=0,column=0,columnspan=4)
def button_click(num):
    current=e.get()
    if current=="+":
        current=""
    e.delete(0,END)
    e.insert(0,str(current)+str(num))
def button_add():
    global ans
    ans=int(e.get())
    e.delete(0,END)
    e.insert(0,"+")
def button_clear():
    e.delete(0,END)
def button_equal():
    x=ans+int(e.get())
    e.delete(0,END)
    e.insert(0,x)
    
Button9=Button(root,text=9,padx=40,pady=20,command=lambda: button_click(9))
Button8=Button(root,text=8,padx=40,pady=20,command=lambda: button_click(8))
Button7=Button(root,text=7,padx=40,pady=20,command=lambda: button_click(7))
Button6=Button(root,text=6,padx=40,pady=20,command=lambda: button_click(6))
Button5=Button(root,text=5,padx=40,pady=20,command=lambda: button_click(5))
Button4=Button(root,text=4,padx=40,pady=20,command=lambda: button_click(4))
Button3=Button(root,text=3,padx=40,pady=20,command=lambda: button_click(3))
Button2=Button(root,text=2,padx=40,pady=20,command=lambda: button_click(2))
Button1=Button(root,text=1,padx=40,pady=20,command=lambda: button_click(1))
Button0=Button(root,text=0,padx=40,pady=20,command=lambda: button_click(0))
Button_a=Button(root,text="+",width=10,pady=20,command=lambda: button_add())
Button_c=Button(root,text="clear",width=10,pady=52,command=lambda: button_clear())
Button_e=Button(root,text="=",padx=87,pady=20,command=lambda: button_equal())

Button9.grid(row=1,column=2)
Button8.grid(row=1,column=1)
Button7.grid(row=1,column=0)

Button6.grid(row=2,column=2)
Button5.grid(row=2,column=1)
Button4.grid(row=2,column=0)

Button3.grid(row=3,column=2)
Button2.grid(row=3,column=1)
Button1.grid(row=3,column=0)

Button0.grid(row=4,column=0)
Button_a.grid(row=3,column=3)
Button_c.grid(row=1,column=3,rowspan=2)
Button_e.grid(row=4,column=1,columnspan=2)

root.mainloop()