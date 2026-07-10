class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = defaultdict(int)
        for i in nums:
            if not seq[i]:
                seq[i] = seq[i-1] + seq[i+1] +1
                seq[i - seq[i-1]] = seq[i]
                seq[i + seq[i+1]] = seq[i]
        return max(seq.values())