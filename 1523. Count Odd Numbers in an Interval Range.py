class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return (high+1)//2 - low//2
if __name__ == "__main__":
    sol = Solution()
    low, high = 3 , 7
    result = sol.countOdds(low,high)
    print(result)