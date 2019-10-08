"""
解题思路:
    第一种方法：
        暴力匹配方法，一个一个去匹配循环。
    第二种方法：
        KMP方法，再第一种方法通过利用匹配过程中已经得到的信息来做排除掉不必要的循环，直接跳到需要继续匹配的地方。
        涉及的概念有前缀，后缀，相同的前缀后缀，最长的相同的前缀后缀。
        核心思想就是通过最长的相同的前缀后缀来进行直接跳到继续匹配的地方的方法。
    第三种方法：
        Python有自带的函数，find函数就可以直接实现。

复杂度分析
    时间复杂度：
        为O(m+n)（其中m为字符段长度，n为匹配模式的长度）
    空间复杂度：
        为O(m)
"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #   两个字符串，取被检测的每一个字母去匹配第一个字母。比较暴力的遍历。
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        #while i < len(haystack):
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i]==needle[j]:
                    if j == len(needle)-1:
                        return i-len(needle)+1
                    if i + 1 == len(haystack):
                        return -1
                    i = i + 1
                else:
                    break
            i = i +1
        return -1

    # 别人优秀的逻辑和写法
    # 逻辑点：
    #     根本不需要一个一个遍历，只需要把需要遍历的字符串长度的内容进行遍历。虽然也是暴力遍历，但是明显比自己方法要好
    # 知识点：
    #
    def strStr_perfect(self, haystack: str, needle: str)-> int:
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        for i in range(len(haystack)):
            j = i + len(needle)
            if haystack[i:j] == needle:
                return i
        return -1



if __name__ == '__main__':
    S = Solution()
    haystack = "mississippi"
    needle = "issip"

    print(S.strStr(haystack,needle))
    print(haystack.find(needle))
    print(S.strStr_perfect(haystack,needle))