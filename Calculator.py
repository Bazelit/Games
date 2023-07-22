while True:
    sign = input("Выберите знак: +, -, /, * (0 - завершить работу) ")

    if sign == "0":
        break

    if sign in ("+", "-", "/", "*"):
        num1 = int(input("Напишите превое число: "))
        num2 = int(input("Напишите второе число: "))
        if sign == "+":
            print(f'{num1} + {num2} = {num1 + num2}')
        elif sign == "-":
            print(f'{num1} - {num2} = {num1 - num2}')
        elif sign == "*":
            print(f'{num1} * {num2} = {num1 * num2}')
        elif sign == "/":
            if num2 == 0:
                print("Деление на ноль!!!")
            else:
                print(f'{num1} / {num2} = {num1 / num2}')
    else:
        print('Неверный знак операции')
