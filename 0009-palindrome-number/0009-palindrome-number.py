class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = ""
        for a in s:
            rev = a + rev
             
        if s == rev:
            return True
        else:
            return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna