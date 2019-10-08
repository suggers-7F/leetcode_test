"""
解题思路:
    第一种方法：
        各种递归

复杂度分析
    时间复杂度：

    空间复杂度：


知识点：
    f"{}"
    字符串合并，原来一直用str转换后再去相加。用这个不需要转换就可以直接合成
"""


class Solution(object):
    # 自己的笨办法
    # 逻辑点：
    #   一个一个对比，暴力遍历
    # 用来计算一个字符串最开始的数字有几个是重复的，返回数量和内容
    def countnum(self,string):
        count = 1
        for l in range(len(string)):
            if l + 1 == len(string):
                return  count ,f"{count}{string[0]}"
                #return count,str(count) + string[0]
            if string[l] == string[l + 1]:
                count += 1
            else:
                return count,f"{count}{string[0]}"
    # 计算一个数字的报数
    def baoshu(self,string):
        string2 = ""
        while (string):
            tempcount, tempstring = self.countnum(string)
            string2 = f"{string2}{tempstring}"
            #string2 += tempstring
            string = string[tempcount:]
        return string2
    # 递归计算。
    def countAndSay(self, n):
        s = "1"
        while(n-1>0):
            s = self.baoshu(s)
            n -=1
        return s


    # 别人优秀的逻辑和写法
    # 逻辑点：
    #     通过挑选出比target小的所有内容，然后计算长度就好。逻辑感人，写法优美
    # 知识点：



if __name__ == '__main__':
    S = Solution()
    n = 10
    print(S.countAndSay(n))
    #print(S.searchInsert_perfect(nums,target))