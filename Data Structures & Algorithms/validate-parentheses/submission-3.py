class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b_map = {")":"(", "}":"{", "]": "["}

        for c in s:
            if c in b_map:
                if stack and stack[-1] == b_map[c]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

        