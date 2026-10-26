# سوال 1:برنامه ای برای تولید اعداد مثلث خیام - پاسکال
#(n,k)=n!/k!(n-k!)
""""
            1
         1    1
       1    2    1
    1    3     3    1
1     4     6     4     1

"""""
def KHP(n):
    if n==1:
        return [1]
    farakhan=KHP(n-1)     #تابع را با یک عدد کمتر اجرا میکند 
    radif=[1]             #هر مثلث خیام پاسکال با عدد 1 شروع می شود
    for i in range(len(farakhan)-1):        #حلقه را با یکی کمتر اجرا میکند 
        radif.append(farakhan[i]+farakhan[i+1])
    radif.append(1)             #عدد یک را به انتهای سطر اضافه میکند 
    return radif

n=int(input("enter your number:"))

if n>=1:
    KHP(n)


print("*"*50)


#سوال2:برنامه ای بنویسید که انتخاب غیر تکراری از یک لیست داشته باشد بدون استفاده از 
#sample

import random as rn
lst=[1,3,5,4,7,8,9,6,4,2,12,3,1,7,5,4]
num=int(input("enter a number:"))
lst2=[]
while len(lst2)<num:       #تا زمانی که تعداد اعضای لیست 2 از نام کمتر باشد دستورات حلقه اجرا میشود 
    a=rn.choice(lst)

    if a not in lst2:
        lst2.append(a)

print(lst2)

print("*"*50)


#سوال4:بازی سنگ کاغذ قیچی

import random as rn 

Entekhab=["سنگ","کاغذ","قیچی"]
computer=rn.choice(Entekhab)
Karbar=input("سنگ ، کاغذ یا قیچی؟")
print("انتخاب کامپیوتر:",computer)
if Karbar==computer:
    print("مساوی شد ")
elif Karbar=="سنگ" and computer=="قیچی":
    print("تو برنده شدی")
elif Karbar=="کاغذ" and computer=="سنگ":
    print("تو برنده شدی")
elif Karbar=="قیچی"and computer=="کاغذ":
    print("تو برنده شدی")
else:
    print("کامپیوتر برنده شد")


print("*"*50)


#سوال4:بازی حدس عدد 

import random as rn


computer = rn.randint(1, 10)

Karbar = int(input("Guess number: "))

while Karbar != computer:
    if Karbar > computer:
        print("Your number is bigger!")
    else:
        print("Your number is smaller!")

    Karbar = int(input("Guess again: "))

print("You win!")


print("*"*50)


#سوال5:تابعی بنویسید که اعداد لیست زیر را با هم جمع کند
#[10,9,6,5,20,1]

def summ(num):
    return sum(num)

num=[10,9,6,5,20,1]

print(summ(num))


print("*"*50)

#تابعی بنویسید که اعداد لیستن زیر را با یکدیگر ضرب کند 
#[10,9,6,5,20,1]

