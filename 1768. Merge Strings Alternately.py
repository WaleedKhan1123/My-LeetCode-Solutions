class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = ''
        
        for a,b in zip(word1,word2):
            
            merge += a
            merge += b

        if len(word1) >len(word2): 
           c = len(word1) - len(word2)
           remaining = word1[-c:]
           merge += remaining
        elif len(word2) >len(word1):
            c = len(word2) - len(word1)
            remaining = word2[-c:]
            merge += remaining

        return merge 
    
    
if __name__ == "__main__":
    sol = Solution()
    
    merge = sol.mergeAlternately("Waleed","khan")
    
    print(merge)
    
    
    
