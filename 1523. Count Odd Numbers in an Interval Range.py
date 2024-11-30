class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        oddcount=0 

        for i in range(low,high):
            print(i)

if __name__ == "__main__":
    sol = Solution()
    low = 3, high = 7
    result = sol.countOdds(low,high)
    print(result)