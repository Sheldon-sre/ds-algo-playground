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

'''
第十八题：最短路径

问题描述
给定一个无权无向图，找出从节点 0 到所有其他节点的最短路径长度（以边数计算）。

示例：
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

输出：{0: 0, 1: 1, 2: 1, 3: 2, 4: 2, 5: 2}
解释：0到1需要1步，0到3需要2步...

引导思考
第一步：为什么BFS能找最短路？
BFS按层扩散，第一次访问到某个节点时，走的一定是最少的步数。
因为如果存在更短的路径，BFS早就通过那条路径先访问到了。

第二步：怎么记录距离？
在上一题的BFS基础上，用一个字典 dist 记录每个节点的距离：

起点距离为 0
每次从队列取出节点时，它的邻居距离 = 当前节点距离 + 1

第三步：什么时候距离确定了？
第一次访问到某个节点时，距离就确定了，不需要更新。
'''

def BFS_shortest_path(graph):

    from collections import deque
    queue = deque()
    queue.append(0)

    result = {0:0}
    visited = set()
    visited.add(0)

    while queue:
        visited_node = queue.popleft()
        for node in graph[visited_node]:
            if node in visited:
                continue
            queue.append(node)
            visited.add(node)
            result[node] = result[visited_node] + 1
    return result

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}
print(BFS_shortest_path(graph))

'''
延伸思考
这题是无权图的最短路，每条边的权重都是1。
但现实中的图往往有权重，比如地图导航中每条路的距离不同。这时BFS就不够用了，需要：

Dijkstra算法 —— 有权图的最短路

它的核心思想和BFS很像，但用小顶堆代替普通队列，每次取出当前距离最小的节点。
'''

'''
第十九题：Dijkstra算法

问题描述
给定一个有权有向图，找出从节点 0 到所有其他节点的最短路径长度。

示例：
graph = {
    0: [(1, 4), (2, 1)],   # (邻居, 边权重)
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

输出：{0: 0, 1: 3, 2: 1, 3: 4}
解释：
0→1 直接走：4
0→2→1 走：1+2=3 ✓ 更短
0→2→1→3 走：1+2+1=4 ✓

引导思考
第一步：BFS为什么不够用了？
无权图中每条边权重相同，BFS按层扩散天然保证最短。
但有权图中，边权不同，层数少不代表距离短：
0→1 直接1步，但权重4
0→2→1 两步，但权重只有3

第二步：Dijkstra的核心思想
用小顶堆代替普通队列，每次取出当前距离最小的节点：
    heap = [(距离, 节点)]
贪心策略：当一个节点从堆中被取出时，它的最短距离已经确定了。
    因为堆里其他路径的距离都比它大，不可能再找到更短的路。

第三步：松弛操作
对于取出的节点 u，遍历它的所有邻居 v：
    如果 dist[u]+w(u,v)<dist[v]，则更新 dist[v]
这叫松弛，是最短路算法的核心操作。

第四步：初始化
dist = {node: float('inf') for node in graph}
dist[0] = 0
heap = [(0, 0)]  # (距离, 节点)

第五步：已确定的节点跳过
同一个节点可能多次进入堆，取出时检查：
if current_dist > dist[node]:
    continue  # 已经找到更短路径，跳过
    
复杂度
设节点数为 V，边数为 E：
方法                    时间复杂度
朴素Dijkstra            O(V^2)
堆优化Dijkstra          O((V+E)log⁡V)
'''
import heapq
def heap_optimized_dijkstra(graph):
    dist = {node: float('inf') for node in graph}
    dist[0] = 0
    heap = [] # (距离, 节点) # 在小顶堆中会首先以元素第一个元素为基准排序
    heapq.heappush(heap,(0, 0))

    while heap:
        dist_node = heapq.heappop(heap)
        current_dist = dist_node[0]
        if current_dist > dist[dist_node[1]]:
            continue
        for node_weight in graph[dist_node[1]]:
            if dist[dist_node[1]] + node_weight[1] < dist[node_weight[0]]:
                dist[node_weight[0]] = dist[dist_node[1]] + node_weight[1]
                heapq.heappush(heap, (dist[node_weight[0]], node_weight[0])) # 移到if内部
            # 一个小优化：松弛成功才需要入堆，否则会把无意义的节点压入堆：
            # heapq.heappush(heap, (dist[node_weight[0]], node_weight[0]))
    return dist
# 有权有向图
graph = {
    0: [(1, 4), (2, 1)],   # (邻居, 边权重)
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

print(heap_optimized_dijkstra(graph))