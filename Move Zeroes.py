#not Complete Yet
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        for i in range(len(nums)):
            if(nums[i]==0):
                nums[-1:],nums[i]==nums[i]
        count=len(nums)
        print(nums)
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    result = sol.moveZeroes(nums)
    print(result)
    