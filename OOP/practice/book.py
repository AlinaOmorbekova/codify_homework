class Book:
    def __init__(self):
        self.name = input('Enter your book: ')
        self.author = input('Enter the author of your book: ')
        self.price = int(input('Enter price: '))

    def get_view(self):
        print(self.name)
        print(self.author)
        print(self.price)   

book_1 = Book()
book_1.get_view()
