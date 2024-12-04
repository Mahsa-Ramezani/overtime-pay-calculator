def computepay(h,r):
     if(h<= 40):
         pay=r*h
     elif(h>40):
         p1=h*r
         p2=(h-40.0)*(r*0.5)
         pay=p1+p2
     return pay
hrs=input("Enter Hours:")
hrs=float(hrs)
rate=input("Enter Rate:")
rate=float(rate)
x=computepay(hrs,rate)
print("Pay",x)
