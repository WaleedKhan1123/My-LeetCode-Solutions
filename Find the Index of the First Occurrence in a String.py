class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        memory = ''
        if len(needle)>len(haystack):
            return -1
        
        for i in range(len(haystack)):  
            if haystack[i] == needle[0]:
               count = i
               for b in range(len(needle)): 
                  if haystack[count] == needle[b]:
                      memory+= haystack[count]
                  
                  else:
                      memory= ''
                      break
                                
                  count+=1
            if memory == needle:
                return i
              
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    
    result = sol.strStr("sadbutsad","sad")
    
    print(result)
    
            