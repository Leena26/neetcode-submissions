class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            y = list(Counter(x))
            y.sort()
            hashmap.setdefault(tuple(y), []).append(x)
        print(hashmap)
        return list(hashmap.values())
            
                

                



        