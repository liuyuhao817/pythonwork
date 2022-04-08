"""
1、冒泡排序
2、选择排序
3、插入排序
4、堆排序
5、归并排序
6、快速排序
"""

#1、冒泡排序

def maopao(num):

    for i in range(len(num)-1):    #为什么要len-1 因为比较到最后一位了就无需比较了
        for j in range(len(num)-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    return num
num=[4,8,6,5,9,7,3]
# print(maopao(num))

#2、选择排序
# 将第一个数定位最小，然后挨次跟后面数比较，如果大于后面的数，就将那个数的下标赋予初始定位最小的
# 最后，将比较完后的下标找到对应值，将它与第一位交换位置。
# 是重复“从待排序的数据中寻找最小值，将其与序列最左边的数字进行交换”
def xuanze(num):

    for i in range(len(num)):
        min_num=i
        for j in range(i+1,len(num)):
            if num[min_num] > num[j]:
                min_num=j
        num[i],num[min_num]=num[min_num],num[i]
    return num

num1=[4,8,6,5,9,7,3]
# print(xuanze(num1))


# 插入排序

def charu(num):

    for i in range(1,len(num)):
        key=num[i]
        j=i-1
        while j>=0 and num[j]>key:
            num[j+1]=num[j]
            j-=1
        num[j+1]=key
    return num

num2=[7,6,5,4,3,2,1]
print(charu(num2))

