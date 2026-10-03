#سوال 1:تابعی بنویسید که عددی گرفته و مشخص کند عدد اول است یا خیر 

def prime(num):
    flag=0
    for i in range(2,num):
        flag+=1
    if flag==0:
        return True
    else:
        return False

print(prime(45))
print(prime(13))


print("0"*50)


#سوال2:تابعی بنویسید که عددی گرفته و مشخص کند کامل است یا خیر 

def kamel(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=1
    if sum==num:
        return True
    else:
        return False

print(kamel(543))
print(kamel(78))


print("0"*50)

#سوال3:عدد گرفته شده از کاربر را با کاراکتر اعداد فارسی چاپ کنید 
#(با کمک دیکشنری )
#"۰۱۲۳۴۵۶۷۸۹"

number=input("Enter a number:")

dic={"0":"۰","1":"۱","2":"۲","3":"۳","4":"۴","5":"۵","6":"۶","7":"۷","8":"۸","9":"۹"}

result=""
for i in number:
    result+=dic[i]
print(result)


print("0"*50)

#سوال4:تابعی بنویسید که یک عدد بکیرد و آن را مغلوب کند 
# 123 ====> 321

def maghloob(num):
    reverse=0
    while num !=0:
        remain=num%10
        reverse=reverse*10+remain
        num=num//10
    return reverse

print(maghloob(852))
print(maghloob(789))
