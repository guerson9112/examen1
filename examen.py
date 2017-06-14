from tkinter import *
import math
import turtle


def btnClick(numbers):
    global operator
    global dibujo
    if numbers==1:
        

        
        print("ingrese el numero de lados MAYOR DE 2")
        l=int(input(""))
         
        print("ingrese la longitud de un lado")
        d=int(input(""))
        print("Su perimetro es]: ")
        per=d*l
        print(per)
        c=l/2
        e=l**2-c**2
        ap=math.sqrt(e)
        perimetro=str(per)
        area=str((per*ap)/2)
        print("Su area es: ")
        print(area)
        dibujo=l
        dibujar(dibujo)
       
        operator="area: "+area+" perimetro: "+perimetro
        text_Input.set(operator)
    
        
        
def dibujar(n):
    t=turtle.Pen()
    if n%2==1:
        for x in range(0,n):
            t.forward(100)
            t.left(360/n)
    else:
        for x in range(0,n):
            t.forward(100)
            t.left(360/n)
    
    
  
cal= Tk()
cal.title("EXAMEN")
operator=""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 0, 'bold'), textvariable=text_Input, bd=30, insertwidth=40,
                   bg="powder blue", justify='right').grid(columnspan=4)

btn7=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="1", bg="blue", command=lambda:btnClick(1)).grid(row=1, column=0)

btn8=Button(cal, padx=16, bd=8,activebackground="green", fg="black", font=('arial', 20, 'bold'),
            text="2", bg="blue", command=lambda:btnClick(2)).grid(row=1, column=1)




cal.mainloop()
