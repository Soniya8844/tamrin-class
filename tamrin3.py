
#سوال3:برنامه ای بنویسید که یک عدد از کاربر گرفته مشخص کند عدد کامل است یا خیر 

number=int(input("enter your number:"))

sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if sum==number:
    print("wonderful number!")
else:
    print("usaull number")

print("="*50)

#سوال 2: با استفاده از حلقه یک لیست را به صورت برعکس در لیست دیگر ذخیره کنید

list1=[3,6,9,12]
list2=[]
for i in range(4):
    list2.append(-1)

print(list2)

print("="*50)

#سوال3: سری فیبوناچی   

n=int(input("enter your number:"))
a=0
b=1
for i in range(n):
    print(n)
    c=a+b

