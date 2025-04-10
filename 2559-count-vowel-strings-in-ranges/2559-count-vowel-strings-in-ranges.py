class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        count = 0
        prefix_sum = [0]* (len(words)+1)
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                count += 1

            prefix_sum[i+1] = count
        res = [0]*len(queries)

        for i,q in enumerate(queries):
            l, r = q

            res[i] = prefix_sum[r+1]- prefix_sum[l]

        return res


        
