# 3.แตก Bank
money = int(input("ระบุจำนวนเงินที่ต้องการจะแลก >>  "))
li = [500 , 100 , 50, 20, 1]
bank = {
    "m500": None,
    "m100": None,
    "m50":None,
    "m20":None,
    "balance":None
}
for idx , key in enumerate(bank):
    bank[key] = money // li[idx]
    money %= li[idx]
    print(f'ได้ธนบัตร {li[idx]} บาท =  {bank[key]} ใบ')
print(f'เหลือเงิน {bank["balance"]} บาท')