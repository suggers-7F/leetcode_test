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
    python 常见字符串去除空格的方法总结
    1：strip()方法，去除字符串开头或者结尾的空格
        >>> a = " a b c "
        >>> a.strip()
            'a b c'

    2：lstrip()方法，去除字符串开头的空格
        >>> a = " a b c "
        >>> a.lstrip()
            'a b c '

    3：rstrip()方法，去除字符串结尾的空格
        >>> a = " a b c "
        >>> a.rstrip()
            ' a b c'

    4：replace()方法，可以去除全部空格
        # replace主要用于字符串的替换replace(old, new, count)
        >>> a = " a b c "
        >>> a.replace(" ", "")
            'abc'

    5: join()方法+split()方法，可以去除全部空格
        # join为字符字符串合成传入一个字符串列表，split用于字符串分割可以按规则进行分割
        >>> a = " a b c "
        >>> b = a.split()  # 字符串按空格分割成列表
        >>> b ['a', 'b', 'c']
        >>> c = "".join(b) # 使用一个空字符串合成列表内容生成新的字符串
        >>> c 'abc'

        # 快捷用法
        >>> a = " a b c "
        >>> "".join(a.split())
            'abc'
    6：split()split(' ')的区别
        split()的时候，多个空格当成一个空格；split(' ')的时候，多个空格也要分割，会分割出来空。

"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #   一个一个对比，暴力遍历
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        cont = 0
        s = s.rstrip()
        for i in range(1,len(s)+1):
            if s[-i] == " " :
                break
            else:
                cont += 1
        return cont



    # 别人优秀的逻辑和写法
    # 逻辑点：
    #     各种字符串取空格方法
    # 知识点：
    def lengthOfLastWord_perfect(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])




if __name__ == '__main__':
    S = Solution()
    s = " a  a "
    # s = s.rstrip()
    # print(s)
    # print(s.split())
    # print(s.split(" "))
    # print(s.split()[-1])
    # print(s.split(" ")[-1])
    print(S.lengthOfLastWord(s))
    print(S.lengthOfLastWord_perfect(s))