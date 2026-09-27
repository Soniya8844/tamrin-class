#سوال 1:برنامه ای بنویسید که مجموع ارقام هر عددی را حساب کند 

num=int(input("Enter your number:"))

sum=0
while num>0:
   sum=sum+num
print(sum)

print("="*50)

#سوال2:به روش لیست خروجی زیر را نمایش دهید  
#fnames = ("mojtaba", "benyamin", "sakineh")
#lnames = ('ghahri', "kachoue", "lopez")
#age = (39, 21, 14)
#خروجی ==>  [("mojtaba", "ghahri", 39), ("benyamin", "kachoue", 21), ("sakineh", "lopez", 14)]

fnames = ("mojtaba", "benyamin", "sakineh")
lnames = ('ghahri', "kachoue", "lopez")
age = (39, 21, 14)

lst=[]
for i in range(3):
    lst.append((fnames[i],lnames[i],age[i]))
print(lst)

print("="*50)


#سوال3:برنامه ای بنویسید که یک عدد از کاربر بگیرید اگر        
#عدد زوج / 2
#اگر فرد  *3 + 1 
#این چرخه انقدر ادامه یابد تا به عدد یک برسد 
#(حدس کولاتز)

number=int(input("Enter a number : "))
while number !=1:
    if number%2==0:
        number=number//2
    else:
        number=number*3+1
    print(number)


print("="*50)



#سوال4:آیتم های تکراری را از لیست زیر حذف کنید.با استفاده از حلقه 
#people = ["mojtaba", "mojtaba", "taghi", "naghi", "sakineh", "sara", "mojtaba", "mojtaba", "mojtaba", "mojtaba", "mojtaba"]

people = ["mojtaba", "mojtaba", "taghi", "naghi", "sakineh", "sara", "mojtaba", "mojtaba", "mojtaba", "mojtaba", "mojtaba"]

new_people=[]
for i in people:
    if i not in new_people:
        new_people.append(i)
print(new_people)