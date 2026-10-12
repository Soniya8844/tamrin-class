#سوال1:تابعی بنویسید که متن را بگیرید و تعداد حرف های کوچک و بزرگ آن را مشخص کند 


def tedad(txt):
    big=0
    small=0
    for i in txt:
        if i.islower():
            small+=1
        elif i.isupper():
            big+=1
    return small,big



print(tedad("""Maryam Mirzakhani (Persian:pronounced [mæɾˈjæm miːɾzɑːxɑːˈniː]; 12 May 1977 – 14 July 2017)
was an Iranian[4][5] mathematician and a professor of mathematics at Stanford University.
[6][7] Her research focused on hyperbolic geometry, dynamical systems, complex analysis,
and topology. In 2014, she was awarded the Fields Medal for her work in "the dynamics and 
geometry of Riemann surfaces and their moduli spaces", becoming the first woman and the first Iranian
citizen to win the prize.[8][9] Along with the Fields Medal, her work earned numerous honors,
including the Blumenthal Award, the Satter Prize, and the Clay Research Award."""))