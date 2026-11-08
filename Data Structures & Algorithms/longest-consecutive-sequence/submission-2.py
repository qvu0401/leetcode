class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in seen:
                count = 1
                while n + count in seen:
                    count += 1

                if count > res:
                    res = count

        return res
        