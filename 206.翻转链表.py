"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        while(head.next):

         = ListNode()

        pass



class Solution:
    # 比较笨的办法，通过暴力循环去寻找对应的解法，缺点就是消耗时间太长，时间复杂度为0(n²) ，空间复杂度O（1）
    def twoSum(self,nums,target):
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
    # 复制一个新的数组进行排序，然后通过首尾相加来和目标值对比，通过空间换时间的方式来解决速度问题
    # 这里先将数组排序好时间复杂度O(nlogn),空间复杂度O(n),再利用双指针法遍历一遍时间复杂度O(n),空间复杂度O(1)得到结果。
    # 为了保存下标信息另开了一个数组
    # 所以总共是时间复杂度O（nlogn），空间复杂度O（n）
    def twoSum_1(self, nums, target):
        # 数组的浅拷贝
        temp = nums.copy()
        # 数组排序
        temp.sort()
        i = 0  # 定义首位指针
        j = len(nums) - 1 # 定义末尾指针
        # 如果首位指针大于等于末尾指正跳出循环（这道题给定了一定的初始条件，就是必有解，所以基本不会通过while的条件语句跳出循环）
        while i < j:
            # 首位和末尾相加大于目标值，则末尾指针向前移动
            if (temp[i] + temp[j]) > target:
                j = j - 1
            # 首位和末尾相加小于目标值，则首位指针向后移动
            elif (temp[i] + temp[j]) < target:
                i = i + 1
            # 如果相等等于找到目标值，跳出循环
            else:
                break
        # 调用数组的index方法找出具体的位置（index只能找到第一个出现的位置）
        p = nums.index(temp[i])
        # 如果答案是不同位置相同的值，需要取出一下，否则直接执行下一个index，还是取到第一个坐标，例如target=6  nums=[3,3]
        nums.pop(p)
        k = nums.index(temp[j])
        # 因为pop过，所以k要去+1  判断k >=p 其实可以省略。因为题目说必有解，所以最特殊的情况也是k=p
        if k >= p:
            k = k + 1
        return [p, k]


    # hash法 利用undered_map数组构造映射，遍历nums[i]时，看target - nums[i]是否存在hash表中即可
    # 时间复杂度O（n），空间复杂度O（n）
    def twoSum_2(self, nums, target):
        hashset = {}
        for i in range(len(nums)):
            if hashset.get(target - nums[i]) is not None:
                return [hashset.get(target - nums[i]), i]
            hashset[nums[i]] = i





if __name__ == '__main__':
    S = Solution()
    nums = [3,3,11,15]
    target = 6
    print(S.twoSum(nums,target))

