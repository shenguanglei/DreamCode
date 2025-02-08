
# 普通函数
def add(a,b):
    return a+b
# Lambda 函数
add_Lambda=lambda a,b:a+b


print(add(1,2))
print(add_Lambda(1,2))
# 使用场景
# Lambda 函数通常用于需要简单函数的场景，例如排序或高阶函数中
# Lambda 函数的语法非常简单，它由关键字 lambda、一个或多个参数、一个冒号和一个表达式组成
# 按元组的第二个元素排序
data =[(1,7),(3,4),(5,6)]
data.sort(key=lambda x:x[1])
print(data)


# 高阶函数
# 高阶函数是指可以接收函数作为参数或返回函数的函数，Python 中的高阶函数包括 map、filter 和 reduce 等
# map 函数接收两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象，它将函数应用于可迭代对象的每个元素，并返回一个迭代器
# filter 函数接收两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象，它将函数应用于可迭代对象的每个元素，并返回一个迭代器，其中包含满足函数条件的元素
# reduce 函数接收两个参数，第一个参数是一个函数，第二个参数是一个可迭代对象，它将函数应用于可迭代对象的连续元素，并返回一个值
# map 函数
numbers = [1, 2, 3, 4, 5]
squared=map(lambda x: x**2, numbers)
print(list(squared))
# filter 函数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 过滤列表中偶数
evens=filter(lambda x:x%2==0,numbers)
print(list(evens))
# reduce 函数
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product= reduce(lambda x, y: x * y, numbers)
print(product)
# 高阶函数的使用场景
# 高阶函数通常用于需要对可迭代对象进行复杂操作的场景，例如数据转换、过滤和聚合等
# 高阶函数可以提高代码的可读性和可维护性，因为它可以将复杂的操作分解为更小的函数

# 高阶函数的优缺点
# 优点
# 高阶函数可以提高代码的可读性和可维护性，因为它可以将复杂的操作分解为更小的函数
# 高阶函数可以简化代码，因为它可以避免显式地编写循环和条件语句
# 高阶函数可以提供更灵活的编程方式，因为它可以接受不同的函数作为参数，从而实现不同的操作

