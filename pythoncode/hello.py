print("Hello, World!")
# n = input("请输入密码：")	#把输入内容赋给n，用 n 接收一下
# print(n)	#打印n

#   1. 包名：全小写，例如 time ;
#   2. 类名：每个单词的首字母大写，其他的小写，简称大驼峰命名，例如 HelloWorld ；
#   3. 变量名/函数名:第一个单词的首字母小写，后面的单词的首字母大写，简称小驼峰命名，例如 helloWorld ；
#   4. 常量：全大写，例如 HELLO 。
# 合法的标识符:字母，数字(不能开头),下划线，py3可以用中文（不建议），py2不可以。
# 大小写敏感。
# 不能使用关键字和保留字。
# 关键字： if while for as import
# 保留字：input，print range
# 没有长度限制。
# 望文生义，看到名字就知道要表达的意思。
# 数据类型可分为以下6类：
# （1） 整型：整数，英文名 int ，例如 5 的数据类型就是整型。
# （2） 浮点型：小数，英文名 float ，例如 0.5 就是1个浮点型数据。
# 科学计数法，e表示乘以10几次方，例如 b=1e10 表示1*10的10次方。
# （3） 字符串：英文str
# 表现形式有4种：'xs' 、 "xs" 、 """xsxs""" 、 ''''xxx'''  
# 三引号有个特殊功能，表示注释，跟 # 一样的功能，例如：
# """
# xsx
# xs
# 这里面的都是注释内容
# """
# （4）布尔类型：英文bool，True为真，False为假；1表示真，0表示假。
# （5）None 是一个单独的数据类型。
# （6）列表、元组、字典、集合也是常见的数据类型。

# 字符串转整型
# 方法是 int(str) ，字符串必须是数字，例如：
user = int('304200780')	
print(user)
# 浮点型转整型
# 方法是 int(float) ，例如：
f = 20.1
ff = int(f) #直接抹去小数部分
print(ff)

f = 30
ff = float(f)  # 30.0
print(ff)

f = 30.5
ff = str(f)
print(type(ff).__name__)    #type()是获取数据类型函数

f = 30
ff = str(f)
print(type(ff).__name__)    #type()是获取数据类型函数

f = 30
print(type(f))

# isinstance()
# isinstance() 常用来判断数据类型，它返回的是布尔值（True或False），语法是 isinstance(对象,class) 。
# 例子：判断30.5是不是整型。
f = 30.5
n = isinstance(f,int)   #用n来接收一下结果
print(n)

# 运算符可以分为很多4类。
# （1）一般运算符
# +，-，*，/（真除法）,//（地板除，舍去小数部分）,%（取余数）,**（幂运算）
# （2） 赋值运算符
# 常用赋值运算符是 = ，等号右边的值赋值等号左边
# 增强赋值运算符：+=，-=，*=，/=,%=,**=
a = 30
a+=10
print(a)

# 3）布尔运算法
# == （等于），！=（不等于） >= <= > <
# （4） 逻辑运算符
# 主要有not、and和or三类，又称非、与和或
# and：前后都为真则为真
# or：有一个为真则为真
# not:非真，非假

a = 10
b = 20
c = 30
d = 40
n1 = a > b and a < c    #a>b为假，a<c为真，假与真为假
n2 = not a < c   #a<c为真，非真则为假
n3 = a > b or a < c     #a>b为假，a<c为真，假或真为真
print(n1,n2,n3)

# 三、流程控制
# 流程控制常用的是条件分支流程的if/else语句和循环控制的while语句。
# 1.条件分支流程
# 当达到某种条件的时候才会触发的代码。
# （1）语法1

a = 10
b = 20
if a < b:
    print("真的")
if a > b:
    print("假的")

a = 10
b = 20
if a > b:
    a = 30
    print(a)

else:
    print(1111)



s = int(input("请输入分数:"))

if 80 >= s >= 60:
    print("及格")
elif 80 < s <= 90:
    print("优秀")

elif 90 < s <= 100:
    print("非常优秀")

else:
    print("不及格")





