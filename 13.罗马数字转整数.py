class Solution(object):

    def romanToInt(self, s):
        dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        sum = 0
        for i in range(len(s)):
            try:
                if dict[s[i]] >= dict[s[i + 1]]:
                    sum = sum + dict[s[i]]
                else:
                    sum = sum - dict[s[i]]
            except:
                sum = sum + dict[s[i]]
        return sum

    def romanToInt_perfect(self, s: str) -> int:
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500,
             'CM': 800, 'M': 1000}
        print(s[6:8])
        print(d.get(s[5:7]),d["V"])
        #print(s[3])
        return sum(d.get(s[max(i - 1, 0):i + 1], d[n]) for i, n in enumerate(s))


if __name__ == '__main__':
    S = Solution()
    x = "MCMXCIV"
    print(S.romanToInt(x))
    print(S.romanToInt_perfect(x))
