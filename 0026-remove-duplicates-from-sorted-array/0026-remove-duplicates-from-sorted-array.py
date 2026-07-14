class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1

        for y in range (1,len(nums)):
            if nums[y] != nums[y - 1]:
                nums[x] = nums[y]
                x += 1

        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna