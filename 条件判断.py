# if-else

# if -elif-else
# 语法：
# if 条件表达式:
#    代码块
# elif 条件表达式:
#    代码块
# elif 条件表达式:
#    代码块
# elif 条件表达式:
#    代码块
# else:
#    代码块

# 执行流程：
# if-elif-else语句在执行时，会自上向下依次对条件表达式进行求值判断，
# 如果表达式结果为True，则执行当前代码块，然后语句结束
# 如果表达式的结果为False，则继续向下判断，直到找到True为止
# 如果所有表达式都为False，则执行else后的代码块

# if-elif-else中只有一个代码块会执行

# 编写一个程序，获取用户输入的整数，然后通过程序显示这个数是奇数还是偶数
a = input('请输入一个整数:')
if int(a) % 2 == 0:  # 也可以直接在上一行代码进行类型转换
    print('是偶数')
else:
    print('是奇数')
    
# 编写一个程序，检查任意一个年份是否是闰年
# 如果一个年份可以被4整除，不能被100整除，或者可以被400整除，这个年份就是闰年
year = input('请输入一个年份:')
if int(year) < 1990:
    print('重新输入')
elif (int(year) % 4 == 0 and int(year) % 100 !=0) or int(year) % 400 == 0 :
    print('是闰年')
else :
    print('不是闰年')
    
    
# 狗和人类年龄换算
# 狗的前两年，每一年相当于人类的10.5岁，然后每增加一年就增加了4岁，5岁的狗相当于33岁的人类
dog_age = float(input('请输入一个年龄:'))
like_person_age = 0
if dog_age < 0:
    print('请输入正数！')
elif dog_age <= 2:
    like_person_age = 10.5 * dog_age
else:
    like_person_age = 10.5 * 2 + 4 * (dog_age - 2)
print(dog_age,'岁的狗，相当于',like_person_age,'的人')
