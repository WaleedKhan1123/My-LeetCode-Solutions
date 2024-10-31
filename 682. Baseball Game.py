class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        numbers=[]
        signs = []
        for i in operations:
            try:
                numbers.append(int(i))
            except:
                signs.append(i)
        print(numbers)
        print(signs)
        
        
        
if __name__ == "__main__":
    sol = Solution()
    ops = ["5","2","C","D","+"]
    result = sol.calPoints(ops)
    print(result)       