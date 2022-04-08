def bubble_sort(nums):
    N = len(nums)
    for i in range(N - 1):
        for j in range(N - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums=[5,8,3,4,2,6,7]
num = bubble_sort(nums)
print(num)