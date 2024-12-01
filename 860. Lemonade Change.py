class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change = []
        for b in bills:
            if b ==5:
                change.append(5)
            elif b==10:
                try:

                    change.remove(5)
                    change.append(10)
                except:
                    return False
            else:
                try:
                    change.remove(10)
                    change.remove(5)
                    change.append(20)
                except:
                    try:
                        change.remove(5)
                        change.remove(5)
                        change.remove(5)
                    except:
                        return False
        return True
    
if __name__ == "__main__":
    sol = Solution()
    bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]
    result = sol.lemonadeChange(bills)
    print(result)     