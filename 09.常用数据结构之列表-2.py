# """
# 双色球随机选号程序

# Author: 骆昊
# Version: 1.1
# """
# import random

# red_balls = [i for i in range(1, 34)] # 红色球 1-33
# blue_balls = [i for i in range(1, 17)]  # 蓝色球 1-16
# # 从红色球列表中随机抽出6个红色球（无放回抽样）
# selected_balls = random.sample(red_balls, 6)
# # 对选中的红色球排序
# selected_balls.sort()
# # 输出选中的红色球
# for ball in selected_balls:
#     print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
# # 从蓝色球列表中随机抽出1个蓝色球
# blue_ball = random.choice(blue_balls)
# # 输出选中的蓝色球
# print(f'\033[034m{blue_ball:0>2d}\033[0m')

# import random
# # random.sample示例 - 抽取多个不重复元素
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 从numbers中随机抽取3个不重复的数字
# sample_result = random.sample(numbers, 3)
# print(f"random.sample结果: {sample_result}")  # 例如: [7, 2, 9]

# # random.choice示例 - 抽取单个元素
# colors = ['红', '橙', '黄', '绿', '蓝', '靛', '紫']
# # 从colors中随机抽取一个颜色
# choice_result = random.choice(colors)
# print(f"random.choice结果: {choice_result}")  # 例如: 蓝

# # 模拟多次使用random.choice (可能会有重复)
# multiple_choices = [random.choice(colors) for _ in range(5)]
# print(f"多次random.choice结果: {multiple_choices}")  # 可能有重复颜色

# # 如果需要抽取多个可能重复的元素，可以使用random.choices (Python 3.6+)
# with_replacement = random.choices(colors, k=5)
# print(f"random.choices结果 (有放回抽样): {with_replacement}")

# """
# 双色球随机选号程序

# Author: 骆昊
# Version: 1.2
# """
# import random

# n = int(input('生成几注号码: '))
# red_balls = [i for i in range(1, 34)]
# blue_balls = [i for i in range(1, 17)]
# for _ in range(n):
#     # 从红色球列表中随机抽出6个红色球（无放回抽样）
#     selected_balls = random.sample(red_balls, 6)
#     # 对选中的红色球排序
#     selected_balls.sort()
#     # 输出选中的红色球
#     for ball in selected_balls:
#         print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
#     # 从蓝色球列表中随机抽出1个蓝色球
#     blue_ball = random.choice(blue_balls)
#     # 输出选中的蓝色球
#     print(f'\033[034m{blue_ball:0>2d}\033[0m')


"""
双色球随机选号程序

Author: 骆昊
Version: 1.3
"""
import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
