from collections import Counter
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_s = Counter(s)
        
        substring = ""
        
        for char in count_s:
            substring+=char
            
        substring2 = ""
        while len(substring2)<len(s):
            
            substring2+=substring
        if substring2 == s:
            return True
        return False
        
        
if __name__ == "__main__":
    sol = Solution()
    result = sol.repeatedSubstringPattern("abcabcabcabc")
    print(result)
            