### 1. 函数（Functions）

**函数**是一段可以重复使用的代码块，它可以接受输入（参数），并返回输出（返回值）。使用函数可以让代码更加简洁、易读和易于维护。

#### 1.1 定义函数

在 Python 中，使用 `def` 关键字来定义函数。函数的基本语法如下：

python

复制

```
def 函数名(参数1, 参数2, ...):
    # 函数体
    return 返回值
```

- **函数名**：函数的名称，遵循变量命名规则。
- **参数**：函数可以接受零个或多个参数。
- **函数体**：函数的具体实现代码。
- **返回值**：使用 `return` 语句返回结果，如果没有 `return`，函数默认返回 `None`。

#### 1.2 示例

python

复制

```
# 定义一个简单的函数
def greet(name):
    return f"Hello, {name}!"

# 调用函数
message = greet("Alice")
print(message)  # 输出: Hello, Alice!
```

#### 1.3 默认参数

你可以为函数的参数指定默认值，这样在调用函数时可以不传递该参数。

python

复制

```
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))  # 输出: Hello, Bob!
print(greet("Bob", "Hi"))  # 输出: Hi, Bob!
```

#### 1.4 可变参数

你可以使用 `*args` 和 `**kwargs` 来接受可变数量的参数。

- `*args`：接受任意数量的位置参数，作为一个元组。
- `**kwargs`：接受任意数量的关键字参数，作为一个字典。

python

复制

```
def print_args(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:", kwargs)

print_args(1, 2, 3, name="Alice", age=25)
# 输出:
# 位置参数: (1, 2, 3)
# 关键字参数: {'name': 'Alice', 'age': 25}
```

### 2. 类（Classes）

**类**是面向对象编程（OOP）的核心概念。类是一个蓝图或模板，用于创建对象。对象是类的实例，具有属性和方法。

#### 2.1 定义类

在 Python 中，使用 `class` 关键字来定义类。类的基本语法如下：

python

复制

```
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        # 初始化方法
        self.属性1 = 参数1
        self.属性2 = 参数2
        # ...

    def 方法名(self, 参数1, 参数2, ...):
        # 方法体
        pass
```

- `__init__`：这是一个特殊的方法，称为**构造函数**，用于初始化对象的属性。
- `self`：表示类的实例本身，通过 `self` 可以访问类的属性和方法。

#### 2.2 示例

python

复制

```
# 定义一个简单的类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

# 创建类的实例
my_dog = Dog("Buddy", 3)

# 访问属性和调用方法
print(my_dog.name)  # 输出: Buddy
print(my_dog.bark())  # 输出: Buddy says woof!
```

#### 2.3 继承

继承是面向对象编程的一个重要特性，它允许你创建一个新类，继承现有类的属性和方法。

python

复制

```
# 定义一个基类
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# 定义一个子类，继承自 Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# 创建子类的实例
my_cat = Cat("Whiskers")
print(my_cat.speak())  # 输出: Whiskers says meow!
```

#### 2.4 类的特殊方法

Python 类中有一些特殊方法（也称为魔术方法），它们以双下划线 `__` 开头和结尾。例如：

- `__str__`：定义对象的字符串表示形式。
- `__len__`：定义对象的长度。

python

复制

```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return len(self.title)

# 创建类的实例
my_book = Book("Python Programming", "Alice")

print(my_book)  # 输出: Python Programming by Alice
print(len(my_book))  # 输出: 18
```

### 3. 总结

- **函数**：用于封装可重用的代码块，可以接受参数并返回值。
- **类**：用于创建对象，类是对象的蓝图，包含属性和方法。
- **继承**：允许你创建一个新类，继承现有类的属性和方法。

接下来，你可以尝试编写一些简单的函数和类，进一步巩固这些概念。如果你有任何问题，随时可以问我