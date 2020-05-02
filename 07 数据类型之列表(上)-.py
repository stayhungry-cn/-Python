#7.1 列表简介
# (1) 定义: 列表是由数字或者字符串等组成的序列，左方括号开始，右方括号结束
# (2) 列表中的值用逗号分隔
"""
sequence_1 = ["dog", "cat", "panda", "tiger"]
sequence_2 = [1, 2 ,3, 5, 8]
sequence_3 = ['bonjour', 0.618 ]
sequence_4 = ['bonjour', [1,2,3] , int(6.66) ]


print(sequence_1)
print(sequence_2)
print(sequence_3)

# 不能直接用print打印列表
"""

#7.2 访问列表元素
# 1) 按索引访问
sequence = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
        #     0         1        2        3        4        5        6
        #    -7        -6       -5       -4       -3       -2        -1


#print(sequence[0])
#print(sequence[-7])


#print(sequence[1])
#print(sequence[-6])


#print(sequence[6])
#print(sequence[-1])









"""
seq = [["a", "b"], [1, 2]]


print(seq[0])
print(seq[1])


print(seq[0][0])

print(seq[0][1])
"""




#2) for 循环访问



"""
sequence_4 = ['a', 'b', 'c', 'd', 'e', 'f']
for item in sequence_4:
    print(item)

"""




# 3) 利用切片获取子列表

"""

sequence_4 = ['a', 'b', 'c', 'd', 'e', 'f']
seq_1 = sequence_4[:4]
print(seq_1)







sequence_4 = ['a', 'b', 'c', 'd', 'e', 'f']
seq_2 = sequence_4[1:]
print(seq_2)


seq_3 = sequence_4[1:3]
print(seq_3)



seq_4 = sequence_4[ : ]
print(seq_4)


"""






#7.3 操作列表

# 1) 修改列表元素
"""
sequence_4 = ['a', 'b', 'c', 'd', 'e', 'f']
sequence_4[2] = 3
sequence_4[4] = 'k'
print(sequence_4) 

"""



"""
# 2) 用 del 语句删除列表中某个值
sequence_4 = ['a', 'b', 'c', 'd', 'e', 'f']


del sequence_4[2]
print(sequence_4)

del sequence_4[2]
print(sequence_4)






# 3) 列表的连接与复制
# + 操作符连接两个列表
sequence_1 = ['huawei', 'xiaomi', 'apple']
sequence_2 = ['yijia', 'oppo']
marque = sequence_1 + sequence_2
print(marque)

"""



# * 操作符:
sequence_3 = ['a', 'b', 'c']
seq = sequence_3 * 5
print(seq)


print("#"*25)




