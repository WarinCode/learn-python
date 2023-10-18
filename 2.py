# ข้อ 2
days = 0
_sum = 0
isZeroNumber = 1
while isZeroNumber != 0:
    days += 1
    liters = int(input(f'Day {days} : Filling Fuel : '))
    _sum += liters
    isZeroNumber = liters
print(f'Average Filling Fuel of month : {(_sum / days):,.2f}')