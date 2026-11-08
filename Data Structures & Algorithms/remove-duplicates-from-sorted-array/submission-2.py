class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = k = 0
        while k < len(nums):
            nums[i] = nums[k]
            while k < len(nums) and nums[k] == nums[i]:
                k += 1
            i += 1
        return i

        