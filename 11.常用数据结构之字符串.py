# 可以通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾；还可以用is开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。

s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True
