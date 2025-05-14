x = float(input("Введите х:  "))
y = float(input("Введите у:  "))
n = input("Выберите операция: +, -, *, /")
def calc():
    while True:
        f = ()
        if n == "x":
            f = x + y
        elif n == "-":
            f = x - y
        elif n == "*":
            f = x * y
        else:
            if n == "/":
                if y == 0:
                    float(input("Введите у: "))
                else:
                    f = x / y
        print(f)
calc()




