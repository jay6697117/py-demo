# # 定义一个三元组
# t1 = (35, 12, 98)
# # 定义一个四元组
# t2 = ('骆昊', 45, True, '四川成都')


# # 拼接运算
# t3 = t1 + t2
# print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')

# # 比较运算
# print(t1 == t3)            # False
# print(t1 >= t3)            # False
# print(t1 <= t3)            # True
# print(t1 <= (35, 11, 99))  # False
# print(t1 >= (35, 11, 99))  # True



# 一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。我们可以通过下面的代码来加以验证。

a = ()
print(type(a))  # <class 'tuple'>
b = ('hello')
print(type(b))  # <class 'str'>
c = (100)
print(type(c))  # <class 'int'>
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>
