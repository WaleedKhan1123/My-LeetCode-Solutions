from collections import Counter
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
        
          # Try for every possible substring length
        for length in range(1, len(s) // 2 + 1):
            if len(s) % length == 0:  # Check if length is a divisor of s
                substring = s[:length]  # Get the substring
                if substring * (len(s) // length) == s:  # Repeat the substring and compare
                    return True
        
        return False
if __name__ == "__main__":
    sol = Solution()
    result = sol.repeatedSubstringPattern("abaababaab")
    print(result)
            