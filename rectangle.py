# 4. Напишите класс Rectangle с атрибутами конструктора длины и ширины.
#Создайте метод Perimeter() для вычисления периметра прямоугольника и метод Area() для вычисления площади прямоугольника.
#Создайте метод display(), который отображает длину, ширину, периметр и площадь объекта.
#Создайте дочерний класс Parallelepipede, наследующий от класса Rectangle, с атрибутом height и еще одним методом Volume() для вычисления объема параллелепипеда.
#Приведите примеры использования.
class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width
  def get_perimeter(self):
    perim = 2*self.length + 2*self.width
    print('Perimeter is:', perim)
  def get_area(self):
    print('Area is:', self.length * self.width)
  def display(self):
    print('Length is: ',self.length)
    print('Width is:', self.width)
    self.get_perimeter()
    self.get_area()
class Parallelepipede(Rectangle):
  def __init__(self, length, width, height):
      super().__init__(length, width)
      self.height = height
  def get_volume(self):
    print('Volume is:', self.length * self.width * self.height)

rectangle_1 = Rectangle(2, 4)
rectangle_1.display()

parallelepipede_1 = Parallelepipede(2,4,8)
parallelepipede_1.get_volume()

