# Python 3 最新语法快速学习手册

本手册旨在快速概览 Python 3.6 至 3.10+ 版本中引入的核心与最新语法，帮助开发者快速上手现代 Python 开发。

---

## 1. 基础语法 (Basic Syntax)

### **变量与类型提示 (Variables & Type Hinting)**
自 Python 3.5 起，可以为变量、函数参数和返回值添加类型提示，以提高代码可读性和健壮性。

```python
# 传统方式
name = "world"
age = 25

# 现代方式 (带类型提示)
name: str = "world"
age: int = 25
is_student: bool = True
```

### **f-string 格式化 (f-string Formatting)**
自 Python 3.6 起，f-string 成为最推荐的字符串格式化方法，它快速、易读。

```python
name = "Alex"
age = 30

# 旧方式
print("My name is {} and I am {} years old.".format(name, age))

# f-string (推荐)
print(f"My name is {name} and I am {age} years old.")
# f-string 内可执行表达式
print(f"Next year, I will be {age + 1} years old.")
```

### **数字字面量中的下划线 (Underscores in Numeric Literals)**
自 Python 3.6 起，为了提高可读性，可以在数字中使用下划线。

```python
large_number = 1_000_000_000
hex_value = 0xFF_EC_DE_5E
```

---

## 2. 数据结构 (Data Structures)

### **列表/字典/集合推导式 (Comprehensions)**
推导式是创建数据结构的紧凑而高效的方式。

```python
# 列表推导式
squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]

# 字典推导式
square_map = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 集合推导式
unique_squares = {x**2 for x in [1, 1, 2, 2, 3]}
# {1, 4, 9}
```

### **字典合并 (Dictionary Merging)**
自 Python 3.9 起，可以使用 `|` 操作符合并字典。

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# b 的值会被 dict2 覆盖
merged_dict = dict1 | dict2
# {'a': 1, 'b': 3, 'c': 4}
```

---

## 3. 控制流 (Control Flow)

### **海象运算符 (Walrus Operator `:=`)**
自 Python 3.8 起，海象运算符 `:=` 可以在表达式内部为变量赋值，常用于简化循环。

```python
# 传统 while 循环
line = f.readline()
while line:
    print(line)
    line = f.readline()

# 使用海象运算符
while (line := f.readline()):
    print(line)

# 也可以用在列表推导式中
# results = [y for x in data if (y := process(x)) is not None]
```

### **结构化模式匹配 (Structural Pattern Matching)**
自 Python 3.10 起，`match...case` 语句提供了一种更强大、更具表现力的分支逻辑方式，类似于其他语言的 `switch` 语句，但功能更强。

```python
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # _ 是通配符，匹配任何其他情况
            return "Unknown status"

print(http_status(404)) # "Not Found"

# 匹配复杂结构
def process_command(command):
    match command:
        case ["move", x, y]:
            print(f"Moving to ({x}, {y})")
        case ["draw", *shapes]:
            print(f"Drawing shapes: {shapes}")
        case {"action": "quit"}:
            print("Quitting...")
        case _:
            print("Invalid command")

process_command(["move", 10, 20])
process_command(["draw", "circle", "square"])
```

---

## 4. 函数 (Functions)

### **仅位置参数和仅关键字参数**
自 Python 3.8 起，函数定义可以更精确地指定参数如何传递。

- `/` 之前的所有参数都必须是**仅位置参数**。
- `*` 之后的所有参数都必须是**仅关键字参数**。

```python
def f(pos1, pos2, /, standard, *, kw1, kw2):
    """
    pos1, pos2: 只能通过位置传递
    standard: 可以通过位置或关键字传递
    kw1, kw2: 只能通过关键字传递
    """
    print(f"pos1={pos1}, pos2={pos2}, standard={standard}, kw1={kw1}, kw2={kw2}")

# 合法调用
f(1, 2, 3, kw1=4, kw2=5)
f(1, 2, standard=3, kw1=4, kw2=5)

# 非法调用
# f(1, pos2=2, ...)  # pos2 不能是关键字参数
# f(1, 2, 3, 4, 5)    # kw1, kw2 不能是位置参数
```

### **带类型提示的函数**

```python
def greet(name: str, is_formal: bool = False) -> str:
    if is_formal:
        return f"Greetings, {name}."
    else:
        return f"Hello, {name}!"
```

---

## 5. 类与数据类 (Classes & Dataclasses)

### **数据类 (`@dataclass`)**
自 Python 3.7 起，`@dataclass` 装饰器可以自动为类生成特殊方法，如 `__init__()`, `__repr__()`, `__eq__()` 等，非常适合用于创建主要用于存储数据的类。

```python
from dataclasses import dataclass

# 传统方式
class PointOld:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# 使用 @dataclass
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # 可以有默认值

p1 = Point(1.5, 2.5)
print(p1)  # Point(x=1.5, y=2.5, z=0.0) - 自动生成了 __repr__
```

---

## 6. 异常与上下文 (Exceptions & Context)

### **异常处理**
`try...except...else...finally` 结构保持不变，但可以组合使用。

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # 如果 try 块没有引发异常，则执行
    print(f"Result is {result}")
finally:
    # 无论如何都会执行
    print("Execution finished.")
```

### **上下文管理器 (`with` 语句)**
`with` 语句是管理资源（如文件、网络连接）的首选方式，它能确保资源被正确关闭。

```python
# 自动处理文件的打开和关闭
try:
    with open("my_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    content = "File not found."

print(content)
```

---

## 7. 异步编程 (Asynchronous Programming)

自 Python 3.5 起，`async` 和 `await` 关键字让异步编程变得更加直接。

```python
import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print("Started...")
    await say_after(1, "hello")
    await say_after(2, "world")
    print("Finished.")

# 运行异步主函数 (Python 3.7+)
asyncio.run(main())
```
