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
        counter = 0
        while i <len(nums):
           if nums[i]==nums[i+1]:
              if nums[i] == nums[i+2]:
                print("working")
                for j in range(i,len(nums)-1):
                   nums[j],nums[j+1] = nums[j+1],nums[j]
                i+=3
                counter+=1
              else:
                print("working")
                i+2
           
           else:
              print("working")
              i=i+1
        return len(nums)-counter

            
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1,2,2,3]
    new_length = sol.removeDuplicates(nums)
    print(nums[:new_length])  