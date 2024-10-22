class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            print(nums[i])

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,2,3]
    result = sol.isMonotonic(nums)
    print(result)
    
    
    