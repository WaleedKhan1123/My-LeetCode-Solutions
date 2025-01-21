class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = {'5':0,'10':0,'20':0}

        for b in bills:
            if b == 5:
                change['5']+=1
            elif b==10:
                if change['5']>0:
                    change['10']+=1
                    change['5']-=1
                else:
                    return False
                
            else :
                if change['5']>0 and change['10']>0:
                    change['10']-=1
                    change['5']-=1
                    change['20'] +=1
                elif change['5']>=3:
                    change['5']-=3
                else:
                    return False
        return True
        
    
if __name__ == "__main__":
    sol = Solution()
    bills = [5,5,5,20]
    result = sol.lemonadeChange(bills)
    print(result)     