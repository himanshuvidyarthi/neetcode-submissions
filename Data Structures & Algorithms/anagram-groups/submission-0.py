from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)
        return [i for i in res.values()]

        