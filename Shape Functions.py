#PERIMETER AND AREA OF VARIOUS SHAPES SUCH AS SQUARE, RECTANGLE, CIRCLE, TRIANGLE
import math as m
while True:
    print("\n1. Square     2. Rectangle\n3. Circle     4. Triangle")
    choice = int(input("Enter your choice: "))
    def square():
        print("Perimeter of square is : ",side*4)
        print("Area of square is : ",side*side)
    def rectangle():
        print("Perimeter of rectangle is : ",2*(len+wid))
        print("Area of rectangle is : ",len*wid)
    def circle():
        print("Perimeter of rectangle is : ",round(2*m.pi*rad,3))
        print("Area of rectangle is : ",round(m.pi*rad*rad,3))
    def triangle():
        print("Perimeter of triangle is : ",a+b+c)
        s=(a+b+c)/2
        print("Area of triangle is : ",round((s*(s-a)*(s-b)*(s-c)) ** 0.5,3))

    if choice == 1:
        side=float(input("enter side of square : "))
        square()
    elif choice == 2:
        len=float(input("enter length of rectangle : "))
        wid=float(input("enter width of rectange : "))
        rectangle()
    elif choice == 3:
        rad=float(input("enter radius of circle : "))
        circle()
    elif choice == 4:
        a=float(input("enter side 1 of triangle : "))
        b=float(input("enter side 2 of triangle : "))
        c=float(input("enter side 3 of triangle : "))
        triangle()
    else:
        print("WRONG INPUT!!")  