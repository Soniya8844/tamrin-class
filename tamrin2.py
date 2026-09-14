
#سوال1:برنامه ای بنویسید که از لیست زیر عدد 8 را پیدا کرده
# .( برای پیدا کردن عدد مورد نظر از متد های خودلیست  استفاده کنید.) و به 80 تغییر دهید 
List1=[1,5,50,3,8,90]
lst=List1.index(8)
List1.remove(8)
List1.insert(-2,80)
print(List1)

print("="*60)

# .سوال 2 :در لیست زیر بعد از عدد6000 عدد 7000 را اضافه کنید
 
#                       0    1
#               0   1      2       3      
List2=[10,20,[300,400,[5000,6000],500],30,40]
#       0  1      2         3      4    5  6
List2[2][2].append(7000)
print(List2)

print("="*60)

#سوال3: برنامه ای بنویسید که یک عدد از کاربر گرفته و
# . آن را به صورت اعداد فارسی نمایش دهد 
#راهنمایی : از استرینگ ها کمک بکیرید

Number=input("Enter your number:")
Number=Number.replace("0","\u06F0")
Number=Number.replace("1","\u06F1")
Number=Number.replace("2","\u06F2")
Number=Number.replace("3","\u06F3")
Number=Number.replace("4","\u06F4")
Number=Number.replace("5","\u06F5")
Number=Number.replace("6","\u06F6")
Number=Number.replace("7","\u06F7")
Number=Number.replace("8","\u06F8")
Number=Number.replace("9","\u06F9")
print(Number)

print("="*60)

#سوال 4:عددی که هم بر 2 و هم بر 3 بخش پذیر باشد بر 6 هم بخش پذیر است 

Adad=int(input("Enter your number:"))
if Adad%2==0 and Adad%3==0:
    print(" It is divisible by 6 ")
else:
    print(" It is not divisible by 6")


print("="*60)


#سوال 5:یک یوزرنیم و پسورد از قبل ذخیره کنید سپس از کاربر یوزرنیم 
# .و پسورد بپرسید اگر با دو مقدار قبلی یکی بود به کاربر ولکام نمایش دهید 

Username="403645814"
Password="soniya"
New_Username=input("please enter your username:")
New_Password=input("please enter your password:")
if Username==New_Username and Password==New_Password:
    print("Welcome")
else:
    print("Username or Password is wrong")


print("="*60)

#سوال6: گرید کاربر را پرسیده و بازه نمره او را نمایش دهید.

grade=input("Enter your grade:")
if grade=="A" or grade=="a" :
    print("your score is between 17 and 20")
elif grade=="B" or grade=="b":
    print("your score is between 14 and 17")
elif grade=="C" or grade=="c":
    print("your score is between 10 and 14")
elif grade=="D" or grade=="d":
    print("you failed!")
else:
    print("please enter your grade correctly")