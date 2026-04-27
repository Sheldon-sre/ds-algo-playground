# 栈
# 栈看起来简单，但它背后能解决一类非常经典的问题

'''
第七题：栈的经典应用

问题描述
给定一个只包含 ( ) { } [ ] 的字符串，判断括号是否合法匹配

示例：
输入：s = "({[]})"
输出：True

输入：s = "({[}])"
输出：False

输入：s = "((("
输出：False

引导思考
第一步：人类是怎么判断的？
你看到 ({[]}) 时，大脑是怎么处理的？
注意你的思维过程：遇到左括号时你会"记住"它，遇到右括号时你会去匹配最近的那个左括号。

第二步："最近的"意味着什么？
最近压入的，最先被匹配。这是什么数据结构的特性？
后进先出 → Last In First Out → 栈

第三步：具体逻辑
遍历字符串，遇到：
左括号 ( { [ → 压入栈
右括号 ) } ] → 取出栈顶元素，检查是否匹配

第四步：遍历结束后
字符串遍历完了，但栈不为空，说明什么？
'''
def stack(s):
    hash_table = {"(": ")", "{": "}", "[":"]"}
    arr = []
    for i in s:
        if i in ["(", "{", "["]:
            arr.append(i)
        if i in [")","}","]"]:
            if len(arr) == 0:
                return False
            if hash_table[arr.pop()] != i:
                return False
    if len(arr) != 0:
        return False
    return True

s1 = "({[]})"
s2 = "({[}])"
s3 = "((("
print(stack(s1))
print(stack(s2))
print(stack(s3))


'''
栈的本质是维护**"最近未处理"**的状态，这个思想能解决一类很重要的问题：
    给定一个数组，对于每个元素，找到它右边第一个比它大的元素。

比如：
输入：[2, 1, 4, 3, 6]
输出：[4, 4, 6, 6, -1]
解释：2右边第一个比它大的是4，1右边第一个比它大的是4...

暴力法是 O(n^2) 但用栈可以做到 O(n)，这个技巧叫单调栈，是栈最强大的应用之一。
'''

'''
第八题：单调栈

问题描述
给定一个整数数组 nums，对于每个元素，找到它右边第一个比它大的元素，如果不存在则返回 -1

示例：
输入：nums = [2, 1, 4, 3, 6]
输出：[4, 4, 6, 6, -1]

输入：nums = [5, 4, 3, 2, 1]
输出：[-1, -1, -1, -1, -1]

引导思考
第一步：暴力解法是什么？
    对每个元素，往右扫描找第一个更大的，时间复杂度是多少？

第二步：暴力法浪费了什么？
    考虑数组 [2, 1, 4, ...]，当你扫描到 4 时：

    4 是 2 右边第一个更大的
    4 也是 1 右边第一个更大的 

    暴力法对 2 和 1 分别扫描了一遍，但其实 4 可以同时解决它们两个

第三步：栈里存什么？
    维护一个栈，存放还没找到答案的元素的下标。
    遍历到一个新元素 nums[i] 时，检查栈顶元素：
        如果 nums[i] 大于栈顶元素对应的值 → 说明什么？
        然后继续检查新的栈顶，直到什么时候停止？
        最后把 nums[i] 的下标压入栈
第四步：栈的单调性
    按照上面的逻辑，栈里的元素从栈底到栈顶，对应的值是递增还是递减的？
    这就是"单调栈"名字的由来。
复杂度
    每个元素最多入栈一次、出栈一次，所以总时间复杂度是 O(n)，而不是O(n^2)
'''

def normal_method(arr):
    result = []
    
    for i in range(len(arr)):
        biggest = True
        for j in range(i+1, len(arr)):
            if arr[j] > arr[i]:
                result.append(arr[j])
                biggest = False
                break
        if biggest:
            result.append(-1)
    return result


nums1 = [2, 1, 4, 3, 6]
nums2 = [5, 4, 3, 2, 1]

print(normal_method(nums1))
print(normal_method(nums2))


def monotonic_stack(arr):
    stack = []
    result = [None] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    while stack:
        index = stack.pop()
        result[index] = -1

    return result

nums1 = [2, 1, 4, 3, 6]
nums2 = [5, 4, 3, 2, 1]

print(monotonic_stack(nums1))
print(monotonic_stack(nums2))