# 编写一个简单的记事本程序，支持读取、写入和追加文件的内容

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print("文件写入成功")
def append_file(filename, content): 
    with open(filename, 'a') as file:
        file.write(content)
    print("文件追加成功")
# 主程序
if __name__=="__main__":
    filename = input("请输入文件名：")
    while True:
        print("1. 读取文件") 
        print("2. 写入文件")
        print("3. 追加文件")
        print("4. 退出程序")
        choice = input("请输入操作编号：")
        if choice == "1":  
            read_file(filename)
        elif choice == "2":
            content = input("请输入要写入的内容：")
            write_file(filename, content)
        elif choice == "3": 
            content = input("请输入要追加的内容：")
            append_file(filename, content)
        elif choice == "4":  
            break   
        else:
            print("无效的操作编号，请重新输入") 
        print() 
        print("操作完成，按任意键继续...")
        input() 
