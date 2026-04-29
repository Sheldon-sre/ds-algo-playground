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