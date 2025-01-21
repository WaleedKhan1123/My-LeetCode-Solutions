class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        return x**n
        
if __name__ == "__main__":
    sol = Solution()
    x = 2.00000
    n = -2
    result = sol.myPow(x,n)
    print(result)