class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, n in enumerate(nums):
            ans = target - n
            if ans in seen:
                return [seen[ans], i]
            
            seen[n] = i
        