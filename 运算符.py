# 关系运算符
# 赋值运算符
# 算数运算符
# 逻辑运算符

# Python中比较两个字符串，实际上是比较字符串的Unicode编码，逐位比较
result = 'ab' > 'b' # False
result = 'abc' > 'ab' # True
# 如果不希望比较两个字符串的Unicode编码，则需要将其转换为数字然后再比较
print(int('2') < int('11')) # True
# 关系运算符用来比较两个值之间的关系，总是会返回一个布尔值
result = 1 == True # True


# is 比较两个对象是否是同一个对象，比较的是对象的id
# is not 比较两个对象是否不是一个对象，比较的是对象的id
result = 1 is not True # True, 1的id和True的id不一样


# 逻辑运算符
# not 逻辑非
# and 逻辑与
# or 逻辑或
a = 2
a = not a
print(a) # 输出False，所以可以认为，Python中，对于非零的数取not，都会得到False
# not 可以对符号右侧的值进行非运算
#    对于布尔值，非运算会对其进行取反操作，True变成False，False变成True
#    对于非布尔值，非运算会先将其转换为布尔值，然后再取反

# and可以对符号两侧的值进行与运算
#    只有在符号两侧都为True时，才会返回True，只要有一个False就会返回False
#    注意，and是“短路”的

# or可以对符号两侧的值进行或运算
#    只要有一个True就会返回True
#    注意，or也是“短路”的


# 非布尔值的与或运算
# 当我们对非布尔值进行与或运算时，Python会将其当做布尔值运算，最终返回原值
# 与运算：如果第一个值是False，则返回第一个值，否则返回第二个值
# 或运算：如果第一个值是True，则返回第一个值，否则返回第二个值  
result = 1 and 0 # 0

# 逻辑运算符可以连用
result = 1 < 2 < 3 # True,相当于2 > 1 且 2 < 3
result = 10 < 20 > 15 # True,相当于20 >10 且 20 > 15



# 条件运算符（三元运算符）
# 语法：语句1 if 条件表达式 else 语句2
#     条件运算符在执行时，会先对条件表达式进行求值判断，如果判断结果为True，则执行语句1并返回执行结果
#                                                  如果判断结果为False，则执行语句2，并返回执行结果

# 通过条件运算符获取三个值中的最大值
a = 10
b = 20 
c = 30 # a,b,c随便取
# 方法1：
max = a if a > b else b
max = max if max > c else c
# 方法2：
max = a if (a > b and a >c) else (b if b > c else c)
print(max)



# 运算符的优先级
# ！and的优先级高于or
# 用括号改变优先级
