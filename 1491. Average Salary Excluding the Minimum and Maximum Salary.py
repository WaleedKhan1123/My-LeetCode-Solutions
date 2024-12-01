class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        min ,max= -1,0
        avg=[]
        for i in salary:
            if i <min:
                min = i
            elif i>max:
                max=i
            else:
                avg.append(i)

        print(avg)
        return sum(avg)/len(avg)
    
if __name__ == "__main__":
    sol = Solution()
    
    salary = [4000,3000,1000,2000]
    
    result = sol.average(salary)
    
    print(result)