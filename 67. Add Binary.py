#not completed yet
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimalsum = 0

        for c in range(len(a)-1,-1,-1):
            
            
            if a[c] == 1:
                power = 2**c
                decimalsum = power
        print(decimalsum)
                


if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    result = sol.addBinary(a,b)
    print(result)