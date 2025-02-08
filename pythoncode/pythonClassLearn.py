
# 类是对象的蓝图，对象是类的实例
# 使用关键字定义类
class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking!")
#__init__是构造函数，用户初始化对象的属性
# self是类实例的引用，可以访问类的属性和方法
# 创建对象 通过类创建对象
my_dog =Dog("Buddy",3)

print(my_dog.name)
print(my_dog.bark())

# 类的继承
# 继承允许一个类继承另一个类的属性和方法
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking!")
class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print(f"{self.name} is meowing!")
def animal_sound(animal):
    animal.speak()
my_cat = Cat("Kitty", 2, "Persian")
animal_sound(my_cat)