class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                num -= roman_to_int[s[i]]
            else:
                num += roman_to_int[s[i]]

        return num
if __name__ == "__main__":
    sol = Solution()
    s = "MMMCDXC"
    result = sol.romanToInt(s)
    print(result)