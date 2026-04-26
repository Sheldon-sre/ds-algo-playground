# 哈希表

'''
问题描述
给定一个无序整数数组 nums 和目标值 target，找出两个数之和等于 target，返回它们的下标。

保证有且只有一个答案。

示例
输入：nums = [3, 1, 8, 2, 6], target = 9
输出：[1, 2]
解释：nums[1] + nums[2] = 1 + 8 = 9

思考一个细节
你的思路已经完整了，直接实现就好。(先查表, 如果target - num[i]不存在, num[i] 和 i 入表; 存在, 返回[table[target - num[i]],i])
但实现前思考一下：
哈希表里存的是 {数值: 下标}，当你找到 target - nums[i] 在哈希表里时，返回的两个下标分别是什么？

复杂度
暴力 O(n^2) O(1)
哈希表 O(n) O(n)

这是一个经典的以空间换时间的例子。
'''

def hash_table(arr, target):
    hash_table = {}
    length = len(arr)

    for i in range(length):
        expect_val = target - arr[i]
        if expect_val in hash_table:
            return [hash_table[expect_val], i]
        else:
            hash_table[arr[i]] = i
    return []

nums = [3, 1, 8, 2, 6]
target = 9

print(hash_table(nums, target))
