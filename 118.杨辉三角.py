"""
解题思路:
    第一种方法：

复杂度分析
    时间复杂度：

    空间复杂度：


知识点：

"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #
    def generate(self, numRows: int):
        sum = []
        def temp(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1,1]
            else:
                data = [1]
                for i in range(1,n-1):
                    data.append(sum[n-2][i-1]+sum[n-2][i])
                data.append(1)
                return data

        for i in range(1,numRows+1):
            sum.append(temp(i))
        return sum



    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：



if __name__ == '__main__':
    S = Solution()
    n = 5


    print(S.generate(n))
    #print(S.merge_perfect(nums1,m,nums2,n))
    #print(S.lengthOfLastWord_perfect(s))

