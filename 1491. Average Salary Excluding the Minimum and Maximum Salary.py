class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        sums=[]
        for i in range(1,len(salary)-1):
            sums.append(salary[i])

        return sum(sums)/len(sums)

if __name__ == "__main__":
    sol = Solution()
    
    salary = [4000,3000,1000,2000]
    
    result = sol.average(salary)
    
    print(result)