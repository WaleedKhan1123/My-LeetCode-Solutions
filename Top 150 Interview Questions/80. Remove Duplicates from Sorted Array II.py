class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 4, 4, 4]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  