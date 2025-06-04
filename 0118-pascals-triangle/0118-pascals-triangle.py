class Solution:
    def generateRow(self, row):
        ans = 1
        res = [1]

        for col in range(1, row):
            ans *= (row-col)
            ans = ans//col

            res.append(ans)
        return res

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1,numRows+1):
            ans.append(self.generateRow(i))

        return ans



        