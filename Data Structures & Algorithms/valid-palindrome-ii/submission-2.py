class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1
        count = 0

        while i < k:
            if s[i] != s[k]:

                temp = s[i + 1: k + 1]
                if temp == temp[::-1]: 
                    return True
                else: 
                    temp = s[i: k]
                    if temp == temp[::-1]:
                        return True
                return False

            i += 1
            k -= 1
        return True
        