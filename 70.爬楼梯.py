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
    def climbStairs(self, n: int) -> int:
        arr = {1:1,2:2}
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2]
        return arr[n]
    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：

    def cli(self,n):
        if n < 2:
            return n
        else:
            a = 1
            b = 2
            i = 3
            while i < n:
                a = b
                b = a + b
                i = i +1
                #print(b)
        return b



if __name__ == '__main__':
    S = Solution()
    x = 3

    #print(S.climbStairs(x))
    print(S.cli(x))
    #print(S.lengthOfLastWord_perfect(s))

