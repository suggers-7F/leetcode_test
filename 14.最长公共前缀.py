class Solution(object):
    #自己的无敌笨办法
    def longestCommonPrefix(self, strs):
        k = 0
        if len(strs) == 0:
            return ""
        min = len(strs[0])
        for i in range(1,len(strs)):
            if min > len(strs[i]):
                min = len(strs[i])
        #print(min)
        for j in range(0,min):
            for i in range(0,len(strs)-1):
                #print(i,j)
                #print(strs[i][j],strs[i+1][j])
                if strs[i][j]==strs[i+1][j]:
                    pass
                else:
                    if k == 0:
                        return ""
                    else:
                        return strs[0][0:k]

            k = k + 1
            #print(k)
        if k == 0:
            return ""
        else:
            return strs[0][0:k]

    #同样的解决逻辑，别人优秀的写法
    #知识点：
    #     if not dict  就可以判断一个数组是不是空的了，根本不需要通过数组长度来判断
    #     同理 not x 可以判断一个数组，一个字符串，一个字典，一个元祖是不是空
    def longestCommonPrefix_perfect(self, strs: [str]) -> str:
        if not strs: return ""
        mi = len(strs[0])
        for s in strs[1:]:
            mi = min(mi, len(s))
        for i in range(mi):
            for j in range(len(strs) - 1):
                if strs[j][i] != strs[j + 1][i]:
                    return strs[j][:i]
            return strs[0][:i + 1] if mi else ""



if __name__ == '__main__':
    S = Solution()
    strs = ["flower","flow","floght"]
    strs1 = ["aa"]
    print(S.longestCommonPrefix(strs1))
