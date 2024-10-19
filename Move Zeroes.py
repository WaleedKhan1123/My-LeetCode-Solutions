class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=len(nums)
        print(nums[count-2])
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    result = sol.moveZeroes(nums)
    