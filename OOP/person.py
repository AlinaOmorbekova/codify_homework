#3. Создайте класс Person с атрибутами экземпляра first_name,last_name,
# middle_name,email,is_active и методами get_full_name - возвращает полное имя, 
# get_gmail - возвращает только почту с доменом @gmail.com. 
# Создайте 5 экземпляров класса Person с разными параметрами и 
# выведите в консоль все параметры созданных вами классов.
class Person:
    first_name = 'Alina'
    last_name = 'Omorbekova'
    middle_name = 'Omorbekova'
    email = 'alina.omorbekovna'
    is_active = 'Active'
    def __init__(self, first_name=None, last_name=None, middle_name=None, email=None, is_active=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name  
        if middle_name:
            self.middle_name = middle_name
        if email:
            self.email = email
        if is_active:
            self.is_active = is_active              
            
    def get_full_name(self):
        print('Full name is:', self.first_name, self.last_name)
    def get_gmail(self):
        print('email is:', self.email + '@gmail.com')    
        
alina = Person()
print(Person.first_name, Person.last_name, Person.middle_name, Person.email, Person.is_active)
alina.get_full_name()  
alina.get_gmail()      

bermet = Person('Bermet', 'Anarbaeva', 'Sultan', 'bermet1809', 'Not active')
print(bermet.first_name, bermet.last_name, bermet.middle_name, bermet.email, bermet.is_active) 
bermet.get_full_name()
bermet.get_gmail()  

anton = Person()
anton.age = 25
print("Anton's age is", anton.age)

andrei = Person()
andrei.hairColor = 'green'
print("Andrei's hair color is", andrei.hairColor)

medina = Person()
medina.isStudent = True
print('Is Medina a student?', medina.isStudent)
