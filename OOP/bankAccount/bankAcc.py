#Создайте класс BankAccount, который представляет банковский счет, c атрибутами экземпляра: 
#accountNumber (числовой тип), name (имя владельца счета строкового типа), balance.
#Создайте конструктор с параметрами: accountNumber, name, balance.
#Создайте метод Deposit(), который управляет действиями по пополнению счета.
#Создайте метод Withdrawal(), который управляет действиями по снятию средств.
#Создайте метод bankFees() для применения банковской комиссии в размере 5% от баланса счета.
#Создайте метод display() для отображения деталей счета.
#Приведите примеры использования.


class BankAccount:
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        self.bankFees = 0.05
    def get_deposit(self):
        money_dep = float(input('Введите количество денег, которые хотите положить на счет: '))  
        self.balance = self.balance + money_dep - money_dep*self.bankFees
        print('Вы успешно пополнили баланс на ', money_dep)
        print('Ваш текущий баланс: ', self.balance)
    def get_withdrawal(self):
        money_withdrw = float(input('Введите сумму, которую хотите снять: '))
        if money_withdrw <= self.balance:
            self.balance = self.balance - money_withdrw - money_withdrw*self.bankFees
            print('Вы успешно сняли ', money_withdrw)
            print('Ваш текущий баланс: ', self.balance)
        else:
            print('Недостаточно денег для снятия!')    
    def display(self):
        self.balance = self.balance - self.balance*self.bankFees
        print('Ваш баланс: ',self.balance)
        
    def get_bankFees(self):
        print('''
        Банковская комссия у нас составляет 5%. Каждый раз когда вы снимаете деньги, 
        пополняете счет, запрашиваете информацию о вашем балансе, у вас снимается 5% из общего счета
        или суммы, которую используете
        ''')

    def my_menu(self):
        choice = 0
        while True:
            try:
                choice = int(input('''
            Если хотите пополнить счет нажмите 1
            Если хотите снять денежные средства нажмите 2
            Если хотите увидеть детали счета нажмите 3
            Если хотите узнать подробнее о банковской комиссии нажмите 4
            So your input is ... '''))
                if choice == 1:
                    self.get_deposit()
                if choice == 2:
                    self.get_withdrawal()
                if choice == 3:
                    self.display()
                if choice == 4:
                    self.get_bankFees()  
                if choice not in [1,2,3,4]:
                    raise Exception('Неверный ввод!')              
            except ValueError:
                print('Вы ввели не число!')     
            except Exception as e:
                print(e)        
               
        
alina = BankAccount('Alina', 118000099999, 50000)
alina.my_menu()
