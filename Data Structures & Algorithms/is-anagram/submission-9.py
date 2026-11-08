class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}
        if len(t) != len(s):
            return False

        for i in range(len(s)):
            sHash[s[i]] = sHash.get(s[i], 0) + 1
            tHash[t[i]] = tHash.get(t[i], 0) + 1

        if sHash == tHash:
            return True
        return False