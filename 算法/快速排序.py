"""
对一串列表数字进行快速排序
思路：
    找一个基准值
    然后用切片切出剩余列表
    遍历该列表 用遍历值于基准值进行比较
    比基准值大的放一边 比基准值小的放一边  即递归条件
    递归 反复调用该函数
    出口为：当列表长度为1或者为0时，默认无需排序了  即基线条件
"""

def quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        less = (i for i in arr[1:] if i <= pivot)
        greater = (i for i in arr[1:] if i > pivot)
        return quicksort(less) + pivot + quicksort(greater)
arr = [4,5,8,2,9,6,3]
quicksort(arr)

"""
散列表  python中就是字典
值和名称相对应
每次给相同名称返回相同一致的值
散列表适合用于：
 模拟映射关系；
 防止重复；
 缓存/记住数据，以免服务器再通过处理来生成它们。
"""
# biao = {}
#
# def char(name):
#     if biao.get(name):
#         print("gun")
#
#     else:
#         biao[name] = True
#         print('欢迎')
#
# char("tom")
# char("ma")
# char("dada")
# char("tom")
