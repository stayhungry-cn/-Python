# 3.1 变量
# (1) 命名
#    1) 只能包含字母、数字和下划线, 不能包含空格  ex: a, a1, is_true, est_vrai
#    2) 不能以数字开头                        ex: 正确 :b_5 错误: 5b,5_b
#    3) 不要将关键字和函数名用作变量名           ex: print, range, False, class, is, return, if 都不可以


# (2) 注意事项
#    1) 见名知义  name, age, student_id
#    2) 避免使用小写字母l，o
# (3) 赋值 "="                               ex: a = 3, b= "name"

# 3.2 字符串
# 解释:一系列字符
# ex: " To be or not to be"
# ex: "老夫聊发少年狂。左牵黄，右擎苍。锦帽貂裘，千骑卷平冈"
# ex: "3.1415926"
# ex: " Il a mis le café, Dans la tasse"

# 3.2.1 字符串操作符
# (1) 连接字符串: +
first_name = "Jacques"
last_name = "Prévert"
full_name = first_name + " " + last_name
#print(full_name)

ctf_1 = "红酥手"
ctf_2 = "黄縢酒"
ctf_3 = "满城春色宫墙柳"
ctf = ctf_1 + ", " + ctf_2 + ", " + ctf_3 + "."
#print(ctf)

# (2) 重复输出字符串: *
#print("#" * 20)
#print('-'* 20)
#print('*' * 9)
#print('*' * 8)
#print('*' * 7)
#print('*' * 6)
#print('*' * 5)
#print('*' * 4)

# 3.2.2 字符串处理函数
message_1 = "je ne sais pas"
message_2 = "I LOVE IT"
# (1) .title()        每一个单词的首字母大写
#print(message_1.title())
#print(message_2.title())

# (2) .capitalize()  只有首字母大写
#print(message_1.capitalize())
#print(message_2.capitalize())

# (3) .upper()       全部转大写
print(message_1.upper())
print(message_2.upper())

# (4) .lower()       全部转小写

#print(message_1.lower())
#print(message_2.lower())

# (5) len()          获取字符串长度
#print(len(message_1))
#print(len(message_2))




# (6) .find          字符串查找,无则返回-1
info = "abcdef abc ef"
#print(info.find('a'))
#print(info.find('b'))
#print(info.find('a',1))
#print(info.find('f',1,7))
#print(info.find('h'))


# (7).index          字符串查找,无则返回错误
#print(info.index('a'))
#print(info.index('b'))
#print(info.index('a',1))
#print(info.index('f',1,7))
#print(info.index('h'))


# (8).count          计算出现的次数
info = "abcdef abc ef"
print(info.count('a'))
print(info.count('h'))






# (9)截取字符串           ex: [0:3]从下标为0的字符开始，不包含下标为3的字符
info = "3.1415926"
#print(info[0:3])
#print(info[0:4])
#print(info[:])       # 截取全部字符串
#print(info[1])
#print(info[1:6])


