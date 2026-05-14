'''
图论，这是算法最贴近现实的部分。
地图导航、社交网络、任务依赖关系，本质上都是图的问题。
我们从图最基础的两种遍历方式开始：
BFS（广度优先搜索） 和 DFS（深度优先搜索）
'''

'''
问题描述
给定一个有 n 个节点的无向图，用邻接表表示，从节点 0 出发，分别用 BFS 和 DFS 输出所有可以访问到的节点。

示例：
输入：
n = 6
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
从节点 0 出发

BFS输出：[0, 1, 2, 3, 4, 5]
DFS输出：[0, 1, 3, 4, 2, 5]

引导思考
BFS：一圈一圈向外扩散
想象把一块石头扔进水里，涟漪一圈圈向外扩散：

先访问距离为1的节点
再访问距离为2的节点
以此类推

需要一个队列来维护待访问的节点，Python 用 collections.deque：
from collections import deque
queue = deque()
queue.append(node)   # 入队
queue.popleft()      # 出队

DFS：一条路走到黑
沿着一条路一直走，走不下去了再回头换另一条：

可以用递归实现
也可以用栈模拟递归

两者都需要注意：
图可能有环，比如 0→1→0→1... 会无限循环。需要一个 visited 集合记录已访问的节点。

复杂度
设节点数为 V，边数为 E：
方法      时间复杂度         空间复杂度
BFS       O(V+E)            O(V + E)
DFS       O(V+E)            O(V + E)
'''

def BFS_queue(graph):
    from collections import deque
    queue = deque()

    visited = set()
    visited.add(0)

    result = []

    queue.append(0)
    
    while queue:
        visited_node = queue.popleft()
        result.append(visited_node)
        for node in graph[visited_node]:
            if node in visited:
                continue
            queue.append(node)
            # 改为入队前标记
            visited.add(node)
    return result


def DFS_recursion():
    pass

def DFS_stack(graph):
    stack = [0]
    visited = set()
    visited.add(0)

    result = []

    while stack:
        visited_node = stack.pop()
        result.append(visited_node)
        # for node in graph[visited_node][::-1]:
        for node in graph[visited_node]:
            if node in visited:
                continue
            stack.append(node)
            # 改为入队时标记
            visited.add(node)

    return result

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

print(BFS_queue(graph))
print(DFS_stack(graph))

'''
优化1：visited 用 set 代替列表
你现在用的是列表，if visited_node in visited 是 O(n)的查找。
改成 set 之后查找是 O(1)：

优化2：BFS 应该在入队时标记visited
你现在是出队时才检查，这意味着同一个节点可能被多次加入队列，浪费空间。
更好的做法是入队时就标记：

queue.append(0)
visited.add(0)  # 入队时就标记
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)  # 保证每个节点只入队一次

DFS 的栈实现也有同样的问题，思考一下怎么改。
'''