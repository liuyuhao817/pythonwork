"""简单可变类型的深浅拷贝"""
"""
拷贝：
    导入模块
    调用方法
        copy() 产生副本 浅拷贝
        deepcopy()  产生副本 深拷贝
"""
import copy
"""
list1 = [1,2,3]
print("list1=",list1,id(list1))#list1= [1, 2, 3] 1537552529920
# list3 = list1
# list3.append(5)
# print("list3=",list3,id(list3))
# copy() 产生副本 浅拷贝
list2 = copy.copy(list1)
print("list2=",list2,id(list2))#list2= [1, 2, 3] 1537552210304
list1.append(5)
print("list1=",list1,id(list1))#list1= [1, 2, 3, 5] 1537552529920
print("list2=",list2,id(list2))#list2= [1, 2, 3] 1537552210304
#此时 虽然是浅拷贝 但是还是会产生新的空间，并且保持数据的独立性
"""
# # deepcopy()  产生副本 深拷贝
# list1 = [1,2,3]
# print("list1=",list1,id(list1))#list1= [1, 2, 3] 2627480041984
# list2 = copy.deepcopy(list1)
# print("list2=",list2,id(list2))#list2= [1, 2, 3] 2627479722368
# #修改list2
# list1.append(4)
# print("list2=",list2,id(list2))#list2= [1, 2, 3, 4] 2627479722368
# print("list1=",list1,id(list1))#list1= [1, 2, 3] 2627480041984
# #总结：简单可变类型的深拷贝，会产生新的空间，并且保持数据的独立性


"""复杂可变数据类型拷贝问题"""

# A = [1,2,3]
# B = [11,22,33]
# C = [A,B]#[[1, 2, 3], [11, 22, 33]]
# print("A=",A,id(A))#
# print("B=",B,id(B))#
# print("C=",C,id(C))#
# print("C0=",C[0],id(C[0]))
#
# #对复杂可变类型浅拷贝
# D = copy.copy(C)
# #D产生新的空间
# print("D=",D,id(D))
# print("D0=",D[0],id(D[0]))
#
# A[0] = 10
# print("C0=",C[0],id(C[0]))
# print("D0=",D[0],id(D[0]))
# print("A=",A,id(A))

# A = [1,2,3]
# B = [11,22,33]
# C = (A,B)
# print("A=",A,id(A))#
# print("B=",B,id(B))#
# print("C=",C,id(C))
# D = C[:]
# print("D=",D,id(D))
# print("D0=",D[0],id(D[0]))
# print("C0=",C[0],id(C[0]))

import sys
#查看环境变量
for p in sys.path:
    print(p)