class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        count1 = Counter(s)
        count2 = Counter(t)
        if count1 != count2:
            return False
        return True