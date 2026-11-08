class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        print(count)
        freq = [[] for i in range(len(nums) + 1)]
        for n in count:
            print(n, count[n] - 1)
            freq[count[n] - 1].append(n)

        print(freq)
        ans = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

