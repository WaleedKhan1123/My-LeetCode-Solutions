from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
   
        """
        
        unique = ''
        count_s = Counter(s)
        count_t = Counter(t)
        for char in  count_t:
            
            if char not in s :
                unique+=char
            elif count_t[char] > count_s[char]:
                unique+=char
                
 
            
                
        return unique
    
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.findTheDifference('aa','aaa')
    print(result)
    

    
    
    
    
   