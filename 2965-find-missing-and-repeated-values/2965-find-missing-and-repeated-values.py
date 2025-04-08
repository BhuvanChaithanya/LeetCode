class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        miss, rep = 0,0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                count[grid[i][j]] += 1

        for i in range(1,(len(grid)**2)+1):
            if count[i] == 0:
                miss = i

            elif count[i] == 2:
                rep = i

        return [rep,miss]
            