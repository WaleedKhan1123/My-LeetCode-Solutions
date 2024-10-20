class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None (in-place modification)
        """
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        print(nums)
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
        print(nums)
        return nums 
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    result = sol.moveZeroes(nums)
    print(result)
    