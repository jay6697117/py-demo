"""
计算三角形的周长和面积

Version: 1.0
Author: 骆昊
"""

# 从用户输入获取三角形的三条边长
a = float(input('a = '))  # 获取第一条边长
b = float(input('b = '))  # 获取第二条边长
c = float(input('c = '))  # 获取第三条边长

# 检验三条边是否能构成三角形（任意两边之和大于第三边）
if a + b > c and a + c > b and b + c > a:
    # 计算三角形周长
    perimeter = a + b + c
    print(f'周长: {perimeter:.2f}')

    # 使用海伦公式计算三角形面积
    # s为半周长
    s = perimeter / 2
    # 面积 = sqrt(s*(s-a)*(s-b)*(s-c))
    # 其中s为半周长，a、b、c为三边长
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积: {area:.2f}')
else:
    # 如果不满足三角形的边长关系，输出提示信息
    print('不能构成三角形')
