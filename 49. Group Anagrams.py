from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for s in strs:
            alphabet_freq = [0]*26
            for c in s:
                alphabet_freq[ord(c)-ord('a')] += 1
            
            anagram_group[tuple(alphabet_freq)].append(s)

        return list(anagram_group.values())
