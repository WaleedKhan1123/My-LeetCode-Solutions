class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k > n

        # Reverse the entire list
        nums.reverse()
        # Reverse first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the rest
        nums[k:] = reversed(nums[k:])


        
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-100,3,99]
    k = 2
    sol.rotate(nums,k)
    print(nums)