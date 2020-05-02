#6.1 while循环
# (1) 逻辑 : 只要条件为True，while 子句中的代码就会执行


# (2) 语法结构
# 1) while关键字
# 2) 可选关键字: break , continue
# 3) 条件（值为True 或 False 的表达式）；
# 4) 冒号
# 5) 代码块缩进









"""
n = 1
while( n<= 100):
    print(n)
    n = n + 1
"""







"""
sum = 0
n = 1
while( n<= 100):
    sum = sum + n                 #  sum += n
    n = n + 1
print(sum)

"""















# (3) break语句
# 含义: 让执行提前跳出 while 循环






"""


print("你知道585的二进制数是多少吗 ?")
bit = "1111"
while True:
    code = input("请二进制数: ")
    if(bit == code):
        print("恭喜你答对了")
        break
print("很厉害，继续加油吧 !")



"""


# (3) continue 语句
# 含义: 跳出本次循环


"""
sum = 0
n = 0
while( n<= 10):
    n = n + 1
    if (n % 2 == 1):
        continue
    else:
        sum += n
print(sum)

"""




# 6.2 range()函数
# 生成一个数列，有三种形式
# (1) range(n)

# for i in range(10):
#     print(i)






# (2) range(a, b)

#for i in range(3,9):
#    print(i)







# (3) range(a, b, n)   指定步长
#for i in range(5,100,12):
#    print(i)








# 6.3 for循环
# (1) 语法结构

# for <variable> in <sequence>:
#     <statements>



# 1) for 关键字；
# 2) 一个变量名；
# 3) in 关键字；
# 4) 序列 : 一个列表,字典,字符串或者range()都可以



"""
sum = 0
for i in range(101):           # 0 1 2 3 4 5 6 7 ... 100
    sum += i   # sum = sum +i
print(sum)
"""





string = "abcdefghijkl"
for i in string:
    print(i)






