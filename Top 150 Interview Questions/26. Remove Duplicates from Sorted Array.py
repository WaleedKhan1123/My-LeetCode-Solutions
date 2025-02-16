class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        unique_index = 0  
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:  
                unique_index += 1
                nums[unique_index] = nums[i]  
        
        
        return unique_index + 1  

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 4, 4, 4]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  
