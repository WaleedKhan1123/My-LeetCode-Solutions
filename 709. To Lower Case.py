class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        lowerCase = s.lower()
        return lowerCase
if __name__ == "__main__":
    sol = Solution()
    s = "Hello"
    result = sol.toLowerCase(s)
    print(result)        