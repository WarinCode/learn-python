# ข้อ 1
Amount = float(input("จำนวนเงินที่ซื้อ >> "))
Membership = input("เป็นสมาชิก (y/n) >> ")
isMembership = Membership == "y" or Membership == "y".upper()

def Discount(percentage , discount):
    if Amount > 5000 and isMembership: percentage = 20
    elif Amount > 5000 and not isMembership: percentage = 10
    else: percentage = 5    
    discount = Amount * ((100 - percentage) / 100)
    return f'คุณได้รับส่วนลด 20% = {(Amount - discount):,.2f}\nยอดเงินที่ต้องจ่ายคือ = {discount:,.2f}'
print(Discount(0 , 0))