class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        cleaned_s = "".join([char for char in s.lower() if char.isalnum()])
        j = len(cleaned_s) - 1
        while j > i:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i += 1
            j -= 1
        return True
