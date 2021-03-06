# +:将两个列表拼接为一个新的列表
my_list = [1,2,3]+[4,5,6] #得到[1,2,3,4,5,6]

# *:将列表重复指定的次数
my_list = [1,2,3] * 5

# in:用来检查指定元素是否存在于列表中，存在返回True，不存在返回False
list_stu = ['小红','小蓝','小黄','小绿','小白','小黑','小蓝','小蓝']
print('小红' in list_stu) # 结果会返回True

# not in:用来检查指定元素是否不在列表中，不在则返回True，否则返回False

# len():用于获取列表中元素的个数
# min(arr):用于获取arr列表中的最小值
# max(arr):用于获取arr列表中的最大值
arr = [10,1,2,5,100,77]
print(min(arr),max(arr)) # 输出1 100

# 两个方法(method)，方法和函数基本上是一样，只不过方法必须通过 对象.方法()的形式调用
# xxx.print() 方法实际上就是和对象关系紧密的函数
# s.index() 获取指定元素在列表中的第一次出现时的索引
# index()的第二个参数表示查找的起始位置，第三个参数表示查找的结束位置
print(list_stu.index('小蓝',2,7)) # 结果返回6，因为在2-7这个位置之间的'小蓝'在位置6
