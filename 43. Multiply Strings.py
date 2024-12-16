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
        numa=0
        numb=0
        for n in num1:
            numx.append(num[n])

        for n in num2:
            numx.append(num[n])
        c=0
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

        


if __name__ == "__main__":
    sol = Solution()
    num1 = "20"
    num2 = "10"
    result = sol.multiply(num1,num2)
    print(result)