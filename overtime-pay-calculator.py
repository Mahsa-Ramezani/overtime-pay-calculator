hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter Rate:")
rate = float(rate)
if hrs<=40 :
    pay = hrs*rate
elif hrs>40 :
    x = hrs-40
    p = 40*rate
    pay = rate * 1.5 * x + p
print(pay)
