class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movements = [0,0]
        
        for m in moves:
            if m =="U":
                movements[0]+=10
            elif m =="D":
                movements[0]-=10
            elif m =="R":
                movements[1]+=10
            else:
                movements[1]-=10
        
        if all(x == 0 for x in movements):
            return True
        return False
        
            

if __name__ == "__main__":
    sol = Solution()
    moves = "UD"
    result = sol.judgeCircle(moves)
    print(result)