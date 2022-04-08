# import time
# def countdown(i):
# #基线条件 函数不再调用自己 即出口
#     if i < 0:
#         return print("程序结束")
# # 递归条件 函数调用自己
#     else:
#         print(i)
#         time.sleep(0.5)
#         countdown(i-1)
#
# countdown(5)


# def func(num):
#     if num == 1:
#         return 1
#     else:
#         return num * func(num-1)
#
# result = func(5)
# print(result)

# def sum(arr):
#     if arr == []:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])
#
# arr = [2,4,8]
# result= sum(arr)
# print(result)

'''
找出列表中的最大值
思路：
    拿一个数和其他进行比较 小于就替换 大于就不变
'''
def max(all):
    if len(all) == 2:
        if all[0] > all[1]:
            return all[0]
        else:
            return all[1]
    else:
        sub = max(all[1:])
        if all[0] > sub:
            return all[0]
        else:
            return sub

all = [2,4,8,5,6]
result= max(all)
print(result)