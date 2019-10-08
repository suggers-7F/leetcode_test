"""
解题思路:
    第一种方法：
        暴力匹配方法，一个一个去匹配循环。
    第二种方法：
        动态规划法
    第三种方法：
        分治法

复杂度分析
    时间复杂度：

    空间复杂度：


知识点：

"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #   一个一个对比，暴力遍历
    def maxSubArray(self, nums) -> int:
        if not nums:
            return 0
        data = {
            #"index":0,
            #"step":0,
            "value":nums[0]
        }
        for step in range(len(nums)):
            for i in range(len(nums)-step):
                sum = 0
                temp_step = step
                while(temp_step>=0):
                    sum += nums[i+temp_step]
                    temp_step -= 1
                if sum > data["value"]:
                    # data["index"] = i
                    # data["step"] = step
                    data["value"] = sum
        return data["value"]


    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：
    #
    def maxSubArray_perfect(self, nums)-> int:
        max_data = nums[0]
        sum_data = 0
        for n in nums:
            if sum_data>0:
                sum_data += n
            else:
                sum_data = n
            max_data = max(max_data,sum_data)
        return max_data



if __name__ == '__main__':
    S = Solution()
    nums = [1]
    #print(S.maxSubArray(nums))
    print(S.maxSubArray_perfect(nums))