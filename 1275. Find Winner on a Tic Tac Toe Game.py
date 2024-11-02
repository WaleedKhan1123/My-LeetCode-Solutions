class Solution(object):
    def tictactoe(self, moves):
        """
        :type moves: List[List[int]]
        :rtype: str
        """
        
        a_moves = [moves[move] for move in range(0,len(moves),2)]
        b_moves = [moves[move] for move in range(1,len(moves),2)]
        win1= [[0,0],[1,1],[2,2]]
        win2= [[0,0],[1,0],[2,0]]
        win3= [[0,0],[0,1],[0,2]]
        win4= [[1,0],[1,1],[1,2]]
        win5= [[2,0],[2,1],[2,2]]
        win6= [[0,2],[1,1],[2,0]]
        win7= [[2,0],[2,1],[2,2]]
        win8= [[0,1],[2,1],[2,2]]
        print(a_moves)
        print(b_moves)
if __name__ == "__main__":
    sol = Solution()
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    result = sol.tictactoe(moves) 
    
    print(result)
    
    