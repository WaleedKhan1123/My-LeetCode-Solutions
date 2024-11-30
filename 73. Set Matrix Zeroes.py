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
        for i in range(len(row)):
            
                
        
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    sol.setZeroes(matrix)
    print(matrix)       