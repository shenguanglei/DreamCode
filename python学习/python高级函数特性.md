## 1. 高级函数特性

### 1.1 Lambda 函数（匿名函数）

Lambda 函数是一种简洁的定义函数的方式，通常用于需要简单函数的场景。

#### 语法

python

复制

```
lambda 参数1, 参数2, ...: 表达式
```

#### 示例

python

复制

```
# 普通函数
def add(a, b):
    return a + b

# Lambda 函数
add_lambda = lambda a, b: a + b

print(add(2, 3))         # 输出: 5
print(add_lambda(2, 3))  # 输出: 5
```

#### 使用场景

Lambda 函数通常用于需要简单函数的场景，例如排序或高阶函数中。

python

复制

```
# 按元组的第二个元素排序
data = [(1, 3), (4, 1), (2, 2)]
data.sort(key=lambda x: x[1])
print(data)  # 输出: [(4, 1), (2, 2), (1, 3)]
```

------

### 1.2 高阶函数

高阶函数是指可以接受函数作为参数或返回函数的函数。Python 中常用的高阶函数包括 `map`、`filter` 和 `reduce`。

#### 1.2.1 `map` 函数

`map` 函数将一个函数应用于可迭代对象的每个元素，并返回一个迭代器。

##### 语法

python

复制

```
map(函数, 可迭代对象)
```

##### 示例

python

复制

```
# 将列表中的每个元素平方
numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # 输出: [1, 4, 9, 16]
```

#### 1.2.2 `filter` 函数

`filter` 函数根据条件过滤可迭代对象中的元素，并返回一个迭代器。

##### 语法

python

复制

```
filter(函数, 可迭代对象)
```

##### 示例

python

复制

```
# 过滤出列表中的偶数
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # 输出: [2, 4, 6]
```

#### 1.2.3 `reduce` 函数

`reduce` 函数对可迭代对象中的元素进行累积计算，并返回一个结果。

##### 语法

python

复制

```
from functools import reduce
reduce(函数, 可迭代对象, 初始值)
```

##### 示例

python

复制

```
from functools import reduce

# 计算列表中所有元素的乘积
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 输出: 24
```

------

## 2. 综合练习

### 2.1 练习 1：简易计算器

编写一个简单的计算器程序，支持加、减、乘、除操作。

#### 示例代码

python

复制

```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "错误：除数不能为零！"
    return a / b

# 主程序
if __name__ == "__main__":
    print("选择操作：")
    print("1. 加")
    print("2. 减")
    print("3. 乘")
    print("4. 除")

    choice = input("输入操作编号 (1/2/3/4): ")

    num1 = float(input("输入第一个数字: "))
    num2 = float(input("输入第二个数字: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("无效的输入")
```

------

### 2.2 练习 2：简易记事本

编写一个简单的记事本程序，支持读取、写入和追加文件内容。

#### 示例代码

python

复制

```
def read_file(filename):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("文件未找到！")

def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print("文件写入成功！")

def append_file(filename, content):
    with open(filename, "a") as file:
        file.write(content)
    print("内容追加成功！")

# 主程序
if __name__ == "__main__":
    filename = "notes.txt"
    while True:
        print("\n选择操作：")
        print("1. 读取文件")
        print("2. 写入文件")
        print("3. 追加内容")
        print("4. 退出")

        choice = input("输入操作编号 (1/2/3/4): ")

        if choice == '1':
            read_file(filename)
        elif choice == '2':
            content = input("输入要写入的内容: ")
            write_file(filename, content)
        elif choice == '3':
            content = input("输入要追加的内容: ")
            append_file(filename, content)
        elif choice == '4':
            break
        else:
            print("无效的输入")
```

------

### 2.3 练习 3：使用高阶函数

编写一个程序，使用 `map`、`filter` 和 `reduce` 对列表进行操作。

#### 示例代码

python

复制

```
from functools import reduce

# 使用 map 对列表中的每个元素平方
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print("平方后的列表:", squared)

# 使用 filter 过滤出偶数
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("偶数列表:", evens)

# 使用 reduce 计算列表中所有元素的乘积
product = reduce(lambda x, y: x * y, numbers)
print("列表元素的乘积:", product)
```

------

## 总结

- **Lambda 函数**：用于定义简单的匿名函数。
- **高阶函数**：`map`、`filter` 和 `reduce` 是常用的高阶函数，可以简化代码。
- **综合练习**：通过编写计算器和记事本程序，巩固所学知识。

如果有任何问题，随时问我！ 😊