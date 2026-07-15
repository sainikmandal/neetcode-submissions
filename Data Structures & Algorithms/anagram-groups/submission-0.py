class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramGroups = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char)-ord('a')] += 1
            key = tuple(count)

            if key in anagramGroups:
                anagramGroups[key].append(s)
            else:
                anagramGroups[key] = [s]
        
        return list(anagramGroups.values())
    