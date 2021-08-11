#В магазине есть список разных продуктов, у каждого продукта есть 
# название, цена, уникальный номер. Сперва пользователю нужно отобразить
# весь список продуктов с их информацией, после нужно сказать чтобы он 
# ввел название товара, если такой товар есть предложить пользователю 
# купить этот товар, и ввести сумму если введенная сумма меньше цены 
# которая указана на товар то нужно уведомить его что у вас не хватает 
# денег чтобы купить, иначе сказать ему что вы получили товар.
def grocery_store(list_of_groceries, list_of_prices):
    print('Список продуктов:', list_of_groceries)
    print('Цены продуктов: ', list_of_prices)
    inpt = input('Введите название товара: ')
    for i in list_of_groceries:
        if inpt in list_of_groceries:
            indx = list_of_groceries.index(inpt)
            print('Хотите совершить покупку?')
            money = int(input('Введите сумму: '))
            cost_of_apple = int(list_of_prices[indx])
            if money >= int(cost_of_apple):
                print('Вы успешно совершили покупку!')
                break
            else:
                print('У вас не хватает средств!')

list_of_groceries = ('apples', 'bread', 'ramen', 'strawberries')
list_of_prices = (150, 80, 240, 450) 
grocery_store(list_of_groceries, list_of_prices)     

