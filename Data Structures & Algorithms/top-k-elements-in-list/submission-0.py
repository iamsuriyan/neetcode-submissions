class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            values = {}

            for num in nums:
                if num in values:
                    values[num] += 1
                else:
                    values[num] =1
            
            sorted_values = sorted(values, key=values.get, reverse=True)

            return sorted_values[:k]