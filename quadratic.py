#IanNolon
#1/31/18
#quadratic.py

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

if (b**2 - (4*a*c)) < 0:
    d = (((4*a*c) - b**2)**0.5)
    e = (((4*a*c) - b**2)**0.5)
    print("The answers are")
    print((-b/4), '+', d/4, 'i')
    print((-b/4), '-', e/4, 'i')
else:
    x1 = (-b + (b**2 - (4*a*c))**0.5)/(2*a)
    x2 = (-b - (b**2 - (4*a*c))**0.5)/(2*a)
    
    print("The answers are")
    print(x1 , x2)
