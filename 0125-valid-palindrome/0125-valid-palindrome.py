class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str=""
        for i in s:
            if i.isalnum():
                new_str+=i.lower()
        return new_str==new_str[::-1]


        #  isalnum() checks if the character is:
        #   a letter (A–Z or a–z) or a number (0–9)
        #    Everything else (spaces, commas, colons, etc.) is skipped.



