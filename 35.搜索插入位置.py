"""
解题思路:
    第一种方法：
        暴力匹配方法，一个一个去匹配循环。
    第二种方法：
        通过挑选出比target小的所有内容，然后计算长度就好
    第三种方法：
        二分法等

复杂度分析
    时间复杂度：
        不一样的写法时间复杂度不一样
    空间复杂度：
        为O(n)

知识点：
    python // 与 / 的含义
    " / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法(截位而不是四舍五入)。
    example:
            3/2 = 1.5  2/2 = 1.0
            3//2 = 1   2//2 = 1
"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #   一个一个对比，暴力遍历
    def searchInsert(self, nums, target) -> int:
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            if nums[i]<target:
                continue
            if nums[i]>target:
                return i


    # 别人优秀的逻辑和写法
    # 逻辑点：
    #     通过挑选出比target小的所有内容，然后计算长度就好。逻辑感人，写法优美
    # 知识点：
    #
    def searchInsert_perfect(self, haystack: str, needle: str)-> int:
        return len([arg for arg in nums if arg < target])


if __name__ == '__main__':
    S = Solution()
    nums = [1,3,5,6]

    target = 7

    print(S.searchInsert(nums,target))
    print(S.searchInsert_perfect(nums,target))