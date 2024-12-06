#not completed yet
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        dec = {
            '1': 1, 
            '11': 2,
            '100': 4,
            '1000': 8,
            '10000': 16,
            '100000': 32
        }

if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    result = sol.addBinary(a,b)
    print(result)