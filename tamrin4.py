#یک جدول ضرب 9*9 چاپ کنید .

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end="\t")
    print()

print("="*60)

#برنامه ای بنویسید که دو عدد از کاربر بگیرد و از عدد کوچکتر تا عدد برگتر 
#اعداد اول ما بین آن دو عدد را بیابد و در یک لیست ذخیره کند 

number1=int(input("Enter your number:"))
number2=int(input("Enter your number:"))
lst=[]
for i in range(number1,number2+1):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==0 and i>=2:
        lst.append(i)
print(lst)
        
print("="*60)

#لیست زیر را درست کنید .
#a=[1,[2,3,[4,5,6],7,8],9]
#output=[1,2,3,4,5,6,7,8,9]

a=[1,[2,3,[4,5,6],7,8],9]
b=[]
for i in a:
    if type(i)==int:
        b.append(i)
    else:
        for j in i:
            if type(j)==int:
                b.append(j)
            else:
                for k in j:
                    if type(k)==int:
                        b.append(k)
print(b) 

print("="*60)

#colors=["red","blue","crimson","blue","green","crimson","crimson","purple","blue","pink",
#"white","pink","pink"]
#برنامه ای بنویسید که رنگ های تکراری را از لیست حذف کند .
 
colors=["red","blue","crimson","blue","green","crimson","crimson","purple","blue","pink",
"white","pink","pink"]
colors2=[]
for i in colors:
    if i not in colors2:
        colors2.append(i)
print(colors2)

print("="*60)
