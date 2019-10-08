"""
判断是不是回文数，主要注意几个点：
1、小于0的不是回文数
2、注意溢出情况
3、最后一位是0也不是回文数
解题思路:
1、转换成字符串
2、不转换的时候通过反转整数然后对比反转后的数字是否与前面相等
3、再2的基础上只需要判断一半的数字
复杂度分析
    时间复杂度：
        O(\log_{10}(n))O(log10(n))，
        对于每次迭代，我们会将输入除以10，因此时间复杂度为 O(\log_{10}(n))O(log10(n))。
    空间复杂度：
        O(1)O(1)。
"""


class Solution(object):
    # 自己的笨办法
    def isPalindrome(self, x):
        result = x
        if x < 0 or (x%10==0 and x!=0):
            return False
        data = 0
        while (True):
            temp = x % 10
            data = 10 * data + temp
            x = int(x / 10)
            if x == 0:
                break
        if data < -2**31 or data > 2**31 -1:
            return False
        else:
            if result==data:

                return True
            else:
                return False
    # 网上优秀解答
    def isPalindrome_perfect(self, x):
        if x < 0 or (x%10==0 and x!=0):
            return False
        data = 0
        while (x>data):
            data = 10 * data + x % 10
            print(data)
            x = int(x / 10)
            print(x)
        print(data)
        return x == data or x == int(data / 10);

if __name__ == '__main__':
    S = Solution()
    x = 12221
    print(S.isPalindrome(x))
    print(S.isPalindrome_perfect(x))
