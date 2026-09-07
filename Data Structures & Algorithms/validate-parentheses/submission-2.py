class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "]":"[", "}":"{" }

        for i in s:
            if i in brackets:
                if not stack or brackets[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        return not stack