#سوال 1: تابعی بنویسید که هر تعداد عددی که به آن میدهیم را با هم جمع کند 
#بدون استفاده از دستور  sum و list

def summ(*args):
    s = 0
    for i in args:
        s+=i
    return s

print(summ(10, 20, 5, 3, 2))

print("_"*50)

#سری فیبوناچی(با استفاده از تابع بازگشتی) 
#Fn=Fn-1+Fn-2



print("_"*50)

#تابع تقسیم (با استفاده از تابع بازگشتی)

def div(a, b):
    if a < b:
        return 0
    else:
        return 1 + div(a - b, b)

print(div(12, 3))

print("_"*50)

# تابعی بنویسید که بزرگترین عدد لیست را بیاید (تابع بازگشتی )

def max(a):
    if len(a) == 1:
        return a[0]
    b = max(a[1:])
    if a[0] > b:
        return a[0]
    return b

print(max([10, 90, 63, 52, 20, 11]))