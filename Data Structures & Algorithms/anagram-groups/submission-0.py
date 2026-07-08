class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <2: 
            return [strs]
        words = strs
        group = []
        while words != []:
            word = words[0]
            new = []
            for x in words:
                if Counter(x) == Counter(word):
                    new.append(x)
            for x in new:
                words.remove(x)
            group.append(new)
        return group
            
                

                



        