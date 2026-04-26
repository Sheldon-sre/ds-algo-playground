# 双指针

'''
问题描述
给定一个升序排列的整数数组 nums 和一个目标值 target，找出数组中两个数，使得它们的和等于 target，返回这两个数的下标。
保证有且只有一个答案

示例：
输入：nums = [1, 2, 4, 6, 8, 11, 15], target = 10
输出：[2, 3]
解释：nums[2] + nums[3] = 4 + 6 = 10

引导思考
第一步：暴力解法是什么？
    枚举所有两个数的组合，时间复杂度是多少？
第二步：有序这个条件能帮你什么？
    把左指针放在最左边（最小值），右指针放在最右边（最大值），计算两者之和：
    如果和等于 target → 找到了
    如果和大于 target → 说明什么？应该移动哪个指针？
    如果和小于 target → 说明什么？应该移动哪个指针？
第三步：为什么这样移动指针是正确的？
    当和大于 target 时，移动右指针，你真的不会错过正确答案吗？
    这是双指针正确性的核心，想清楚这个问题。

    因为是单调性的
    比如说left = 0 , right = len(arr) - 1时, 如果 sum < target --> 所有的right  = 1 , = 2, .. = len(arr) - 1 都是不符合要求的, 但是只需要
    判断right = len(arr) -1即可，因为right向左移动(left = 0不变)，sum是单调递减的, sum只会更小, 所以说判断right = len(arr) - 1之后, 就直接
    排除right = 0 ...的所以情况了(left = 0不变)  
复杂度对比
    暴力枚举 O(n^2)
    双指针 O(n)
'''

def normal_method(arr, target):
    sum = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

def two_pointers(arr,target):
    left = 0
    right = len(arr) - 1

    while left < right:
        val_left = arr[left]
        val_right = arr[right]
        val = val_left + val_right

        if val == target:
            return [left, right]
        if val > target:
            right -= 1
        else:
            left += 1
    return []

nums = [1, 2, 4, 6, 8, 11, 15]
target = 10

print(normal_method(nums, target))
print(two_pointers(nums, target))