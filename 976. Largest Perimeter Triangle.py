class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,c =0,0,0
        sum = 0
        nums.sort(reverse =True)
        for n in nums:
            if n<=b:
                a=n
            elif n<=c:
                b=n
            else:
                c=n
        sum= a+b+c

        return sum

if __name__ == "__main__":

    sol = Solution()
    
    nums = [2,1,2]
    result = sol.largestPerimeter(nums)
    
    print(result)