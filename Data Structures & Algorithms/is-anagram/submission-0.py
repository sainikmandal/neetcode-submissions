class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_counts_s = [0] * 26  # Assuming lowercase English alphabets
        char_counts_t = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            char_counts_s[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            char_counts_t[index] += 1

        return char_counts_s == char_counts_t
