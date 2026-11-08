class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in seen:
                return [seen[ans], i]
            seen[nums[i]] = i

