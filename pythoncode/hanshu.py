
# 定义一个简单的函数
def greet(name):
    return f"Hello,{name}!"

# 调用函数并打印结果
message = greet("Alice")
print(message)

# 定义一个带有默认参数的函数
def greet(name ,greeting="Hello"):
    return f"{greeting},{name}!"
# 调用函数并打印结果
print(greet("Alice"))
print(greet("Bob","Hi"))

def print_args(*args,**kwargs):
    print("位置参数:",args)
    print("关键字参数:",kwargs)

print_args(1,2,3,4,5,a=1,b=2,c=3)
