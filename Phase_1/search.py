# 二分查找

'''
二分查找的本质:
给定一个升序数组和目标值，找到目标值的位置。
— 看起来简单，但它背后的"边界思维"会贯穿你整个学习旅程。
'''

'''
第一题: 二分查找

问题描述:
给定一个升序排列、无重复元素的整数数组 nums, 和一个目标值 target。
请你找出 target 在数组中的下标，如果不存在则返回 -1。

示例:
输入: nums = [1, 3, 5, 7, 9, 11, 13], target = 7
输出: 3

输入: nums = [1, 3, 5, 7, 9, 11, 13], target = 6
输出：-1

引导思考:
第一步：最笨的方法是什么？
假设你完全不知道这个数组是有序的，你会怎么找？时间复杂度是多少？

第二步：有序这个条件能帮你什么？
想象你在查一本字典，你会从第一个字一个个往后翻吗？你实际上会怎么做？

第三步：二分的核心直觉
每次查找，你都可以选一个位置"试探"一下：

如果试探的值等于 target → 找到了
如果试探的值大于 target → target 只可能在哪边？
如果试探的值小于 target → target 只可能在哪边？

每次试探之后，问题规模变成了原来的多少？

想一想这个数学问题:
一个长度为 n 的数组，每次排除一半，最多需要试探几次才能确定答案？
提示: n -> n/2 -> n/4 -> ... -> 1, 这是什么数学关系？

实现:
你需要维护两个边界 left 和 right
每次取中间位置 mid
根据比较结果缩小范围
思考循环的终止条件是什么
'''

'''
细节1: mid 怎么算？
left 和 right 的中间位置，最直觉的写法是：

mid=(left+right)/2mid = (left + right) / 2mid=(left+right)/2
先用这个，之后我们会讨论它隐藏的一个问题。
细节2: 边界更新时, mid 要不要包含在新范围里？
找到 mid 之后，已经知道 nums[mid] != target 了，那新的范围应该是：

left = mid 还是 left = mid + 1?
right = mid 还是 right = mid - 1?

细节3: 循环终止条件是什么？
while left < right 还是 while left <= right? 想想什么时候该停。
'''
def binary_search(arr, target) -> int:
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2
        # mid = (left + right) / 2 --> 结果为float类型 --> TypeError: list indices must be integers or slices, not float
        if (arr[mid] == target):
            return mid
        elif (arr[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11, 13], 7))
print(binary_search([1, 3, 5, 7, 9, 11, 13], 6))

'''
mid = (left + right) // 2
在 Python 里这没问题，因为 Python 的整数是任意精度的，不会溢出。
但在 C / C++ / Java 里, int 类型有上限: 2^31 - 1 大约等于 2.1 * 10^9

如果 left = 1,000,000,000, right = 1,500,000,000:
left+right=2,500,000,000 > 2^31 - 1
加法本身就溢出了, mid 会变成一个负数，程序崩溃

工业界的标准写法是：
mid = left + (right - left) / 2
数学上完全等价，但避免了中间值溢出。这是你以后写 C++/Java 时需要养成的习惯。
'''

'''
拓展视野:
二分查找的本质不是"在数组里找值"，而是：
    在一个有单调性的空间里，快速定位边界。

现实中的应用：
Git 的 git bisect: 在几千个 commit 里，用二分找到引入 bug 的那一个
数据库索引: B树的查找本质上是多路二分
工程中"猜答案"：如果一个问题的答案具有单调性（答案越大越满足/不满足某条件），就可以二分答案，而不是暴力枚举
'''


'''
第二题：寻找边界
二分思想的一个经典变种，会让你对"边界"的理解更上一层楼 

问题描述:
给定一个升序排列、但有重复元素的整数数组 nums, 和一个目标值 target。
请你找出 target 在数组中第一次出现的下标。如果不存在则返回 -1。

示例：
输入: nums = [1, 3, 3, 3, 5, 7, 9], target = 3
输出: 1   ← 第一个3的下标

输入: nums = [1, 3, 3, 3, 5, 7, 9], target = 6
输出：-1

引导思考
第一步：直接用上一题的代码行吗？
上一题的代码找到的是"某一个" target,但不保证是第一个。比如上面的例子，它可能直接返回下标 2 (中间那个3)，而不是 1

第二步：找到一个 target 之后，怎么办？
假设你用二分找到了 nums[mid] == target, 但你不知道它是不是第一个
此时你能排除哪一半？

第三步：思考终止条件的变化
上一题找到就立刻 return mid, 这题能这样做吗？
如果不能立刻返回，你需要把"找到的位置"记录下来，然后继续往哪个方向缩小范围？


想一想
最终 left 和 right 会收缩到同一个位置，这个位置就是答案。但你需要思考：
收缩到最后，你怎么判断这个位置上的值确实是 target,而不是 target 根本不存在？
'''

def binary_search_first_index(arr, target) -> int:
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2
        if (arr[mid] == target):
            if (left == right):
                return left
            right = mid
        elif (arr[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binary_search_first_index([1, 3, 3, 3, 5, 7, 9], 3))
print(binary_search_first_index([1, 3, 3, 3, 5, 7, 9], 6))