# 递归

'''
第十一题：递归的本质

问题描述
给定一个整数 n，计算斐波那契数列的第 n 项。

斐波那契数列定义为：
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)，n >= 2

示例：
输入：n = 6
输出：8
解释：0, 1, 1, 2, 3, 5, 8

引导思考
第一步：递归实现
定义本身就是递归的，直接翻译成代码即可。但思考一下：
    递归的终止条件是什么？
    如果没有终止条件会发生什么？

第二步：递归的代价
计算 F(5) 时，展开递归树：
F(5) = F(4) + F(3)
F(4) = F(3) + F(2)
F(3) = F(2) + F(1)
...
F(3) 被计算了几次？F(2) 呢？
这棵递归树的时间复杂度是 O(2^n)，非常低效。

第三步：记忆化搜索
既然重复计算是问题所在，能不能把已经算过的结果存起来，下次直接查表？
用一个字典 memo 存储已计算的结果：
    计算前先查 memo，有就直接返回
    没有就计算，计算完存入 memo
这叫记忆化搜索，是递归到动态规划的过渡思想。

第四步：自底向上
其实不用递归，从 F(0), F(1) 开始，逐步推到 F(n)，这叫迭代法，时间复杂度 O(n)，空间复杂度 O(1)

复杂度对比
朴素递归 O(2^n) O(n)
记忆化搜索 O(n) O(n)
迭代法 O(n) O(1)
'''

def simple_recursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return simple_recursion(n-1) + simple_recursion(n-2)

# memo = {"0": 0, "1": 1}
# def memoized_search(n):
#     if str(n) in memo:
#         return memo[str(n)]
#     val = memoized_search(n-1) + memoized_search(n-2)
#     memo[str(n)] = val
#     return val

# 一个小建议：memo 的键可以直接用整数，不需要转成字符串，Python 字典支持任意可哈希类型作为键：
memo = {0: 0, 1: 1}
def memoized_search(n):
    if n in memo:
        return memo[n]
    val = memoized_search(n-1) + memoized_search(n-2)
    memo[n] = val
    return val

def iteration_method(n):
    f0 = 0
    f1 = 1
    while n:
        num = f1
        f1 = f0 + f1
        f0 = num
        n -= 1
    return f0

n = 6
print(simple_recursion(n))
print(memoized_search(n))
print(iteration_method(n))

'''
延伸思考
斐波那契其实还有一个 O(log⁡n)的解法，用到了矩阵快速幂：
[F(n+1)F(n)​]=[11​10​]n[10​]
矩阵的 n 次幂可以用快速幂做到 O(log⁡n)。这是一个很漂亮的数学结论，了解即可，我们之后遇到快速幂时会再提到它。
'''

'''
递归最强大的应用是回溯，它能解决一类"枚举所有可能"的问题：
    给定一组数，找出所有可能的组合、排列、子集
    这类问题暴力法根本写不出来，但用回溯可以优雅地解决。
'''

'''
第十二题：回溯

问题描述
给定一个无重复元素的整数数组 nums，返回它所有可能的子集。

示例：
输入：nums = [1, 2, 3]
输出：[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

引导思考
第一步：子集有多少个？
n 个元素的数组，每个元素有"选"或"不选"两种状态，所以共有2^n个子集。这意味着任何算法都至少是O(2^n)，因为光是输出答案就需要这么多时间。

第二步：用树来理解回溯
把决策过程画成一棵树：

每一层对应一个元素，左分支表示"选"，右分支表示"不选"，所有叶子节点就是所有子集。

第三步：回溯的代码结构
def backtrack(start, current):
    result.append(current[:])  # 记录当前子集
    for i in range(start, len(nums)):
        current.append(nums[i])    # 选择
        backtrack(i + 1, current)  # 递归
        current.pop()              # 撤销选择 ← 这是回溯的核心

思考一下：
    start 的作用是什么？为什么需要它？ --> 当前真正枚举(选/不选)的元素下标
    current[:] 为什么要加 [:]，直接传 current 行吗？ --> 当前子集的浅拷贝, 不能直接传current, 因为这样相当于是向result中加入同一个current的引用
    current.pop() 撤销选择，对应树上的什么操作？ --> 回溯

    start 的作用？
    防止重复选择同一个元素，保证每次只往后选，比如选了 [1,2] 就不会再生成 [2,1]。
    current[:] 为什么要加 [:]？
    因为 current 是一个列表，直接传引用的话，后续的 pop() 会修改已经加入 result 的子集。[:] 创建了一个副本，保存的是当前状态的快照。
    current.pop() 对应树上的什么操作？
    回到父节点，撤销刚才的选择，去探索另一条分支。
'''


result = []
nums = [1, 2, 3]
def backtrack(start, current):
    result.append(current[:]) # 记录当前子集
    for i in range(start, len(nums)): # 从当前元素开始，进行枚举, 选/不选
        current.append(nums[i]) # 选择
        backtrack(i+1, current) # 枚举剩下的元素
        current.pop() # 撤销选择, 相当于不选

backtrack(0,[])
print(result)