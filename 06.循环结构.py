# """
# 从1到100的偶数求和

# Version: 1.0
# Author: 骆昊
# """
# """
# total = 0
# # 前闭后开 2-100 跨度2
# for i in range(2, 101,2):
#     print(i)
#     if i % 2 == 0:
#         total += i
# print(total)
# """

# """
# 从1到100的奇数求和

# Version: 1.0
# Author: 骆昊
# """
# """
# res = sum(range(1, 101, 2))
# print(res)
# """

# # total = 0
# # i= 2
# # while i <= 100:
# #     print(i)
# #     total += i
# #     i += 2
# # print(total)

# """
# 从1到100的偶数求和

# Version: 1.3
# Author: 骆昊
# """
# total = 0
# i = 2
# while i <= 100:
#     print(i)
#     total += i
#     i += 2
# print(total)


# """
# 从1到100的偶数求和

# Version: 1.3
# Author: 骆昊
# """
# total = 0
# i = 2
# while i <= 100:
#     total += i
#     i += 2
# print(total)


# """
# 从1到100的偶数求和

# Version: 1.4
# Author: 骆昊
# """
# total = 0
# i = 2
# while True:
#     print(i)
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)


# """
# 从1到100的偶数求和

# Version: 1.5
# Author: 骆昊
# """
# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         continue
#     print(i)
#     total += i
# print(total)


# """
# 打印乘法口诀表
# Version: 1.0
# Author: 骆昊
# """
# # 1-9
# index = 10
# for i in range(1, index):
#     for j in range(1, i + 1):
#         print(f'{i}×{j}={i * j}', end='\t')
#     print()


# """
# 输入一个大于1的正整数判断它是不是素数

# Version: 1.0
# Author: 骆昊
# """
# num = int(input('请输入一个正整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')


# """
# 输入两个正整数求它们的最大公约数

# Version: 1.0
# Author: 骆昊
# """
# x = int(input('x = '))
# y = int(input('y = '))
# for i in range(x, 0, -1):
#     print(i)
#     if x % i == 0 and y % i == 0:
#         print(f'最大公约数: {i}')
#         break


# """
# 输入两个正整数求它们的最大公约数

# Version: 1.1
# Author: 骆昊
# """
# x = int(input('x = '))  # 获取第一个正整数
# y = int(input('y = '))  # 获取第二个正整数
# # 使用辗转相除法（欧几里得算法）求最大公约数
# while y % x != 0:  # 当余数不为0时继续循环
#     x, y = y % x, x  # 交换：x变为y除以x的余数，y变为原来的x
# print(f'最大公约数: {x}')  # 输出最大公约数


"""
猜数字小游戏
计算机随机生成一个1-100之间的整数，玩家通过输入数字来猜测答案
根据玩家的输入给出相应的提示，直到猜中为止

Version: 1.0
Author: 骆昊
"""
import random  # 导入random模块，用于生成随机数

# 生成1到100之间的随机整数作为答案
answer = random.randrange(1, 101) # 前闭后开
# 初始化计数器，记录玩家猜测的次数
counter = 0
# 无限循环，直到玩家猜中答案
while True:
    # 每次猜测计数器加1
    counter += 1
    # 获取玩家输入的数字
    num = int(input("请输入: "))
    # 如果玩家猜的数字小于答案
    if num < answer:
        print("大一点.")  # 提示玩家猜大一点
    # 如果玩家猜的数字大于答案
    elif num > answer:
        print("小一点.")  # 提示玩家猜小一点
    # 如果玩家猜中了答案
    else:
        print("猜对了.")  # 提示玩家猜对了
        break  # 跳出循环，游戏结束
# 显示玩家总共猜了多少次
print(f"你一共猜了{counter}次.")
