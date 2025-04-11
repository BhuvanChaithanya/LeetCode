class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        res = []
        end = []
        for n in arr2:
            for i in range(count[n]):
                res.append(n)
            
        for n in arr1:
            if n not in arr2:
                end.append(n)

        end.sort()

        for n in end:
            res.append(n)
        return res