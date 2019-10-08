"""
解题思路:
    第一种方法：
        暴力匹配方法，一个一个去匹配循环。
    第二种方法：
        各种字符串方法

复杂度分析
    时间复杂度：

    空间复杂度：


知识点：

"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #
    def plusOne(self, digits):
        s = map(str,digits)
        s1 = ""
        for i in s:
            s1 = f"{s1}{i}"
        num = int(s1)+1
        s2 = str(num)
        list_a = list(map(int,s2))
        return list_a



    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：
    # def lengthOfLastWord_perfect(self, s: str) -> int:
    #     return len(s.rstrip().split(" ")[-1])




if __name__ == '__main__':
    S = Solution()
    digits = [1,2,3,4]

    print(S.plusOne(digits))
    #print(S.lengthOfLastWord_perfect(s))