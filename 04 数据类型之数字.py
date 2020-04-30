#4.1 整型与浮点型
# (1) 整型:整数,包括正整数与负整数
a = 5
b = -5

# (2) 浮点型: 带小数点的数
c = 3.14
d = 0.618


# 4.2 算术运算符
# (1) 加 : +
#print(3+2)
# (2) 减 : -
#print(5-3)
# (3) 乘 : *
#print(6*3)
# (4) 除: /
#print(5/3)

# (5) 取模(取余数) : %
#print(5%2)
#print(97%3)
#print(4%2)

# (6) 取整(向下取整) //
#print(5//2)
#print(9//2)

# 4.3 str()、int()和float()函数
# (1) str():将括号里的内容转成字符串     来源: String
#print(2020)
#print("2020")
#print(str(2020))

#print('I am ' + 20 + 'years olds')
#print('I am ' + str(20) + ' years olds')


# (2) int():将括号的内容转成整型    来源:integer
#print(int("666"))
#print("666")

#print(333+"666")
#print(333+int("666"))
#print(int(33.33))


# (3) float():将括号的内容转成浮点型
#print(float("3.14"))
#print(float(3))
#print(float("3"))


# 4.4 input()函数
# 通过键盘输入，按下回车键后返回**字符串**
price_1 = input("Please enter the price of the book:")
price_2 = input()
total_price = price_1 + price_2
print(total_price)

total_price_ = int(price_1) + int(price_2)
print(total_price_)