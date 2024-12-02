class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,c =0,0,0
        nums.sort(reverse =True)
        if nums[0]>= nums[1] and nums[1]>=nums[2]:
            c = nums[0]
            b = nums[1]
            a = nums[2]
            return a+b+c
        else:
            return 0 

if __name__ == "__main__":

    sol = Solution()
    
    nums = [1,2,1,10]
    result = sol.largestPerimeter(nums)
    
    print(result)