from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == len(t):
            count_s = Counter(s)
            count_t = Counter(t)
            if count_s == count_t:
                return True
            else:
                return False
                 
        else:
            return False
            
if __name__ == "__main__":
    sol = Solution()
    result = sol.isAnagram('anagram','nagaram')
    print(result)
    
    