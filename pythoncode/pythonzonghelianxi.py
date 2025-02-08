
# 联系1 简易计算器
def add(x,y):
    return x+y
def sub(x,y):    
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if y==0:
        return '除数不能为0'
    return x/y
# 主程序
if __name__ == '__main__':
    print('1.相加')
    print('2.相减')
    print('3.相乘')
    print('4.相除')
    choice = input('请输入你的选择（1/2/3/4）：')
    num1 = float(input('请输入第一个数字：'))
    num2 = float(input('请输入第二个数字：'))
    if choice == '1':
        print(num1,'+',num2,'=',add(num1,num2))
    elif choice == '2': 
        print(num1,'-',num2,'=',sub(num1,num2)) 
    elif choice == '3':
        print(num1,'*',num2,'=',mul(num1,num2))
    elif choice == '4':
        print(num1,'/',num2,'=',div(num1,num2))
    else:   
        print('非法输入')