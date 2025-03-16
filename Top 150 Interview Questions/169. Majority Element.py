class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)/2
        counter = 0
        current_frequent = None
        for i in nums:
            for j in nums:
                if j == i:
                  counter+=1
                if counter>n:
                    current_frequent = j
        return current_frequent
            
             

                
    
        
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,1,1,1,2,2]
    result = sol.majorityElement(nums)
    print(result)