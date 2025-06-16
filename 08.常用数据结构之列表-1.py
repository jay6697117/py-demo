# 在开始本节课的内容之前，我们先给大家一个编程任务，将一颗色子掷 6000 次，统计每种点数出现的次数。这个任务对大家来说应该是非常简单的，我们可以用 1 到 6 均匀分布的随机数来模拟掷色子，然后用 6 个变量分别记录每个点数出现的次数，相信通过前面的学习，大家都能比较顺利的写出下面的代码。

import random
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0
for i in range(6000):
    temp = random.randint(1, 6)
    if temp == 1:
        num1 +=1
    if temp == 2:
        num2 +=1
    if temp == 3:
        num3 +=1
    if temp == 4:
        num4 +=1
    if temp == 5:
        num5 +=1
    if temp == 6:
        num6 +=1

print('num1',num1)
print('num2',num2)
print('num3',num3)
print('num4',num4)
print('num5',num5)
print('num6',num6)
