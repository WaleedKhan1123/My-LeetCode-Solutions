class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        
        Directions = {
            
            "North":1,
            "West":0,
            "East":0,
            "South":0
        }
        coordinates = [0,0]
        Circle = 0
        c = 0
        while c != 10:
            for i in instructions:
                if i == "G":
                    if Directions["North"]==1:
                        coordinates[1]=coordinates[1]+1 
                    elif Directions["West"]==1:
                        coordinates[0]=coordinates[0]-1
                    elif Directions["South"] ==1:
                        coordinates[1]=coordinates[1]-1
                    elif Directions["East"] ==1:
                        coordinates[0]=coordinates[0]+1
                                        
                elif i =="L":
                    if Directions["North"]==1:
                        Directions["North"] = 0
                        Directions["West"] = 1
                    elif Directions["West"]==1:
                        Directions["West"] = 0
                        Directions["South"] = 1
                    elif Directions["South"] ==1:
                        Directions["South"] = 0
                        Directions["East"] =1
                    elif Directions["East"] ==1:
                        Directions["East"] = 0
                        Directions["North"] =1
                elif i == "R":
                    if Directions["North"]==1:
                        Directions["North"] = 0
                        Directions["East"] = 1
                    elif Directions["East"]==1:
                        Directions["East"] = 0
                        Directions["South"] = 1
                    elif Directions["South"] ==1:
                        Directions["South"] = 0
                        Directions["West"] =1
                    elif Directions["West"] ==1:
                        Directions["West"] = 0
                        Directions["North"] =1
                           
            if coordinates[0] == 0 and coordinates [1] ==0:
                return True
            c +=1
            
        return False
    

if __name__ == "__main__":
    sol = Solution()
    instructions = "GG"
    result = sol.isRobotBounded(instructions) 
    
    print(result)