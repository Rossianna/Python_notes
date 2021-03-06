# 在python中，数值分成了三种：整数、浮点数（小数）、复数
# 在python中，所有整数都是int类型
# python中的整数大小没有限制，可以是一个无限大的整数
# **表示幂
max_length = 2 ** 2
print(max_length)
# 得到的结果是4

# 如果数字的长度过大，可以使用下划线作为分隔符，十进制的数字不能以0开头
c = 123_456_789
print(c)
# 下划线在显示时会被自动忽略，打印输出123456789

# 其他进制的整数，只要时数字，打印时，一定是以十进制的形式显示的
#    1.二进制     0b开头
#    2.八进制     0o开头
#    3.十六进制   0x开头


# 浮点数（小数），在python中所有的小数都是float类型，对浮点数进行运算时可能得到不精确的结果）
c = 0.1 + 0.2
print(c)
# 不会得到0.3而会得到0.3000000...0004
