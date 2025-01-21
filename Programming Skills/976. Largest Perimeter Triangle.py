class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse =True)
        for i in range(len(nums) - 2):
           
            if nums[i] < nums[i + 1] + nums[i + 2]:
              
                return nums[i] + nums[i + 1] + nums[i + 2]
        else:
            return 0 

if __name__ == "__main__":

    sol = Solution()
    
    nums = [3,6,2,3]
    result = sol.largestPerimeter(nums)
    
    print(result)