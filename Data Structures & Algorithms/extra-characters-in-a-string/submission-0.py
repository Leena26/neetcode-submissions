class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, w):
        cur = self.root
        for c in w:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for w in dictionary:
            trie.addWord(w)
        
        dp = {len(s):0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)
            cur = trie.root

            for j in range(i, len(s)):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.end:
                    res = min(res, dfs(j+1))
            
            dp[i] = res
            return res
        
        return dfs(0)











