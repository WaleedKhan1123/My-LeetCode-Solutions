from collections import Counter
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring = ""
        if(len(s)<=1):
            return False
        substring= s[:len(s)//2]
        print(substring)    
        substring2 = ""
        for i in range(len(substring)):
            if substring2 == s:
                return True
            while True:
                 substring2+=substring[i]
                 if substring2==s:
                     break
        return False
        
        
if __name__ == "__main__":
    sol = Solution()
    result = sol.repeatedSubstringPattern("abaababaab")
    print(result)
            