# 动态规划

'''
第十四题：动态规划入门

问题描述
你正在爬楼梯，每次可以爬 1级 或 2级台阶，爬到第 n 级台阶共有多少种不同的方法？

示例：
输入：n = 3
输出：3
解释：1+1+1, 1+2, 2+1 三种方法

输入：n = 4
输出：5
解释：1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 五种方法

引导思考
第一步：最后一步能告诉你什么？
站在第 n 级台阶上，你的最后一步只有两种可能：

从第 n-1 级跨 1 步上来
从第 n-2 级跨 2 步上来

所以到达第 n 级的方法数 = 到达第 n-1 级的方法数 + 到达第 n-2 级的方法数

第二步：和斐波那契的关系
f(n)=f(n−1)+f(n−2)
爬楼梯本质上就是斐波那契，只是初始条件不同：
f(1) = 1
f(2) = 2

第三步：DP 的思维方式
用一个数组 dp，dp[i] 表示爬到第 i 级的方法数：
从小到大填表
每个状态只依赖前两个状态
最终答案是 dp[n]

这就是自底向上的动态规划。

第四步：DP 的两个核心要素
状态定义：dp[i] 是什么意思？
状态转移方程：dp[i] 怎么从之前的状态推导出来？

复杂度

方法                         时间复杂度                         空间复杂度
朴素递归                     O(2^n)                             O(n)
记忆化搜索                     O(n)                             O(n)
动态规划                       O(n)                             O(n)
空间优化dp                     O(n)                             O(1)
'''

def climb_stairs(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    if n < 2:
        return dp[n]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(climb_stairs(4))

# 空间优化dp
def climb_stairs_2(n):
    f0 = 1
    f1 = 2
    if n == 1:
        return f0
    while n-2:
        f0, f1 = f1, f0+f1
        n -= 1
    return f1

print(climb_stairs_2(4))


'''
第十五题：0/1背包问题

问题描述
有一个容量为 W 的背包，和 n 个物品，每个物品有重量 w[i] 和价值 v[i]。
每个物品只能选一次（选或不选），求背包能装下的最大价值。

示例：
输入：W = 5, w = [1, 2, 3], v = [1, 4, 5]
输出：9
解释：选第2件(重2,价值4)和第3件(重3,价值5)，总重5，总价值9

引导思考
第一步：状态定义
定义 dp[i][j] = 前 i 个物品，背包容量为 j 时的最大价值。

最终答案是什么？
对于第 i 个物品，只有两种选择：

第二步：状态转移
不选：dp[i][j] = dp[i-1][j]
选：前提是 j >= w[i]，此时 dp[i][j] = dp[i-1][j-w[i]] + v[i]

两种选择取最大值：
dp[i][j]=max⁡(dp[i−1][j], dp[i−1][j−w[i]]+v[i])

第三步：初始条件
dp[0][j] = 0：没有物品时价值为0
dp[i][0] = 0：背包容量为0时价值为0

第四步：填表顺序
dp[i][j] 依赖 dp[i-1][...]，所以外层循环遍历物品，内层循环遍历容量，从小到大填表。
画一下这个表格，W=5, w=[1,2,3], v=[1,4,5]
'''

# def Knapsack_problem(w,v,W):
#     MAX = 0
#     dp = [[0] * (W+1) for _ in range(len(w)+1)]
#     for i in range(len(w)+1):
#         if i == 0:
#             continue
#         for j in range(W+1):
#             if j == 0:
#                 continue
#             if j >= w[i-1]:
#                 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
#             else:
#                 dp[i][j] = dp[i-1][j]
#             if dp[i][j] > MAX:
#                 MAX = dp[i][j]
#     return MAX
# 一个小简化：其实不需要追踪 MAX，因为最优答案一定在最后一行最后一列：
def Knapsack_problem(w,v,W):
    dp = [[0] * (W+1) for _ in range(len(w)+1)]
    for i in range(len(w)+1):
        if i == 0:
            continue
        for j in range(W+1):
            if j == 0:
                continue
            if j >= w[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[len(w)][W]
print(Knapsack_problem([1,2,3], [1,4,5], 5))

'''
延伸思考
你现在的解法是 O(n×W)时间，O(n×W)空间。

观察转移方程：
dp[i][j]=max(dp[i−1][j], dp[i−1][j−w[i]]+v[i])

dp[i] 只依赖 dp[i-1]，所以可以把二维数组压缩成一维：

dp = [0] * (W+1)
for i in range(len(w)):
    for j in range(W, w[i]-1, -1):  # ← 注意这里倒序，想想为什么
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])

关键问题：内层循环为什么要倒序？
提示：正序遍历时，dp[j-w[i]] 已经被当前轮次更新过了，会导致同一个物品被选多次。
'''

'''
我们下一题来看一个更经典的二维DP：
最长公共子序列（LCS） —— 字符串DP的基础，Git的diff算法、DNA序列比对都用到了它。
'''

'''
第十六题：最长公共子序列

问题描述
给定两个字符串 s1 和 s2，找出它们的最长公共子序列的长度。
子序列不要求连续，但顺序必须一致。

示例：
输入：s1 = "ABCDE", s2 = "ACE"
输出：3
解释：最长公共子序列是 "ACE"

输入：s1 = "ABCDE", s2 = "BCE"
输出：3
解释：最长公共子序列是 "BCE"

引导思考
第一步：状态定义
定义 dp[i][j] = s1 的前 i 个字符和 s2 的前 j 个字符的最长公共子序列长度。
最终答案是什么？

第二步：状态转移
对于 s1[i] 和 s2[j]，只有两种情况：

相等：s1[i] == s2[j]，这两个字符可以同时纳入公共子序列：

dp[i][j]=dp[i−1][j−1]+1

不等：s1[i] != s2[j]，至少要舍弃其中一个字符，取较大值：

dp[i][j]=max⁡(dp[i−1][j], dp[i][j−1])

第三步：初始条件
dp[0][j] = 0：s1 为空时公共子序列长度为0
dp[i][0] = 0：s2 为空时公共子序列长度为0

第四步：手动填表
'''

def longest_common_subsequence(s1,s2):
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

    for i in range(len(s1)+1):
        if i == 0:
            continue
        for j in range(len(s2)+1):
            if j == 0:
                continue
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s1)][len(s2)]

print(longest_common_subsequence("ABCDE", "ACE"))