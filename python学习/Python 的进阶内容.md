## 1. 模块与包

### 1.1 模块（Module）

模块是一个包含 Python 代码的文件（`.py` 文件），它可以包含函数、类、变量等。通过模块，你可以将代码组织成可重用的单元。

#### 1.1.1 导入模块

使用 `import` 关键字导入模块。

python

复制

```
# 导入标准库模块
import math

# 使用模块中的函数
print(math.sqrt(16))  # 输出: 4.0
```

#### 1.1.2 导入模块中的特定内容

你可以只导入模块中的特定函数或变量。

python

复制

```
from math import sqrt, pi

print(sqrt(25))  # 输出: 5.0
print(pi)        # 输出: 3.141592653589793
```

#### 1.1.3 给模块起别名

如果模块名太长，可以给它起一个别名。

python

复制

```
import math as m

print(m.sqrt(36))  # 输出: 6.0
```

#### 1.1.4 自定义模块

你可以创建自己的模块。例如，创建一个名为 `mymodule.py` 的文件：

python

复制

```
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

然后在另一个文件中导入并使用它：

python

复制

```
import mymodule

print(mymodule.greet("Alice"))  # 输出: Hello, Alice!
print(mymodule.add(2, 3))       # 输出: 5
```

------

### 1.2 包（Package）

包是一个包含多个模块的目录。包通过目录中的 `__init__.py` 文件来标识。

#### 1.2.1 创建包

假设你有一个名为 `mypackage` 的包，结构如下：

复制

```
mypackage/
    __init__.py
    module1.py
    module2.py
```

- `__init__.py` 可以是空文件，也可以包含包的初始化代码。
- `module1.py` 和 `module2.py` 是包中的模块。

#### 1.2.2 导入包中的模块

你可以通过以下方式导入包中的模块：

python

复制

```
from mypackage import module1, module2

print(module1.greet("Bob"))  # 假设 module1 中有 greet 函数
print(module2.add(4, 5))     # 假设 module2 中有 add 函数
```

#### 1.2.3 导入包中的特定内容

你也可以直接导入包中模块的特定内容。

python

复制

```
from mypackage.module1 import greet

print(greet("Charlie"))  # 输出: Hello, Charlie!
```

------

## 2. 异常处理

### 2.1 异常处理机制

在 Python 中，异常是程序运行时发生的错误。通过异常处理，你可以捕获并处理这些错误，避免程序崩溃。

#### 2.1.1 基本语法

使用 `try-except` 语句捕获异常。

python

复制

```
try:
    # 可能引发异常的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理异常
    print("不能除以零！")
```

#### 2.1.2 捕获多个异常

你可以捕获多个异常，并分别处理。

python

复制

```
try:
    num = int(input("请输入一个整数: "))
    result = 10 / num
except ValueError:
    print("输入的不是整数！")
except ZeroDivisionError:
    print("不能除以零！")
```

#### 2.1.3 捕获所有异常

使用 `except Exception` 可以捕获所有异常。

python

复制

```
try:
    result = 10 / 0
except Exception as e:
    print(f"发生错误: {e}")
```

#### 2.1.4 `finally` 语句

`finally` 块中的代码无论是否发生异常都会执行。

python

复制

```
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("文件未找到！")
finally:
    file.close()  # 确保文件被关闭
```

#### 2.1.5 抛出异常

使用 `raise` 关键字手动抛出异常。

python

复制

```
def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零！")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)  # 输出: 除数不能为零！
```

------

## 3. 面向对象编程（OOP）

### 3.1 类和对象

类是对象的蓝图，对象是类的实例。

#### 3.1.1 定义类

使用 `class` 关键字定义类。

python

复制

```
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"
```

- `__init__` 是构造函数，用于初始化对象的属性。
- `self` 表示类的实例本身。

#### 3.1.2 创建对象

通过类创建对象。

python

复制

```
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # 输出: Buddy
print(my_dog.bark())  # 输出: Buddy says woof!
```

### 3.2 继承

继承允许一个类继承另一个类的属性和方法。

python

复制

```
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

my_cat = Cat("Whiskers")
print(my_cat.speak())  # 输出: Whiskers says meow!
```

### 3.3 多态

多态是指不同类的对象可以对同一方法做出不同的响应。

python

复制

```
def animal_sound(animal):
    print(animal.speak())

my_dog = Dog("Buddy", 3)
my_cat = Cat("Whiskers")

animal_sound(my_dog)  # 输出: Buddy says woof!
animal_sound(my_cat)  # 输出: Whiskers says meow!
```

------

## 4. 总结

- **模块与包**：通过模块和包组织代码，实现代码复用。
- **异常处理**：使用 `try-except` 捕获和处理异常，增强程序的健壮性。
- **面向对象编程**：掌握类、对象、继承和多态等 OOP 概念，编写更结构化的代码。