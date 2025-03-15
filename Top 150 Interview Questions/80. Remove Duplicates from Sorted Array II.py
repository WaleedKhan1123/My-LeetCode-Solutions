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
        while i <len(nums):
           print(i)
           if nums[i]==nums[i]+1:
              if nums[i] == nums[i]+2:
                for j in range(i,len(nums)-1):
                   nums[j],nums[j+1] = nums[j+1],nums[j]
                i+=3
           
           else:
              i=i+1

            
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  