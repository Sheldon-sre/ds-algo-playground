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


'''
延伸思考：二分的边界本质
你现在已经实现了"找第一个"，思考一下：
找最后一个 target 的下标，代码需要改哪里？
    提示：找第一个时，找到 target 之后往左压缩。找最后一个呢？

这两个问题合在一起，就是经典的：
    给定 target, 找到它在数组中的 [左边界, 右边界]

这在实际中非常有用，比如：
    数据库查询: SELECT * FROM orders WHERE date = '2024-01-01' 本质上就是在索引里找一段连续区间的左右边界

    统计某个值出现了多少次：右边界 - 左边界 + 1
'''

def binary_search_last_index(arr, target):
    left = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2
        if (arr[mid] == target):
            if (left == right):
                return left
            left = mid
        elif (arr[mid] > target):
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(binary_search_last_index([1, 3, 3, 3, 5, 7, 9], 3))
print(binary_search_last_index([1, 3, 3, 3, 5, 7, 9], 6))

def binary_search_index_range(arr, target):
    left_boundary = 0
    right_boundary = len(arr) - 1
    left_boundary = binary_search_first_index(arr, target)
    right_boundary = binary_search_last_index(arr, target)

    return (left_boundary, right_boundary)

print(binary_search_index_range([1, 3, 3, 3, 5, 7, 9], 3))


'''
真正的延伸：二分答案
现在跳出"在数组里找值"的框架，看这个问题：
    一根绳子要切成 k 段，每段长度相同，问每段最长能有多长？
这个问题没有数组，但仍然可以用二分。

核心问题： 什么东西具有单调性，可以被二分？
    如果每段长度为 x, 能切出 k 段 → 那长度为 x-1 能切出 k 段吗？

    如果每段长度为 x+1 , 能切出 k-1 段
    如果每段长度为 x-1 , 能切出 k+1 段

每次试探 mid 作为"每段长度"，然后问
    以 mid 为每段长度，能切出几段？

    然后根据切出的段数和 k 的关系，决定往左还是往右缩小范围

关键问题
二分结束后, left 停在哪里？它就是答案吗？
这和第二题的"找边界"本质一样：你在找的是满足条件的最大的 mid。
'''

'''
二分答案

问题描述
给定一根长度为 L 的绳子，要切成至少 k 段，每段长度必须相等且为整数。
问每段最长能有多长？

示例：
输入：L = 10, k = 3
输出：3
解释：每段长3，可以切出3段（剩余1单位浪费），满足至少3段的要求

输入：L = 9, k = 3
输出：3
解释：每段长3，恰好切出3段

输入：L = 9, k = 4
输出：2
解释：每段长2，可以切出4段（剩余1单位浪费），满足至少4段的要求

引导思考
第一步：给定每段长度 x，能切出几段？
    这个计算只需要一行，想想 L 和 x 怎么运算。

第二步：二分空间是什么？
    left = 1（每段至少长1）
    right = L（每段最多长L，也就是不切）
    每次试探 mid 作为每段长度，判断能切出几段。

第三步：边界怎么更新？
    如果以 mid 为每段长度，切出的段数 >= k → 说明什么？能不能让每段更长？
    如果切出的段数 < k → 说明什么？
第四步：你在找什么边界？
    你在找满足"切出段数 >= k"的最大的 mid，对应第二题的"找最后一个"。
    循环结束后，left 还是 right 是答案？
'''

# def max_length(L, k):
#     left = 1
#     right = L

#     while(left <= right):
#         mid = (left + right) // 2
#         number = L // mid
#         if (number == k):
#             if (left == right):
#                 return left
#             left = mid
#         elif (number > k):
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# def max_length(L, k):
#     left = 1
#     right = L

#     while(left < right - 1):
#         mid = (left + right) // 2
#         number = L // mid
#         if number == k:
#             left = mid
#         elif number > k:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left

# 根据我对于测试数据集的计算和观察，最后的死循环left一直等于mid，而且此时left和right之间只差1,
# 所以说无论怎么mid = (left + right) // 2, 结果都是left，而left处就是答案，所以我修改了循环终止条件

# 隐患1：number > k 时不应该 left = mid + 1
    # 当 number > k 时，说明每段可以更长，mid 本身也是合法答案，直接 left = mid + 1 会跳过它
# 隐患2：while left < right - 1 会漏掉一些情况
    # 当数组只剩两个元素时你直接退出了，但没有检验 right 处是否是更优的答案。

def max_length(L, k):
    left = 1
    right = L

    while left < right:
        mid = (left + right + 1) // 2
        number = L // mid

        if number >= k:
            left = mid
        else:
            right = mid - 1
    return left
# 这里 mid 的计算加了 1，这是"找右边界"的关键，思考一下
# 如果 left = 1, right = 2，不加1时 mid = 1，然后 left = mid = 1，又死循环了。加1后 mid = 2，就能正常推进。
# 在上一版本中, left最后一直等于mid, 循环无法结束，这里的方法，让left最后还可以更新一次，让left = mid == right, 循环结束
print(max_length(10, 3))
print(max_length(9, 3))
print(max_length(9, 4))