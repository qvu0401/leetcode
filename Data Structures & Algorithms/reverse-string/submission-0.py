class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, k = 0, len(s) - 1

        while i < k:
            tempi = s[i]
            tempk = s[k]
            s[i] = tempk
            s[k] = tempi

            i += 1
            k -= 1
