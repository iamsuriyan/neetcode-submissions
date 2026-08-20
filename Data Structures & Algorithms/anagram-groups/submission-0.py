class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for str in strs:
            sort = "".join(sorted(str))
            if sort in seen:
                seen[sort].append(str)
            else:
                seen[sort] = [str]
        return list(seen.values())