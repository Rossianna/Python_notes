# 列表是python的对象
# 创建列表
my_list = [] # 创建一个空列表

# 列表中存储的数据称为元素，一个列表中可以存储多个元素，也可以在创建列表时，来指定列表中的元素
my_list = [10] # 创建一个只包含一个元素10的列表

# 当向列表中添加多个元素时，多个元素之间使用','隔开
my_list = [10,20,30,40,50] # 创建了一个包含有5个元素的列表

# 列表中可以保存任意对象
my_list = [10,'hello',True,None,[1,2,3],print]

# 列表的对象会按插入顺序存储到列表中

# 可以通过索引(index)获取列表中的元素，索引是元素在列表中的位置，列表中的每个元素都有索引
# 索引从0开始
my_list[0]

# 获取列表的长度
len(my_list)
print(len)  # len函数用来获取列表的长度（列表中元素的个数）

# 列表的索引可以是负数
# 如果索引是负数，则从后往前获取元素，-1表示倒数第1个，-2表示倒数第2个，以此类推
list_stu = ['小红','小蓝','小黄','小绿','小白','小黑']
print(list_stu[-2]) # 得到 小蓝

# 列表的切片（从现有列表中获取子列表）
# 做切片操作时，总会返回一个新的列表（原本的列表不变）
# 语法：列表[起始:结束]
# 通过切片获取元素时，会包括起始位置的元素，不会包括结束位置的元素
print(list_stu[0:2]) # 得到['小红','小蓝']
print(list_stu[1:]) # 得到['小蓝','小黄','小绿','小白','小黑']
print(list_stu[:3]) # 得到['小红','小蓝','小黄']，省略起始位置，会从第1个元素开始截取
print(list_stu[:]) # 得到['小红','小蓝','小黄','小绿','小白','小黑']


# 语法：列表[起始:结束:步长]
# 默认步长为1，步长不能为0，可以为负数
# 步长为负数时，会从列表的后部向前取元素，步长=-1时，相当于把列表倒过来

