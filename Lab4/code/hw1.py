# ข้อ 1
Amount = float(input("จำนวนเงินสินค้าที่ซื้อ >> "))
Membership = input("คุณเป็นสมาชิกหรือไม่ >> ")
Discount = None
d = None

def funcDiscount(amount , percent):
    # https://brandinside.asia/how-to-calculate-percent-in-daily-life
    return amount * ((100 - percent) / 100)

if Amount > 5000 and (Membership == "Y" or Membership == "y"):
    d = 20
    Discount = funcDiscount(Amount , 20)
elif Amount > 5000 and (Membership == "N" or Membership == "n"):
    d = 10
    Discount = funcDiscount(Amount , 10)
else:
    d = 5
    Discount = funcDiscount(Amount , 5)
    
print(f"คุณซื้อสินค้าในราคา {Amount:,} บาท คุณได้ส่วนลด {d}% ราคาที่ต้องจ่ายจริงคือ {Discount:,.2f}")