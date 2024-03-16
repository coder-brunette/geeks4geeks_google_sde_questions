# def valid_string_cnt(s):
#     stack = []
#     char_dict = {'{':'}','[':']','(':')'}
#     current_length = 0
#     max_length = 0
#     for char in s:
#         if char in char_dict.keys():
#             stack.append(char)
#         elif char in char_dict.values():
#             if stack and char == char_dict[stack.pop()]:
#                 current_length += 2
#                 max_length = max(max_length, current_length)
#             else:
#                 current_length = 0
#     return max_length 

# #print(valid_string_cnt(")()())"))
# print(valid_string_cnt("()()())))"))

def longest_valid_substring(s):
    stack = []
    max_length = 0
    start = -1
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    max_length = max(max_length, i - start)
            else:
                start = i
    return max_length

print(longest_valid_substring("()()())))"))