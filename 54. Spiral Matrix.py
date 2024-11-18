class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
         
        
        m  = len(matrix)
        n  = len(matrix[0])
        print(f"matrix is {m} x {n}")
        newMatrix = []
        traverse = 0
        reverse = 0
        if m == 1:
            return newMatrix+matrix[0]
        x=0
        for i in matrix:
          x+=1
          if traverse==0 and reverse==0:
               for j in i:
                   newMatrix.append(j)
               
               traverse=1
          elif traverse==1 and reverse ==0:
              for k in range(1,m):
                  print(f"k is {k}")
                  newMatrix.append(matrix[k][n-1])
                  
              m-= 1
              
          if x == 2:
           break
       
               
          
           
        print(f"Spiral Matix is {newMatrix}")
       
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    result = sol.spiralOrder(matrix)
    print(result)