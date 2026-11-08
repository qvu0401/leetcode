class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, k = 0, 0

        while n > 0 and m > 0:
            print(nums1, "m: " + str(m), "n: " + str(n), "i: " + str(i), "k: " + str(k))
            if nums2[k] < nums1[i]:
                nums1.insert(i, nums2[k])
                nums1.pop()
                n -= 1
                k += 1
                i += 1
            else: 
                i += 1
                m -= 1
        for i in range(n):
            nums1.pop()
        nums1 += nums2[k: k + n]

        