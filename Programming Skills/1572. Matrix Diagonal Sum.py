import math 
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        second_i=0
        matrixlen = len(mat[0])
        ceil = 0
        
        if matrixlen ==1:
            return mat[0][0]
        
        if matrixlen %2 !=0:
            ceil = math.ceil(matrixlen/2)-1
        
        for i in range(len(mat[0])):
            sum+=mat[i][i]
        
        if ceil>0:
            
            for i in range(len(mat[0]) - 1, -1, -1):
                
                if ceil!=i:
                    sum+=mat[second_i][i]
                    
                second_i+=1
                
        else:
            for i in range(len(mat[0]) - 1, -1, -1):
                

                sum+=mat[second_i][i]
                    
                second_i+=1
                
        
        return sum
        
if __name__ == "__main__":
    sol = Solution()
    
    mat = [[1,3,5],
           [6,2,3],
           [9,12,3]]
    
    result = sol.diagonalSum(mat)
    
    print(result)