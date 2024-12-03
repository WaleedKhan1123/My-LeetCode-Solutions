class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x = []
        y = []

        for c in coordinates:
            x.append(c[0])
            y.append(c[1])

        x.sort()       
        y.sort()

        distance_x = x[1] - x[0]
        distance_y = y[1] - y[0]

        for c in range(len(coordinates)-1):
            
            if x[c+1]-x[c]==distance_x and y[c+1]-y[c]==distance_y:
                continue
            else:
                return False

        return True
    
if __name__ == "__main__":
    sol = Solution()
    coordinates = [[2,4],[2,5],[2,8]]
    result = sol.checkStraightLine(coordinates) 
    
    print(result)