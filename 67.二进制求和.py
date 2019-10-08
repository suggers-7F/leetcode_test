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
    def addBinary(self, a: str, b: str) -> str:

        if len(a)>len(b):
            max_len = len(a)
            for i in range(len(a)-len(b)):
                b = f"{0}{b}"
        else:
            max_len = len(b)
            for i in range(len(b)-len(a)):
                a = f"{0}{a}"
        temp = '0'
        finall_str = ""
        print(a,b)
        for i in range(1,max_len+1):

            print(a[-i],b[-i])


            if a[-i]=='0' and b[-i]=='0':
                finall_str = f'{temp}{finall_str}'
                temp = '0'
            elif a[-i]=='1' and b[-i]=='1':
                finall_str = f'{temp}{finall_str}'
                temp ='1'
            else:
                if temp == '0':
                    finall_str = f'{1}{finall_str}'
                    temp = '0'
                else:
                    finall_str = f'{0}{finall_str}'
                    temp = '1'
            print(finall_str,temp)
        if temp == '1':
            finall_str = f"{1}{finall_str}"
        return finall_str
    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：
    # def lengthOfLastWord_perfect(self, s: str) -> int:
    #     return len(s.rstrip().split(" ")[-1])




if __name__ == '__main__':
    S = Solution()
    a = "1"
    b = "111"

    print(S.addBinary(a,b))
    #print(S.lengthOfLastWord_perfect(s))

