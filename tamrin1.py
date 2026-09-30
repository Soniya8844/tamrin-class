#سوال1:یک کلمه از حرف اول،وسط و اخر کلمه بسازید و در خروجی نمایش دهید 
# (International)

word="International"
First_word=word[0]
Middle_word=word[len(word)//2]
Last_word=word[-1]
new_word=First_word+Middle_word+Last_word
print(new_word)



print("="*50)

#سوال2:استیرینگ داده شده را وسط استرینگ اول اضافه و در خروجی نمایش دهید 
#str1="python"
#str2="programing"

str1="python"
str2="programing"
str3=len(str1)//2
str4=str1[:str3]+str2+str1[str3:]
print(str4)


print("="*50)

#سوال3:رشته داده شده را به گونه ای در خروجی چاپ کنید که حروف کوچک ابتدا و حروف بزرگ انتها باشند
#DjAnGOFraMeWorK


print("="*50)

#سوال4:یک متن دلخواه از ویکی پدیا را تمیز کنید و تهداد کلمه های آن را نمایش دهید 

text=""" Albert Einstein[a] (14 March 1879 – 18 April 1955) was a German-born theoretical physicist best
known for developing the theory of relativity. Einstein also made important contributions to quantum theory.
[1][5] His mass–energy equivalence formula E = mc2, which arises from special relativity, has been called 
"the world's most famous equation".[6] He received the 1921 Nobel Prize in Physics for "his services to 
theoretical physics, and especially for his discovery of the law of the photoelectric effect".[7]"""

text=text.replace("]","")
text=text.replace("[","")
text=text.replace("1","")
text=text.replace("2","")
text=text.replace("3","")
text=text.replace("4","")
text=text.replace("5","")
text=text.replace("6","")
text=text.replace("7","")
text=text.replace("8","")
text=text.replace("9","")
text=text.replace("0","")
text=text.replace(":","")
text=text.replace(",","")
text=text.replace(")","")
text=text.replace("(","")
text=text.replace("/","")

print(text)
print(text.split)
