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


'''
延伸思考

你现在用的是小顶堆解决"第 k 大"问题。

反过来思考：

如果要找第 k 小，应该用大顶堆还是小顶堆？

另外，堆还能解决一个更经典的问题：

给定 n 个已排序的数组，把它们合并成一个有序数组

比如：
输入：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]

暴力法是把所有元素合并后排序，O(nlog⁡n)
但用堆可以做到 O(nlog⁡k)

提示：每次从 k 个数组的当前最小值中选出最小的，堆天然支持这个操作。

这个问题叫K路归并，是堆最重要的应用之一
'''

'''
第十题：K路归并

问题描述
给定 k 个已排序的整数数组，将它们合并成一个有序数组。

示例：
输入：[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]

输入：[[1, 3, 5], [2, 4]]
输出：[1, 2, 3, 4, 5]

引导思考

第一步：暴力法是什么？
把所有数组的元素合并到一起，再排序，时间复杂度是多少？

第二步：暴力法浪费了什么？
每个数组内部已经有序了，排序完全忽略了这个信息。

第三步：堆里存什么？
每次你只需要从 k 个数组的当前队头中选出最小的，这正是小顶堆擅长的。

堆里存一个三元组 (值, 数组下标, 元素下标)：
    值：用于堆的比较
    数组下标：知道这个值来自哪个数组
    元素下标：知道这个数组的下一个元素在哪里

第四步：流程
    把每个数组的第一个元素压入堆
    每次弹出堆顶（当前最小值），加入结果
    然后把该元素所在数组的下一个元素压入堆
    重复直到堆为空

复杂度
    设总元素个数为 n，数组个数为 k：
    暴力排序 O(nlog⁡n)
    K路归并 O(nlog⁡k)
    每次堆操作是 O(logk)，共 n 次，所以是 O(nlog⁡k)
'''

import heapq
def k_way_merge(arr):
    k = len(arr)
    heap = []
    result = []

    for i in range(k):
        heapq.heappush(heap, (arr[i][0], i, 1))

    while heap:
        val_tuple = heapq.heappop(heap)
        result.append(val_tuple[0])

        arr_index = val_tuple[1]
        ele_index = val_tuple[2]
        if ele_index < len(arr[arr_index]):
            heapq.heappush(heap, (arr[arr_index][ele_index], arr_index, ele_index+1))
    
    return result


nums3 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
nums4 = [[1, 3, 5], [2, 4]]

print(k_way_merge(nums3))
print(k_way_merge(nums4))