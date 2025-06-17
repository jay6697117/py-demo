# 在开始本节课的内容之前，我们先给大家一个编程任务，将一颗色子掷 6000 次，统计每种点数出现的次数。这个任务对大家来说应该是非常简单的，我们可以用 1 到 6 均匀分布的随机数来模拟掷色子，然后用 6 个变量分别记录每个点数出现的次数，相信通过前面的学习，大家都能比较顺利的写出下面的代码。

# import random
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# num5 = 0
# num6 = 0

# for i in range(6000):
#     temp = random.randint(1, 6)
#     if temp == 1:
#         num1 +=1
#     if temp == 2:
#         num2 +=1
#     if temp == 3:
#         num3 +=1
#     if temp == 4:
#         num4 +=1
#     if temp == 5:
#         num5 +=1
#     if temp == 6:
#         num6 +=1

# print('num1',num1)
# print('num2',num2)
# print('num3',num3)
# print('num4',num4)
# print('num5',num5)
# print('num6',num6)


# items4 = list(range(1, 10))
# items5 = list('hello')

# print(items4)
# print(items5)

# items5 = [35, 12, 99, 45, 66]
# items6 = [45, 58, 29]
# items7 = ['Python', 'Java', 'JavaScript']
# print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
# print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
# items5 += items6
# print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]

# print(29 in items6)  # True
# print(99 in items6)  # False
# print('C++' not in items7)     # True
# print('Python' not in items7)  # False

# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# print(items8[0])   # apple
# print(items8[2])   # pitaya
# print(items8[4])   # watermelon
# items8[2] = 'durian'
# print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
# print(items8[-5])  # 'apple'
# print(items8[-4])  # 'waxberry'
# print(items8[-1])  # watermelon
# items8[-4] = 'strawberr
# print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
# print(items8[-2::-1])  # ['peach', 'durian', 'strawberry', 'apple']
# print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']

# nums1 = [1, 2, 3, 4] # [1, 2, 3, 4]
# nums2 = list(range(1, 5)) # [1, 2, 3, 4]
# nums3 = [3, 2, 1] # [3, 2, 1]
# print(nums2)
# print(nums1 == nums2)  # True
# print(nums1 != nums2)  # False
# print(nums1 <= nums3)  # True
# print(nums2 >= nums3)  # False



# languages = ['Python', 'Java', 'C++', 'Kotlin']
# print(len(languages))
# for index in range(len(languages)):
#     print('---')
#     print(index)
#     print(languages[index])


# languages = ['Python', 'Java', 'C++', 'Kotlin']
# for language in languages:
#     print(language)

"""
将一颗色子掷6000次，统计每种点数出现的次数

Author: 骆昊
Version: 1.1
"""
import random

counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1

print(counters)
# # 输出每种点数出现的次数
for i in range(len(counters)):
    print(f'{i+1}点出现了{counters[i]}次')

# 上面的代码中，我们用counters列表中的六个元素分别表示 1 到 6 点出现的次数，最开始的时候六个元素的值都是 0。接下来，我们用 1 到 6 均匀分布的随机数模拟掷色子，如果摇出 1 点，counters[0]的值加 1，如果摇出 2 点，counters[1]的值加 1，以此类推。大家感受一下，由于使用了列表类型加上循环结构，我们对数据的处理是批量性的，这就使得修改后的代码比之前的代码要简单优雅得多。
