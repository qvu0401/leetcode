class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0

        while index1 < len(numbers):
            index2 = index1 + 1
            while (index2 < len(numbers) and numbers[index1] + numbers[index2] <= target):
                print(index1, index2)
                if numbers[index1] + numbers[index2] == target:
                    return [index1 + 1, index2 + 1]

                index2 += 1

            index1 += 1

