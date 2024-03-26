from tkinter import ttk , Tk , StringVar , IntVar , mainloop
from tkinter.ttk import Combobox , Checkbutton , Radiobutton , Button
from tkinter.scrolledtext import ScrolledText

#Insert ScrollText
def btnFood_clicked():
    txtOrder.insert('1.0' , f'{selFood.get()}\n')

#Clear ScrollText
def btnClear_clicked():
    txtOrder.delete('1.0' , "end")
    txtDetail.delete('1.0' , "end")
    
# แก้ไขรายละเอียดและการจ่ายเงิน
def edit_detail():
    # ตรวจสอบส่วนรายละเอียด
    strDetail = ""
    if cWarm.get() == 1:
        strDetail += "อ่น, "
    if cBag.get() == 1:
        strDetail += "รับถุง, "
    if cSpoon.get() == 1:
        strDetail += "รับช้อน, "
    
    # ตรวจสอบวิธีการจ่ายเงิน
    strPay = ""
    if rPay.get() == "cash":
        strPay = 'เงินสด'
    elif rPay.get() == "tran":
        strPay = 'เงินโอน'
    
    # ล้างข้อมูลรายละเอียดและการจ่ายเงิน
    txtDetail.delete('1.0' , "end")
    strDetail = strDetail + "\n" + strPay
    txtDetail.insert('1.0' , strDetail)

# Main Program
root = Tk()
root.title("Food Order")
root.geometry("600x400")

# สร้าง ComboBox
foodlist = ['ข้าวขาหมู' , 'ข้าวหมูแดง' , 'ข้าวมันไก่']
selFood = StringVar()
cwbFood = Combobox(root , values=foodlist ,textvariable=selFood)
# cwbFood['values'] = foodlist
cwbFood.place(y=20,x=20)

# สร้างปุ่มบันทึกรายการอาหาร
btnFood = Button(root , text='บันทึกรายการ' , command=btnFood_clicked)
btnFood.place(y=20 , x=200)

# สร้างปุ่มล้างรายการอาหาร
btnClear = Button(root , text="ล้างรายการ" , command=btnClear_clicked)
btnClear.place(y=60,x=200)

# สร้าง ScrolledText รายการอาหาร
txtOrder = ScrolledText(root , width=30 , height=10)
txtOrder.place(y=20,x=300)

# สร้าง CheckBox รายละเอียด
cWarm = IntVar()
chkWarm = ttk.Checkbutton(root , text='อุ่น' , command=edit_detail , variable=cWarm)
chkWarm.place(y=200 , x=20)
cBag = IntVar()
chkBag = Checkbutton(root , text='รับถุง' , command=edit_detail , variable=cBag)
chkBag.place(y=200 , x=100)
cSpoon = IntVar()
chkSpoon = Checkbutton(root , text='รับช้อน' , command=edit_detail , variable=cSpoon)
chkSpoon.place(y=200 , x=180)

# สร้าง Radio การจ่ายเงิน
rPay = StringVar()
rdoCash = Radiobutton(root , text='เงินสด',value='cash' ,variable=rPay , command=edit_detail)
rdoCash.place(y=260 , x=20)
rdoTran = Radiobutton(root , text='เงินโอน',value='tran' ,variable=rPay , command=edit_detail)
rdoTran.place(y=260 , x=100)

# สร้าง ScrolledText รายละเอียด
txtDetail = ScrolledText(root , width=30 , height=5)
txtDetail.place(y=200 , x=300)
mainloop()