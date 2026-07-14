class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        y = set()

        for num in nums:
            if num in y:
                return True
            y.add(num)

        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna