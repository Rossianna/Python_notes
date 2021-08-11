# while循环 for循环
# while循环
# 语法：
# while 条件表达式:
#    代码块
# else:
#    代码块
# 执行流程：在执行时，会先对while后的条件表达式进行求值判断，如果为True，则执行代码块内容
# 循环体执行完毕，继续对条件表达式进行求值判断，以此类推，直到判断结果为False，则循环终止；如果循环有对应的else，则执行else后的代码块


# break 和 continue
# break用于立即退出循环（包括else，else的部分不会执行，直接退出）
# continue用于跳过当次循环（只跳过这一次循环）
# break和continue都只对离它最近的循环起作用

i = 0
if i < 5:
  pass # pass在这里没有实际意义，当在开发时没有想好功能的时候，可以先这么写
