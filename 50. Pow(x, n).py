class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        result = x**n
        print(result)
if __name__ == "__main__":
    sol = Solution()
    x = 2.00000
    n = 10
    result = sol.myPow(x,n)
    print(result)