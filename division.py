def calculate_division(num1, num2):
    try:
        print(num1, ' / ', num2, '=', num1 / num2)
    except ZeroDivisionError:
        print('На нуль делить нельзя!')    