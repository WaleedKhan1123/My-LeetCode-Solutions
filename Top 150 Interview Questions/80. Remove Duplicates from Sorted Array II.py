#not completed yet
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
         return 0
        
        i=0      
        while i <10:
           print(i)
           i=i+2
            
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  