'''
Use stack class to check whether parenthesis are balanced
'''

from stack import Stack

def is_match(p1, p2):
    if p1 == "{" and p2 == "}": return True
    elif p1 == "[" and p2 == "]": return True
    elif p1 == "(" and p2 == ")": return True
    else: return False
    
def is_paren_balanced(paren_str):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_str) and is_balanced:
        paren = paren_str[index]
        if paren in "{([":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

    # paren_str = list(paren_str)
    # for i in range(len(paren_str)):
    #     if paren_str[i] in ["{", "[", "("]:
    #         s.push(paren_str[i])
    #     elif paren_str[i] in ["}", "]", ")"]:
    #         if s.is_empty() or paren_str[i] != s.peek():
    #             return False
    # return True

print(is_paren_balanced("{{()}}"))