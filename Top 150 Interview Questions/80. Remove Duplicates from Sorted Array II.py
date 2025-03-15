class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        write_index = 0
        for i in range(len(nums)):
            if write_index < 2 or nums[i] != nums[write_index - 2]:
                nums[write_index] = nums[i]
                write_index += 1
        
        return write_index

            
if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  