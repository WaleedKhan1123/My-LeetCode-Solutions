#not completed yet
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
        nums = {
            '0':'0',
            '1':'1',
            '2':'2',
            '3':'3',
            '4':'4',
            '5':'5',
            '6':'6',
            '7':'7',
            '8':'8',
            '9':'9'
        }
        numx=[]
        num_digits = 1
        num3=0
        num4=0
            
        for n in range(len(num1)-1):
             if n ==0:
              num3 = num[num1[n]] * (10 ** num_digits) + num[num1[n+1]] 
             else:
                num3 = num3 * (10 ** num_digits) + num[num1[n+1]]
        
        for n in range(len(num2)-1):
             if n ==0:
              num4 = num[num2[n]] * (10 ** num_digits) + num[num2[n+1]] 
             else:
                num4 = num4 * (10 ** num_digits) + num[num2[n+1]]          
        result = num3*num4  
        print(result)
        while result>0:
            digit = result%10
            numx.append(digit)
            result//=10
        numx.reverse()
        resultString = ""
        for n in numx:
           resultString+=nums[n]
        print(resultString) 

        


if __name__ == "__main__":
    sol = Solution()
    num1 = "20"
    num2 = "10"
    result = sol.multiply(num1,num2)
    print(result)