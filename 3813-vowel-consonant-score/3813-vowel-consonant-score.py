class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = "aeiou"
        vow = 0
        con = 0 

        for x in s:
            if x.isalpha():
                if x in vowels:
                    vow += 1
                else:
                    con += 1

        if con == 0:
            return 0

        return vow // con

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna