"""
解题思路:
    没什么解题思路，题目比较简单，就是Python的链表写法比较怪

复杂度分析
    时间复杂度：
        O(n+m) 。因为每次循环迭代中，l1 和 l2 只有一个元素会被放进合并链表中， while 循环的次数等于两个链表的总长度。所有其他工作都是常数级别的，所以总的时间复杂度是线性的。
    空间复杂度：
        O(1) 。迭代的过程只会产生几个指针，所以它所需要的空间是常数级别的.
"""


class Solution(object):
    # 自己的笨办法
    def mergeTwoLists(self, l1,l2):
        def add(l1,l2,length):
            for i in range(length,len(l2)):
                l1.append(l2[i])
            return l1
        temp = []
        a = 0
        b = 0
        while(True):
            print(a,b,l1[a],l2[b],temp)

            if l1[a]<l2[b]:
                temp.append(l1[a])
                a = a + 1
                if a == len(l1):
                    temp = add(temp,l2,b)
                    break
            else:
                temp.append(l2[b])
                b = b + 1
                if b == len(l2):
                    temp = add(temp,l1,a)
                    break
        return temp



if __name__ == '__main__':
    S = Solution()
    l1 = [1,2,4]
    l2 = [1,3,4]
    print(S.mergeTwoLists(l1,l2))
    #print(S.isValid_perfect())