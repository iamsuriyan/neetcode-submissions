class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []

        for _ in range(k):
            max_key = None
            max_freq = -1

            for key, value in freq.items():
                if value > max_freq:
                    max_freq = value
                    max_key = key
            result.append(max_key)
            del freq[max_key]
        return result