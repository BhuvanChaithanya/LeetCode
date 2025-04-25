class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_freq = defaultdict(int)
        for i in range(len(rectangles)):
            ratio = rectangles[i][0]/rectangles[i][1]
            ratio_freq[ratio] = ratio_freq.get(ratio,0)+1

        res = 0

        for r,f in ratio_freq.items():
            if f > 1:
                res += (f*(f-1))
        return int(res/2)
        