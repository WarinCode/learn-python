import tkinter as tk
from tkinter import ttk , Tk

root = Tk()
root.title("Fundamental Tkinter")
root.geometry('380x250')

showNumbers = tk.StringVar()
string = ''
def btn_clicked(theNum):
    global showNumbers
    global string
    string += str(theNum)
    showNumbers.set(string)
    
def clear():
    global string
    string = ''
    showNumbers.set(string)
    
txtAll = ttk.Entry(root,textvariable=showNumbers)
txtAll.grid_configure(row=1, column=2 ,padx=20,pady=20)
txtAll.config(width=13 ,font=10)
btn1 = ttk.Button(root,text='1',command=lambda:btn_clicked(1)).grid(row=2,column=1,padx=15 , pady=10)
btn2 = ttk.Button(root,text='2',command=lambda:btn_clicked(2)).grid(row=2,column=2,padx=15 , pady=10)
btn3 = ttk.Button(root,text='3',command=lambda:btn_clicked(3)).grid(row=2,column=3,padx=15 , pady=10)
btn4 = ttk.Button(root,text='4',command=lambda:btn_clicked(4)).grid(row=3,column=1,padx=15 , pady=10)
btn5 = ttk.Button(root,text='5',command=lambda:btn_clicked(5)).grid(row=3,column=2,padx=15 , pady=10)
btn6 = ttk.Button(root,text='6',command=lambda:btn_clicked(6)).grid(row=3,column=3,padx=15 , pady=10)
btn7 = ttk.Button(root,text='7',command=lambda:btn_clicked(7)).grid(row=4,column=1,padx=15 , pady=10)
btn8 = ttk.Button(root,text='8',command=lambda:btn_clicked(8)).grid(row=4,column=2,padx=15 , pady=10)
btn9 = ttk.Button(root,text='9',command=lambda:btn_clicked(9)).grid(row=4,column=3,padx=15 , pady=10)
btnReset = ttk.Button(root , text='ลบ' , command=lambda:clear()).grid(row=5,column=2,padx=15 , pady=10)
root.mainloop()