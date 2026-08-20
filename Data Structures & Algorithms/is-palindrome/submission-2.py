class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        
        reverse = cleaned[::-1]

        if cleaned == reverse:
            return True
        else:
            return False