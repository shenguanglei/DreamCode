
# 读取文件
with open('D:/test/test.txt', 'r') as file:
    content=file.read()
    print(content)

# 逐行读取文件
with open('D:/test/test.txt', 'r') as file:
    for line in file:
        print(line.strip()) # 去掉换行符
# 写入文件 w 模式会覆盖文件内容。如果文件不存在，会自动创建
with open('D:/test/output.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a test file.')

with open('D:/test/output.txt', 'r') as file:
    content=file.read()
    print(content)
# 追加内容到文件
with open('D:/test/output.txt', 'a') as file:
    file.write('This line is appended.')

with open('D:/test/output.txt', 'r') as file:
    content=file.read()
    print(content)
# 读取二进制文件
with open('D:/test/test.png', 'rb') as file:
    data=file.read()
    print(data)
# 写入二进制文件
with open('D:/test/copy.png', 'wb') as file:
    file.write(data)
# 读取大文件 并统计行数
with open('D:/test/test.txt', 'r') as file:
    lines=file.readlines()# 读取所有行
    print(lines)
    print(f"lines{len(lines)} 行")
# 复制文件 编写一个程序，将一个文件的内容复制到另一个文件中。
with open('D:/test/test.txt', 'r') as source_file:
    with open('D:/test/copy.txt', 'w') as target_file:
        for line in source_file:
            target_file.write(line)
# 读取 CSV 文件
with open('D:/test/test.csv', 'r') as file:
    lines=file.readlines()
    for line in lines[1:]:
        # 去掉行首行尾的空白字符（包括换行符）
        line = line.strip()
       # 如果行为空，跳过
        if not line:
            continue
        name, age, city = line.split(',')
        print(f"Name: {name}, Age: {age}, City: {city}")
       
       