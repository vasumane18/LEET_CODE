class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stk.append(c)
            else:
                if not stk or abs(ord(stk[-1]) - ord(c)) > 2: return False
                stk.pop()
        return not stk