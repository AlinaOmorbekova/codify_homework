# Калькулятор для 4ых операций(+,-,*,/), каждая операция - в отдельном модуле,
# основной модуль программы - main.py
# Сделать возможность запускать модули самостоятельно и выполнять приведённый в них функционал, с помощью конструкции: 
#if __name__ == '__main__':
      #pass
import minus  
import plus   
import multiplication
import division 
def main():
  num1 = int(input('Введите первое число: '))
  num2 = int(input("Введите второе число: "))
  operation = input("Выберите оперцию '+, -, *, /':  ")
  if operation == '-':
    result = minus.calculate_subtraction(num1, num2)
  elif operation == '+':
    result = plus.calculate_addition(num1, num2) 
  elif operation == '*':
    result = multiplication.calculate_multiplication(num1, num2)
  elif operation == '/':
    result = division.calculate_division(num1, num2)    

if __name__ == "__main__":
  main()  



