# 查找函数
def findSmallest(arr):  #arr = [5,8,6,2,4,9,3]
    # 存储最小值
    smallest = arr[0]
    # 存储最小值索引
    smallest_index = 0
    # 循环遍历 起始位置为1,因为0值我们取了 最大位置是列表长度
    for i in range(1,len(arr)):
        # 条件判断 如果列表中有值小于我们设置的初始值
        if arr[i] < smallest:
            # 让小的值替换掉初始值
            smallest = arr[i]
            # 那个值的位置索引也相应替换
            smallest_index = i
    # 循环完成后 返回最小值索引位置
    return smallest_index

# 选择排序函数
def selectionSort(arr):
    # 定义一个空列表来存储查找出的数
    new_arr = []
    # 循环 条件：当长度不大于要排序的列表长度时
    # 这个地方循环调用了列表长度次数的查找函数
    # 才能使查找函数不断执行返回每次执行的相应最小值
    for i in range(len(arr)):
        # 调用查找函数 返回当前列表最小值的位置
        smallest = findSmallest(arr)
        # 将查找出来的最小值依次往空列表中添加
        # pop函数作用是删除指定位置值 并返回当前值
        # 接受到查找函数返回的最小值索引 添加后并将其删除 这样下次查找的最小值就会是排在上一次最小值之上的数
        new_arr.append(arr.pop(smallest))
    # 返回排序好的列表
    return new_arr

arr = [5,8,6,2,4,9,3]
print(selectionSort(arr))







def chazhaohanshu(arr):
    small = arr[0]
    small_indx = 0
    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            small_indx = i

    return small_indx

def xuanzhepaixu(arr):
    new_arrl = []
    for i in range(len(arr)):
        small = chazhaohanshu(arr)
        new_arrl.append(arr.pop(small))
    return new_arrl


print(xuanzhepaixu([5, 8, 7, 9, 1, 4, 6, 3]))



















