#5.1 布尔值与布尔操作符
# (1) 布尔值(1,0)
True
False
# 备注: T 和 F 要大写








# (2) 布尔操作符
# 与 : and
#print(True and True)
#print(True and False)
#print(False and False)

# 或 : or
#print(True or True)
#print(True or False)
#print(False or False)

# 非 : not
#print(not True)
#print(not False)




# 5.2 比较操作符
# (1) 等于: ==
#print(666==666)
#print(666==999)

# 备注: =为赋值符号，==为比较操作符，作用是判断两边的值是否相等，相等则返回True，不等则返回False


# (2) 不等于: !=
#print(666!= 666)
#print(666!= 999)








# (3) 小于: <
#print(666 < 999)
#print(999 < 666)






# (4) 大于: >
#print(666 > 999)
#print(999 > 666)




# (5) 小于等于: <=
#print(666 <= 999)
#print(999 <= 666)

# (6) 大于等于: >=
#print(666 >= 999)
#print(999 >= 666)





# 5.3 条件语句
# (1) 什么是条件语句



# (2) 语法结构
# 1) 关键字: if, else, elif
# 2) 条件: 表达式为True 或者 False
# 3) 冒号
# 4) 缩进: 在条件成立下执行的命令须缩进




# (3) 形式
# 1) if 结构
#price = input("请输入心理预期的价格:")
#price = int(price)
#if (price > 8000):
#    print("太贵了，得想一个理由 !")




# 2) if - else 结构
#price = int(input("请输入心理预期的价格:"))
#if (price > 8000):
#    print("太贵了，得想一个理由 !")
#else:
#    print("不算贵，可以买")



# 3) if - elif (- else) 结构
#price = int(input("请输入心理预期的价格:"))
#if (price > 8000):
#    print("太贵了，得想一个理由 !")
#elif (price > 6000):
#    print("还是有点贵，商量一下换个礼物 !")
#elif (price > 4000):
#    print("这个价格还可以接受，再磨一磨试试看还能不能再低 !")
#else:
#    print("这个可以有了 !")






# 习题
"""
 输入一个年份，判断是否是闰年。
 条件:
 (1) 计算这一年份能否被4整除。如果不能，它就不是闰年，比如2013年就不是闰年。
 (2) 计算这一年份能否被100整除。如2012年可以被4整除，但不能被100整除，它就是闰年。
     而如果某个年份，比如2000年，既能被4整除，又能被100整除，就继续往下读。
 (3) 计算这一年份能否被400整除。如1900年能被100整除，但不能被400整除，它就不是闰年。
     如果某一年份既能被100整除又能被400整除，比如2000年，那这一年份就是闰年。
"""

year = int(input("请输入一个年份:"))
is_leap_year = True
if (year % 4 != 0):
    is_leap_year = False
else:
    if (year % 100 != 0):
        is_leap_year = True
    else:
        if(year % 400 != 0):
            is_leap_year = False
        else:
            is_leap_year = True

if (is_leap_year):
    print(str(year) + "年是闰年")
else:
    print(str(year) + "年不是闰年")
