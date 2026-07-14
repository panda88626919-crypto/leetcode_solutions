class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range (len(nums)):
            for y in range (x + 1,len(nums)):
                if nums[x] + nums[y] == target:
                    return [x,y]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna