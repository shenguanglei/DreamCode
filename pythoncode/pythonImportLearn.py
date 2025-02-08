

# 导入标准库模块
import math
from math import sqrt,pi
import math as m
import mymodule

# 使用模块中函数
print(math.sqrt(4))
print(pi)

print(m.sqrt(4))
print(mymodule.greet("Alice"))  # 输出: Hello, Alice!
print(mymodule.add(2, 3))       # 输出: 5


try:
    result = 10 / 0
except ZeroDivisionError:
    # 处理异常
    print("除数不能为零")
try:
    num =int(input("请输入一个整数: "))
    result = 10 / num
except ValueError:
    # 处理异常
    print("输入的不是整数")
except ZeroDivisionError:
    # 处理异常
    print("除数不能为零")
try:
    result = 10 / 0
except Exception as e:
    # 处理所有异常
    print("发生了一个异常:", e)

# 使用raise语句抛出异常
def divide(a, b):
    if b==0:
        raise ZeroDivisionError("除数不能为零")
    return a / b
try:
    divide(10, 0)
except ValueError as e:
    print("发生了一个异常:", e)

try:
    file = open("example.txt","r")
    contents = file.read()
except FileNotFoundError:
    # 处理异常
    print("文件未找到")
finally:
    file.close()


