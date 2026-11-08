class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       prevMap = {}

       for i, n in enumerate(nums):
            ans = target - n
            if ans in prevMap:
                return [prevMap[ans], i]
            prevMap[n] = i


        