class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        length = len(matrix)
        reverse = len(matrix[0])-1 
        if length==1:
            return matrix[0]
        if length ==2:
           for i in range(length):
               for b in range(len(matrix[0])):
                 
                if i==0:
                    spiral.append(matrix[i][b])
                else:
                    spiral.append(matrix[i][reverse])
                    reverse-=1
           return spiral             
        reverse = len(matrix[0])-1
        for i in range(length):
            for b in range(len(matrix[0])):
                if i==1:
                    spiral.append(matrix[i][-1])
                    break
                elif i==0:
                    spiral.append(matrix[i][b])
                else:
                    spiral.append(matrix[i][reverse])
                    reverse-=1
                       
        for i in range(0,len(matrix[1])-1):
            
            spiral.append(matrix[1][i])
        return spiral
if __name__ == "__main__":
    sol = Solution()
    matrix = [[2,5,8],[4,0,-1]]
    result = sol.spiralOrder(matrix)
    print(result)