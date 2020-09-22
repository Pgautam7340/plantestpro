Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> while True:
    option= input("Enter 'add' or 'subtract', 'multiply', 'divide', 'power', 'quit'")
    if option== 'quit':
        break
    elif option=='add':
        x= int(input("enter number 1"))
        y= int(input("enter number 2"))
        print(x+y)
    elif option=='subtract':
        x= int(input("enter number 1"))
        y= int(input("enter number 2"))
        print(x-y)
    elif option=='multiply':
        x= int(input("enter number 1"))
        y= int(input("enter number 2"))
        print(x * y)
    elif option=='divide':
        x= int(input("enter number 1"))
        y= int(input("enter number 2"))
        print(x/y)
    elif option=='power':
        x= int(input("enter the base"))
        y= int(input("enter the exponent"))
        print(x**y)
    else:
        print("invalid argument")
