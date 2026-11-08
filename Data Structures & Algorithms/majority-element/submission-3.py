class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = nums[0]

        for n in nums:
            if n == ans:
                count += 1
            else:
                count -= 1
                if count == -1:
                    count = 1
                    ans = n
        
        return ans

        

