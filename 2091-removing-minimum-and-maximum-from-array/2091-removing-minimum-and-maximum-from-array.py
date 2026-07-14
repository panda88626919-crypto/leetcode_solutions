class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        from_front = max_index + 1
        from_back = len(nums) - min_index
        both = (min_index + 1) + (len(nums) - max_index)

        return min(from_front, from_back, both)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna