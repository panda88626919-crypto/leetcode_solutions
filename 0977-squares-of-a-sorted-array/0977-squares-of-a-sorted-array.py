class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            result.append(num*num)

        result.sort()

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna