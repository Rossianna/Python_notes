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
# 
