from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if not same(s[i], s[len(s) - 1 - i]):
                return False
        return True

def same(a: str, b: str) -> bool:
    ab = a + b
    print(ab)
    if ab == "()" or ab == "{}" or ab == "[]":
        return True
    return False