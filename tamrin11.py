#سوال1:تابعی بنویسید که تعداد ضلع را از کاربر بگیرد مثلا ان و ان ضلعی منتظم بسازد 

import turtle as tr 

win=tr.Screen()

win.title("soniya")

win.bgcolor("blue")

pen=tr.Turtle()
pen.shape("turtle")
pen.color("white")
pen.pensize(6)
pen.pencolor("white")



def shaping(n):
    for i in range(n):
        pen.forward(150)
        pen.left(360/n)


n=int(input("enter number your shape:"))


win.mainloop()
