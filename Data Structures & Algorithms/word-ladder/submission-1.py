class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + "*" + w[j+1:]
                nei[pattern].append(w)
        
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                
                for j in range(len(w)):
                    pattern = w[:j] + "*" + w[j+1:]
                    for n in nei[pattern]:
                        if n not in visit:
                            visit.add(n)
                            q.append(n)
            res +=1
        return 0
