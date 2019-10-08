class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            status = -1
            x = x * -1
        else:
            status = 1
        data = 0
        while (True):
            temp = x % 10
            data = 10 * data + temp
            x = int(x / 10)
            if x == 0:
                break
            print(data)
            print(x)
        finall_data = status * data
        if finall_data > 10000000:
            return 0
        else:
            return finall_data

if __name__ == '__main__':
    S = Solution()
    print(S.reverse(-12344))
    print(-111%10)