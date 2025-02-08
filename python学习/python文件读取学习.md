好的！文件操作是编程中非常常见的任务，Python 提供了简单而强大的文件操作功能。接下来，我们将学习如何打开、读取和写入文件，并通过一些简单的代码片段进行练习。

### 1. 文件操作基础

在 Python 中，文件操作通常包括以下几个步骤：

1. **打开文件**：使用 `open()` 函数打开文件。
2. **读取或写入文件**：使用文件对象的方法进行读取或写入操作。
3. **关闭文件**：使用 `close()` 方法关闭文件，释放资源。

#### 1.1 打开文件

使用 `open()` 函数打开文件，语法如下：

python

复制

```
file = open("文件名", "模式")
```

- **文件名**：文件的路径（可以是相对路径或绝对路径）。
- **模式**：指定文件的打开模式，常见的模式有：
  - `"r"`：只读模式（默认）。
  - `"w"`：写入模式，会覆盖文件内容。
  - `"a"`：追加模式，在文件末尾添加内容。
  - `"b"`：二进制模式（例如 `"rb"` 或 `"wb"`）。
  - `"+"`：读写模式（例如 `"r+"` 或 `"w+"`）。

#### 1.2 读取文件

常用的读取文件的方法有：

- `read()`：读取整个文件内容。
- `readline()`：读取文件的一行。
- `readlines()`：读取所有行并返回一个列表。

#### 1.3 写入文件

常用的写入文件的方法有：

- `write()`：写入字符串到文件。
- `writelines()`：写入一个字符串列表到文件。

#### 1.4 关闭文件

使用 `close()` 方法关闭文件，释放资源。为了避免忘记关闭文件，推荐使用 `with` 语句，它会在代码块执行完毕后自动关闭文件。

### 2. 文件操作示例

#### 2.1 读取文件

python

复制

```
# 打开文件并读取内容
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

- `example.txt` 是文件名，`"r"` 表示以只读模式打开。
- `with` 语句会自动关闭文件，无需手动调用 `close()`。

#### 2.2 逐行读取文件

python

复制

```
# 逐行读取文件
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() 用于去除行末的换行符
```

#### 2.3 写入文件

python

复制

```
# 写入文件
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
```

- `"w"` 模式会覆盖文件内容。如果文件不存在，会自动创建。

#### 2.4 追加内容到文件

python

复制

```
# 追加内容到文件
with open("output.txt", "a") as file:
    file.write("\nThis line is appended.")
```

- `"a"` 模式会在文件末尾追加内容，而不会覆盖原有内容。

#### 2.5 读取和写入二进制文件

python

复制

```
# 读取二进制文件
with open("image.png", "rb") as file:
    data = file.read()

# 写入二进制文件
with open("copy.png", "wb") as file:
    file.write(data)
```

- `"rb"` 和 `"wb"` 分别表示以二进制模式读取和写入文件。

### 3. 练习

#### 练习 1：读取文件并统计行数

编写一个程序，读取一个文本文件并统计文件中的行数。

python

复制

```
# 统计文件行数
with open("example.txt", "r") as file:
    lines = file.readlines()
    print(f"文件共有 {len(lines)} 行。")
```

#### 练习 2：复制文件

编写一个程序，将一个文件的内容复制到另一个文件。

python

复制

```
# 复制文件
with open("example.txt", "r") as source_file:
    with open("copy.txt", "w") as target_file:
        for line in source_file:
            target_file.write(line)
```

#### 练习 3：处理 CSV 文件

假设有一个 CSV 文件 `data.csv`，内容如下：

复制

```
name,age,city
Alice,25,New York
Bob,30,Los Angeles
Charlie,35,Chicago
```

编写一个程序，读取 CSV 文件并打印每个人的信息。

python

复制

```
# 读取 CSV 文件
with open("data.csv", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:  # 跳过标题行
        name, age, city = line.strip().split(",")
        print(f"{name} is {age} years old and lives in {city}.")
```

### 4. 总结

- **打开文件**：使用 `open()` 函数，指定文件名和模式。
- **读取文件**：使用 `read()`、`readline()` 或 `readlines()` 方法。
- **写入文件**：使用 `write()` 或 `writelines()` 方法。
- **关闭文件**：使用 `close()` 方法，或使用 `with` 语句自动关闭。
- **文件模式**：`"r"`（只读）、`"w"`（写入）、`"a"`（追加）、`"b"`（二进制）。

通过这些基础的文件操作，你可以处理各种文件读写任务。如果有任何问题，随时问我！ 