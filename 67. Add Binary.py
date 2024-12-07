class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        decimalsum = 0
        result = ""
        i = 0

        for c in range(len(a)-1,-1,-1):
            
            
            if a[c] == '1':
                power = 2**i
                decimalsum += power
            i+=1
                
        i = 0
        
        for c in range(len(b)-1,-1,-1):
            
            
            if b[c] == '1':
                power = 2**i
                decimalsum += power
            i+=1
        
        while decimalsum!=0:
             
            remainder = decimalsum%2

            result = str(remainder) + result

            decimalsum = decimalsum//2

        return result

        

if __name__ == "__main__":
    sol = Solution()
    a = "1010"
    b = "1011"
    result = sol.addBinary(a,b)
    print(result)