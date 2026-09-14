
#سوال 1:برنامه ای بنویسید که از لیست زیر عدد 8 را پیدا کرده و به 80 تغییر دهد 
#(برای پیدا کردن عدد مورد نظر از متد های خود لیست استفاده شود )
list1=[1,5,50,3,8,90]
list1.pop(list1.index(8))
list1.insert(4,80)
print(list1)


print("*"*100)


# سوال 2:در لیستدزیر بعد از عدد 6000عدد 7000 را اضافه کنید
list1=[10,20,[300,400,[5000,6000],500],30,40]
list1[2][2].insert(2,7000)
print(list1)

#سوال3:برنامه ای بنویید که یک عدد از کاربر گزفته و آن را به صورت اعداد فارسی نمایش دهد 
#راهنمایی:از استرسنگ ها کمک بگیرید 
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
#سوال 4: عددی که هم بر 2 و هم بر 3 بخش پذیر باشد بر 6 هم بخش پذیر است 
Adad=int(input("Enter your number:"))
if Adad%2==0 and Adad%3==0:
    print(" It is divisible by 6 ")
else:
    print(" It is not divisible by 6")


#سوال 5: یک یوزرنیم و یه پسورد از قبل ذخیره کنید سپس از کاربر یوزرنیم و پسورد بپرسید 
#اگر با یوزرنیم و پسورد اصلی مطابقت داشت ولکام نمایش دهد 


#سوال6:گرید کاربر را پرسیده و بزه نمره او را نمایش دهید 


