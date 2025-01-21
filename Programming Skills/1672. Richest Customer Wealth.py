class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richList = []
        wealth = 0
        for a in accounts:
             
            
            for i in range(len(a)):
               wealth+=a[i]      
            richList.append(wealth)
            wealth=0
        richest = max(richList)
        try:
         if len(richest)>1:
            return richest[0]
        except:
            return richest    
        
    
if __name__ == "__main__":
    sol = Solution()
    accounts = [[1,5],[7,3],[3,5]]
    result = sol.maximumWealth(accounts)
    
    print(result)