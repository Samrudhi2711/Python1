a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
if a < b:
    if b < c:
        print (a, "<", b, "<", c)
    else:
        if a < c:
            print (a, "<", c, "<", b)
        else:
            print (c, "<", a, "<", b)
else:
    if c < b:
        print (c, "<", b, "<", a)
    else:
        if c < a:
            print (b, "<", c, "<", a)
        else:
            print (b, "<", a, "<", c)