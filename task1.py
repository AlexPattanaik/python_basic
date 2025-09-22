def task1():
    A=int(input("Enter the first number: "))
    B=int(input("Enter the second number: "))


    Addition=A+B
    print(f"\nAddition: {Addition}")
    Subtraction=A-B
    print(f"Subtraction: {Subtraction}")
    Multiplication=A*B
    print(f"Multiplication: {Multiplication}")
    try:
        Division=A/B
        print(f"Division: {Division}")
    except ZeroDivisionError:
        print("you are trying to dividing by 0 ")

task1()