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