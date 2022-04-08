"""
二分查找：
    每次从中间查找
    框出范围 最大最小
    查找此数 然后与最大那位进行比较 如果小于最大那位 就是在此范围
    不然报错退出
    然后进入循环 判断是否与最大那位相等 是 返回该数位置
    不是 判断是否大于中间那位数 是则最小位置变成中间数位置
    不是 判断是否小于中间那位数 是则中间那位数位置变成最大位置 反复循环
"""


def Binary_searc(list,num):
    low = 0  #low height 用于跟踪要在其中查找的列表部分
    height = len(list) - 1
    while low <= height: #只要列表范围没有缩小到只包含一个元素
        mid = int((low + height)/2)
        if num == list[mid]:#刚好等于中间数 找到了元素
            return mid#返回中间数位置
        elif num <= list[mid]:#小于中间数
            height = mid - 1
        elif num >= list[mid]:#大于中间数
            low = mid + 1
    return None#没有指定元素
my_list = [1,2,3,4,5,6,7]


print(Binary_searc(my_list,3))

#递归方式二分查找
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch(arr, l, r, x):
    # 基本判断 只要列表范围没有缩小到只包含一个元素
    if r >= l:
        mid = int(l + (r - l) / 2)
        # 元素整好的中间位置
        if arr[mid] == x:
            return mid
            # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
            # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        # 不存在
        return -1
# 测试数组
arr = [2, 3, 4, 10, 40]
x = 10
# 函数调用
result = binarySearch(arr, 0, len(arr) - 1, x)
if result != -1:
    print("元素在数组中的索引为 %d" % result)
else:
    print("元素不在数组中")


