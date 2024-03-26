# 1.กู้เงิน ดอกเบี้ย ร้อยละ 2 ต่อเดือน 
rate = 0.02
loan = eval(input("จำนวนเงินที่คุณต้องการกู้ >> "))
month = int(input("จำนวนเดือนที่ต้องการจะชำระ >> "))
intr = loan * rate 
pay = (loan / month ) + intr
all = pay * month
li = [f'ดอกเบี้ยเดือนละ {int(intr):,} บาท' , f'ต้องจ่ายเงินพร้อมดอกเบี้ยเดือนละ {int(pay):,} บาท' , f'รวมจ่ายเงินทั้งมด {int(pay):,} บาท']
print(*li , sep='\n')