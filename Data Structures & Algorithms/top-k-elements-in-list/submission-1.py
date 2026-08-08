from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict=Counter(nums)
        return list(dict(freq_dict.most_common()).keys())[:k]
        