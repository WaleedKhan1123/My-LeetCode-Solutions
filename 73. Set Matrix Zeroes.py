#not completed yet 
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row , column = [],[]
        for r in range(len(matrix)):
            
            for c in range(len(matrix[r])):
                 
                 if matrix[r][c] == 0:
                    row.append(r)
                    column.append(c)
        print(row)
        print(column)
        for i in row:
            for r in range(len(matrix)):
                matrix[r][i]=0
            for c in range(len(matrix[0])):
                    matrix[i][c] = 0

            
            
                
        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    print(matrix)       