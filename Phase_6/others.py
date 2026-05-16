'''
我们进入 Phase 6：进阶专题，第一个主题是拓扑排序。
现实中非常实用：

课程有先修要求，给定依赖关系，判断能否完成所有课程，如果能，给出一个合法的学习顺序。

这本质上是图的一个经典问题，和你学过的BFS有直接联系。
'''

'''
第二十题：拓扑排序

问题描述
你需要完成 n 门课程，编号为 0 到 n-1。某些课程有先修要求，用 prerequisites 表示，[a, b] 表示学课程 a 之前必须先学 b。
请判断是否能完成所有课程，如果能，输出一个合法的学习顺序。

示例：
输入：n = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]
输出：[0, 1, 2, 3] 或 [0, 2, 1, 3]
解释：先学0，再学1和2，最后学3

输入：n = 2, prerequisites = [[0,1], [1,0]]
输出：[]
解释：0依赖1，1依赖0，形成环，无法完成

引导思考
第一步：建图
把课程看作节点，先修关系看作有向边：
[a, b] → 从 b 指向 a 的边（先学b才能学a）

第二步：入度
每个节点的入度 = 有多少门课程依赖它。
入度为 0 的节点 = 没有先修要求，可以直接学。

第三步：Kahn算法（BFS拓扑排序）
计算所有节点的入度
把所有入度为 0 的节点加入队列
每次从队列取出一个节点，加入结果
把它的所有邻居入度减 1
如果邻居入度变为 0，加入队列
重复直到队列为空

第四步：如何判断有环？
如果最终结果包含所有 n 个节点，说明无环，可以完成。
如果结果少于 n 个节点，说明有环，无法完成。
    想想为什么：有环的节点入度永远不会变为 0，永远进不了队列。

复杂度
时间复杂度          空间复杂度
O(V+E)             O(V+E)
'''

def topological_sort(n, prerequisites):
    result = []

    node_entry_degree = {node: 0 for node in range(n)}
    for node in range(n):
        for prerequisite in prerequisites:
            if node == prerequisite[0]:
                node_entry_degree[node] += 1

    graph = {node: [] for node in range(n)}
    for a, b in prerequisites:
        graph[b].append(a)

    from collections import deque
    queue = deque()
    for node in range(n):
        if node_entry_degree[node] == 0:
            queue.append(node)
    
    while queue:
        pop_node = queue.popleft()
        result.append(pop_node)
        # for prerequisite in prerequisites:
        #     if prerequisite[1] == pop_node:
        #         node_entry_degree[prerequisite[0]] -= 1
        #         if node_entry_degree[prerequisite[0]] == 0:
        #             queue.append(prerequisite[0])
        for neighbor in graph[pop_node]:
            node_entry_degree[neighbor] -= 1
            if node_entry_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return result if len(result) == n else []

n1 = 4
prerequisites1 = [[1,0], [2,0], [3,1], [3,2]]

n2 = 2
prerequisites2 = [[0,1], [1,0]]

print(topological_sort(n1, prerequisites1))
print(topological_sort(n2, prerequisites2))

'''
你现在每次处理节点时都遍历整个 prerequisites，时间复杂度是 O(V×E)O(V \times E)
O(V×E)。
预先建立邻接表，查找邻居就是 O(1)O(1)
O(1)：
graph = {node: [] for node in range(n)}
for a, b in prerequisites:
    graph[b].append(a)  # b → a

然后处理邻居时直接查表：
for neighbor in graph[pop_node]:
    node_entry_degree[neighbor] -= 1
'''