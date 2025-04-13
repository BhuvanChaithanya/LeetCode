class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        balls = 0 
        moves = 0

        res_sum = [0]*len(boxes)

        for i in range(len(boxes)):
            res_sum[i] = balls+moves

            moves = moves+balls
            if boxes[i] == '1':
                balls += 1

            

        
        balls, moves = 0,0

        for i in range(len(boxes)-1,-1,-1):
            res_sum[i] += balls+moves
            moves = moves+balls
            if boxes[i] == '1':
                balls += 1

        return res_sum