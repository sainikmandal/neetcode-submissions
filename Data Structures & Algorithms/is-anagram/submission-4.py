import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        alphabet_dict = {letter: 0 for letter in string.ascii_lowercase}
        for letter in s:
            alphabet_dict[letter] += 1
        for letter in t:
            alphabet_dict[letter] -= 1
        
        for letter in alphabet_dict:
            if alphabet_dict[letter] != 0:
                return False
        return True


        
        
        