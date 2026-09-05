class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_word1 = "".join(sorted(s))
        sorted_word2 = "".join(sorted(t))
        if sorted_word1 == sorted_word2: return True
        return False
        
        