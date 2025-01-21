class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        
        if x1 - x0 == 0:  
            for x, y in coordinates:
                if x != x0:
                    return False
            return True
        
        
        initial_slope = (y1 - y0) / float(x1 - x0)
        
        
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            
            if x - x0 == 0 or (y - y0) / float(x - x0) != initial_slope:
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()
    coordinates = [[2, 4], [2, 5], [2, 8]]  
    result = sol.checkStraightLine(coordinates)
    print(result)  
