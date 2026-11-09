class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums))]

        for n in nums:
            count[n] += 1
            
        
        for key, value in count.items():
            freq[value-1].append(key)

        ans = []

        for i in range(len(freq) - 1, -1, -1):
            if freq[i]:
                for j in freq[i]:
                    ans.append(j)
                    if len(ans) == k:
                        return ans

        return ans