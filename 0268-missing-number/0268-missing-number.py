class Solution:
    def missingNumber(self, nums):
        x = len(nums)

        total = x * (x + 1) // 2
        arr_sum = sum(nums)

        return total - arr_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna