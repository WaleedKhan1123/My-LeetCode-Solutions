class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        low,high= min(salary),max(salary)
        avg=[]
        for i in salary:
            if i !=high or i!=low:
                avg.append(i)
        return sum(avg)/len(avg)
    
if __name__ == "__main__":

    sol = Solution()
    
    salary = [4000,3000,1000,2000]
    
    result = sol.average(salary)
    
    print(result)