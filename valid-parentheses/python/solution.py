class Solution:
    def isValid(self, s: str) -> bool:
        relations = {")": "(", "]": "[", "}": "{"}
        stack = []
        for p in s:
            if p in relations:  # Closing
                if len(stack) == 0 or stack.pop() != relations[p]:
                    return False
                continue

            stack.append(p)

        return len(stack) == 0


""" Before refactors

    lots of "in" operators on a list = nono performance
    unnecessary .index() and conditions => use a dictionary

    closing = (')', ']', '}')
    stack = []
    for paren in s:
        if paren in closing:
            if len(stack) == 0:
                return False

            idx = closing.index(paren)
            if idx == 0:  # (
                if stack[-1] != '(':
                    return False
            elif idx == 1:
                if stack[-1] != '[':
                    return False
            elif idx == 2:
                if stack[-1] != '{':
                    return False
            stack.pop()
        else:
            # put in stack
            stack.append(paren)

    return stack.__len__() == 0
"""

""" First refactor

adapt to dictionary

relations = {")": "(", "]": "[", "}": "{"}
stack = []
for p in s:
    if p in relations:  # Closing
        if len(stack) == 0:
            return False

        if stack[-1] != relations[p]:
            return False

        stack.pop()
        continue

    stack.append(p)

return len(stack) == 0 """
