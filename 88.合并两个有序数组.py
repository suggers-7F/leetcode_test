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
    def merge(self, nums1, m , nums2, n):
        i = m
        j = 0
        while(n!=j):
            nums1[i] = nums2[j]
            i +=1
            j +=1
        for i in range(0,len(nums1)):
            for j in range(i+1,len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i],nums1[j] = nums1[j],nums1[i]
        return nums1


    # 别人优秀的逻辑和写法
    # 逻辑点：
    #
    # 知识点：
    #   sort 与 sorted 区别：
    #   sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    #   list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
    #   而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    def merge_perfect(self, nums1, m, nums2, n):
        return sorted(nums1[0:m] + nums2[0:n])



if __name__ == '__main__':
    S = Solution()
    nums1 = [1, 2, 3,0,0,0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3


    print(S.merge(nums1,m,nums2,n))
    print(S.merge_perfect(nums1,m,nums2,n))
    #print(S.lengthOfLastWord_perfect(s))

