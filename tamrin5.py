#سوال یک :سه عدد به عنوان طول ضلع های یک مثلث از کاریر بگیرید 
#بررسی کنید آیا این سه ضلع میتواند مثلث بستازد یا خیر 
#(شرط: مجموع هر دو ضلع باید بزرگ تر از ضلع سوم باشد )

a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))

if a+b>c and a+c>b and c+b>a:
    print("A triangle is formed")
else:
    print("A triangle is not formed")

#سوال 2:سه عدد ار کاربر بگیرید و مشخص کنید یزرگترین عدد کدام است ؟

num1=int(input("Enter number 1:"))   
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))

if num1>num2 and num1>num3:
    print("num1 is max number")
elif num2>num1 and num2>num3:
    print("num2 is max number")
else:
    print("num3 is max number")

#سوال3:یک سال از کاربر بگیرید  و بررسی کنید آیا سال کبیسه است یا خیر.
#(شرط: اگر بر 4 بخش پذیر باشد و بر 100 بخش پذیر نباشد ، یا بر 400 بخش پذیر باشد کبیسه است )

year=int(input("enter your year:"))
if year%4==0 or year%400==0:
    print("kabise year")
else:
    print("not kabise year")


#سوال 4:یک نمره 0 تا 20 ار کاربر بگیرید و وضعیت دانش آموز را مشخص کنید 
#اگر 0 تا 9:ضعیف           10 تا 14 : متوسط             15 تا 17 : خوب           17 تا 20 : عالی 

Score=int(input("Enter your Score:"))
if Score>=0 and Score<=9:
    print("Weak")
elif Score>=10 and Score<=14:
    print("Middle")
elif Score>=14 and Score<=17:
    print("good")
elif Score>=17 and Score<=20:
    print("Excellent")
else:
    print("pleas entrr corroct number")


#سوال 5:دو عدد و یک عملگر از کاربر بگیرید ،عملگر میتواند یکی از +،-،*،/ باشد 
#نتیجه را حساب کن و اگر عملگر ناشناخته بود پیام خطا چاپ کن 

a=int(input("enter your number1:"))
b=int(input("enter your number2:"))
am=input("enter your operator:")
c=0
if am=="+":
    a+b=c
elif am=="-":
    a-b=c
elif am=="*":
    a*b=c
elif am=="/":
    a/b=c
else:
    print("operator is wrong!!")