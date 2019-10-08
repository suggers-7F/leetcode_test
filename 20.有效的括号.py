"""
解题思路:
    通过栈的思想去处理这道题，往栈里添加元素，当出现目标元素的时候就和前面一个元素去比较，如果符合
    要求，就删除。通过循环。最终判断栈中是否还存在元素，如果存在说明无效，否则符合题目要求。

复杂度分析
    时间复杂度：
        O(n)O(n)，因为我们一次只遍历给定的字符串中的一个字符并在栈上进行 O(1)O(1) 的推入和弹出操作。
    空间复杂度：
        O(n)O(n)，当我们将所有的开括号都推到栈上时以及在最糟糕的情况下，我们最终要把所有括号推到栈上。
"""


class Solution(object):
    # 自己的笨办法
    def isValid(self, s):
        dict = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        temp = []
        for i in s:
            temp.append(i)
            #print(temp)
            if i in dict:
                if len(temp)<2:
                    return False
                #print(temp[-2])
                #print(dict[i])
                if dict[i]== temp[-2]:
                    temp.pop()
                    #print(temp)
                    temp.pop()
                    #print(temp)
                else:
                    return False
        if len(temp)>0:
            return False
        else:
            return True

    # 同样的解决逻辑，别人优秀的写法
    # 逻辑点：
    #     可以先删除，在判断，而不是像自己一样，先添加再去连续删除两个。别人的方法速度更快
    # 知识点：
    #     if stack  就可以判断是不是空的了，根本不需要通过数组长度来判断
    def isValid_perfect(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack



if __name__ == '__main__':
    S = Solution()
    x = "[])"
    print(S.isValid(x))
    print(S.isValid_perfect(x))