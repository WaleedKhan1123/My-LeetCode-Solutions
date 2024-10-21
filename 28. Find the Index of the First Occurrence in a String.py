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
        
        elif len(needle)==len(haystack) and needle==haystack:
             return 0
         
        for i in range(len(haystack)):  
            if haystack[i] == needle[0] and i+1<len(haystack) :
               count = i
               for b in range(len(needle)): 
                  if haystack[count] == needle[b]:
                      memory+= haystack[count]
                  
                  else:
                      memory= ''
                      break
                  if count+1 <len(haystack):
                    count+=1                 
                  
                      
                                
                 
            if memory == needle:
                return i
        if needle ==haystack[-1:]:
            return len(haystack)-1 
        print("Did not find sol")     
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    
    result = sol.strStr("sadbutsad","sad")
    
    print(result)
    
            