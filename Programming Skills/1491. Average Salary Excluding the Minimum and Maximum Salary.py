class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        low,high= min(salary),max(salary)
        avg=[]
    
        for i in salary:
            if i !=high and i!=low:
                avg.append(i)
        
        return sum(avg)/len(avg)
    
if __name__ == "__main__":

    sol = Solution()
    
    salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
    
    result = sol.average(salary)
    
    print(result)