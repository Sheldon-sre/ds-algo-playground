# 队列与堆

# 堆能解决一类非常实用的问题：

#    在一个动态变化的数据集里，随时找到最大值或最小值

# 这在现实中无处不在，比如任务调度、Top K 问题、实时排行榜


'''
第九题：堆的经典应用

问题描述
给定一个整数数组 nums 和一个整数 k，找出数组中第 k 大的元素。

示例：
输入：nums = [3, 1, 5, 2, 4], k = 2
输出：4
解释：排序后为 [5, 4, 3, 2, 1]，第2大是4

输入：nums = [3, 1, 5, 2, 4], k = 1
输出：5

引导思考
第一步：最简单的方法是什么？
    直接排序，时间复杂度是多少？

第二步：排序是否浪费了？
    你只需要第 k 大，但排序把所有元素的顺序都确定了，做了很多不必要的工作。

第三步：小顶堆的思路
维护一个大小为 k 的小顶堆（堆顶是堆里最小的元素）：

    遍历数组，把元素加入堆
    当堆的大小超过 k 时，弹出堆顶（最小值）
    遍历结束后，堆顶就是答案

思考一下：为什么堆顶就是第 k 大？
    堆里始终保留的是什么？

第四步：Python 的堆
Python 的 heapq 模块默认是小顶堆：
    import heapq
    heap = []
    heapq.heappush(heap, val)   # 插入
    heapq.heappop(heap)          # 弹出最小值
    heap[0]                      # 查看堆顶

复杂度对比
    排序 O(nlog⁡n)
    小顶堆 O(nlog⁡k)
    当 k 远小于 n 时，堆的优势非常明显。
'''
import heapq
def K_biggest(arr, k):
    heap = []
    for val in arr:
        heapq.heappush(heap, val)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]

nums1 = [3, 1, 5, 2, 4]
k1 = 2

nums2 = [3, 1, 5, 2, 4]
k2 = 1

print(K_biggest(nums1, k1))

print(K_biggest(nums2, k2))