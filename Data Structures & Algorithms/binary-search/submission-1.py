class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        i = -1
        while l < r:
            i = (r + l) // 2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                r = i
            else: 
                l = i + 1
        if nums[i] == target:
            return i
        else:
            return -1
        



        