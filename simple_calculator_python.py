import tkinter as tk

root=tk.Tk()
root.title("calculator")
root.geometry("405x405") 
root.configure(background="black")
root.iconbitmap(r'ic.ico') 

def clears():
    eny.delete(0,"end")
eny=tk.Entry(root,fg="white",bg="black",width=59,borderwidth=21)
eny.grid(rowspan=4,columnspan=4)
nine=tk.Button(root,text="9",width=10,height=3,fg="black",bg="grey",font=('Arial', 12),command=lambda : eny.insert("end","9"))
nine.grid(row=4,column=0,sticky="w",pady=10) 
eight=tk.Button(root,text="8",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","8"))
eight.grid(row=4,column=1,sticky="w",pady=10)
seven=tk.Button(root,text="7",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","7"))
seven.grid(row=4,column=2,sticky="w",pady=10)
plus=tk.Button(root,text="+",width=10,height=3,fg="black",bg="goldenrod",font=12,command=lambda : eny.insert("end","+"))
plus.grid(row=4,column=3,sticky="w",pady=10)
six=tk.Button(root,text="6",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","6")) 
six.grid(row=5,column=0,sticky="w",pady=10)
five=tk.Button(root,text="5",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","5"))
five.grid(row=5,column=1,sticky="w",pady=10)
four=tk.Button(root,text="4",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","4"))
four.grid(row=5,column=2,sticky="w",pady=10)
minus=tk.Button(root,text="-",width=10,height=3,fg="black",bg="goldenrod",font=12,command=lambda : eny.insert("end","-"))
minus.grid(row=5,column=3,sticky="w",pady=10)
three=tk.Button(root,text="3",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","3"))
three.grid(row=6,column=0,sticky="w",pady=10)
two=tk.Button(root,text="2",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","2"))
two.grid(row=6,column=1,sticky="w",pady=10)
one=tk.Button(root,text="1",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","1"))
one.grid(row=6,column=2,sticky="w",pady=10)
mul=tk.Button(root,text="*",width=10,height=3,fg="black",bg="goldenrod",font=12,command=lambda : eny.insert("end","*"))
mul.grid(row=6,column=3,sticky="w",pady=10)
zero=tk.Button(root,text="0",width=10,height=3,fg="black",bg="grey",font=12,command=lambda : eny.insert("end","0"))
zero.grid(row=7,column=1,sticky="w",pady=10)
clear=tk.Button(root,text="CLS",width=10,height=3,fg="white",bg="#383A3A",font=12,command=clears)
clear.grid(row=7,column=0,sticky="w",pady=10)
point=tk.Button(root,text="=",width=10,height=3,fg="white",bg="#383A3A",font=12,command=lambda : eny.insert("end","="))
point.grid(row=7,column=2,sticky="w",pady=10)
div=tk.Button(root,text="/",width=10,height=3,fg="black",bg="goldenrod",font=12,command=lambda : eny.insert("end","/"))
div.grid(row=7,column=3,sticky="w",pady=10)
clears()
root.mainloop()