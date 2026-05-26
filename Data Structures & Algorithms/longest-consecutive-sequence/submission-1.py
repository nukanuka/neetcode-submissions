class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        lookup = set(nums)
        longest = 0

        for num in nums:

            # start of a sequence
            if num - 1 not in lookup:

                current = num
                curMax = 1

                # extend streak
                while current + 1 in lookup:
                    current += 1
                    curMax += 1

                longest = max(longest, curMax)

        return longest