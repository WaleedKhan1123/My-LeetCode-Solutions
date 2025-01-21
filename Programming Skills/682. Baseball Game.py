class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result=[]
        for value in operations:
            try:
                result.append(int(value))
            except:
                
                if value == "C":
                  if(len(result)!=0):
                    result.pop()
                    
                elif value =="D":
                    result.append(result[-1]*2)
                    
                else:
                    result.append(result[-1]+result[-2])
                    
        totalsum =  sum(result)
        return totalsum
        
        
if __name__ == "__main__":
    sol = Solution()
    ops = ["5","2","C","D","+"]
    result = sol.calPoints(ops)
    print(result)       