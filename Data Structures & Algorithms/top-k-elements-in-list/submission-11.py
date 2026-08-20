class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        items = list(count.items())

        def get_freq(item):
            return item[1]
        
        items.sort(key=get_freq, reverse=True)

        final = items[:k]

        result = []
        for i, _ in final:
            result.append(i)
        return result