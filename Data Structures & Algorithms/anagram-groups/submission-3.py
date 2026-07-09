class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            w = ''.join(sorted(s))
            res[w].append(s)
        return list(res.values())

            
                

                



        