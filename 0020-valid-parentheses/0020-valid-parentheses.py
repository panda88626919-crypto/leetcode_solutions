class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x == "(" or x == "[" or x == "{":
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False

                top = stack.pop()

                if x == ")" and top != "(":
                    return False
                if x == "]" and top != "[":
                    return False
                if x == "}" and top != "{":
                    return False

        return len(stack) == 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna