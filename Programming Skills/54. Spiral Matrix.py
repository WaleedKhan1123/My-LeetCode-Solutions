class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])  
        top, bottom, left, right = 0, m - 1, 0, n - 1
        result = []
        
        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  
            
            
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  
            
            
            if top <= bottom:  
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  
            
            
            if left <= right:  
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  
        
        print(f"Spiral Matrix is {result}")
        return result

if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = sol.spiralOrder(matrix)
    print(result)
