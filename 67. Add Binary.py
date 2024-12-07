#not completed yet
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimalsum = 0
        result = ""

        for c in range(len(a)-1,-1,-1):
            
            
            if a[c] == '1':
                power = 2**c
                decimalsum += power
                
                
        for c in range(len(b)-1,-1,-1):
            
            
            if b[c] == '1':
                power = 2**c
                decimalsum += power

        
        while decimalsum!=0:

            print(decimalsum)


        

if __name__ == "__main__":
    sol = Solution()
    a = "11"
    b = "1"
    result = sol.addBinary(a,b)
    print(result)