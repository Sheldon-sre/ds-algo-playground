# 滑动窗口

'''
问题描述:
给定一个整数数组 nums 和一个整数 k, 找出所有长度为 k 的连续子数组中，和最大的那个，返回这个最大和。

示例:
输入: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
输出: 16
解释：
     [1,3,-1]=3, [3,-1,-3]=-1, [-1,-3,5]=1, 
     [-3,5,3]=5, [5,3,6]=14, [3,6,7]=16
     最大是 16

引导思考:
第一步：暴力解法是什么？
    两层循环，枚举每个窗口，算出每个窗口的和，时间复杂度是多少？
第二步：暴力解法浪费了什么？
    从窗口 [1,3,-1] 移动到 [3,-1,-3] 时，你重新把三个数加了一遍。
    但这两个窗口之间有什么关系？
    新窗口的和 = 旧窗口的和 - 滑出的元素 + 滑入的元素
第三步：这意味着什么？
    你只需要维护一个"窗口的和"，每次移动只做一次减法和一次加法，而不是重新求和。

复杂度对比
暴力: O(n * k)
滑动窗口: O(n)
'''

def normal_method(arr, k):
    left = 0
    right = k - 1
    result = 1e-9 # 无穷小
    boundary = len(arr)
    while(right < boundary):

        val = sum(arr[left:right+1])
        if val > result:
            result = val
        left += 1
        right += 1
    return result

def sliding_window(arr, k):
    left = 0
    right = k
    previous_window = sum(arr[0:k])
    result = previous_window # 以第一个窗口值为起始值, 避免少比较一次
    boundary = len(arr)

    while right < boundary:
        val = previous_window + arr[right] - arr[left]
        if val > result:
            result = val
        
        previous_window = val
        left += 1
        right += 1
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(normal_method(nums, k))
print(sliding_window(nums, k))

'''
延伸思考
这道题的窗口大小是固定的 k。
但现实中很多问题的窗口大小是可变的，比如：
    找最长的连续子数组，使得其中所有元素之和不超过 S
这时候窗口需要动态伸缩, left 和 right 不再同步移动。这是滑动窗口最强大的形态，我们之后会遇到它。
'''

def longest_continuous_subarray(arr, s):
    left = 0
    right = 1
    previous_sum = arr[0]
    boundary = len(arr)
    result = [arr[0]]
    max_length = 0
    while right < boundary:
        while previous_sum <= s:
            previous_sum = previous_sum + arr[right]
            result.append(arr[right])
            right += 1
        previous_sum = previous_sum - arr[left]
        if len(result) > max_length:
            result.remove(arr[left])
            max_length = len(result)
        left += 1
    return result
nums = [1, 7, 3, 1, 5, 0, 1, 7]
s = 10

print(longest_continuous_subarray(nums, s))