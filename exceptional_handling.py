def division():
    try:
        a=float(input("enter the a's value"))
        b=float(input("enter the b's value"))
        c=a/b
        print("divison of a and b is",c)
    except ZeroDivisionError:
        print("Error=number is divided by zero")
    except ValueError:
        print("Error=insert the correct value")
    finally:
        print("the block of code will always execute")
division()