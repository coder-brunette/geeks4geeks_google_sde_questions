def check_balanced_brackets(s):
    stack = []
    char_map = {'{':'}','[':']','(':')'}

    for char in s:
        if char in char_map.keys():
            stack.append(char)
        elif char in char_map.values():
            if not stack or char_map[stack.pop()] != char:
                return False
    return True

print(check_balanced_brackets("[(])"))