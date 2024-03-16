
def multiply_strings(num1, num2):
    num1 = num1[::-1]
    num2 = num2[::-1]

    result = [0] * (len(num1)+ len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i+j] += int(num1[i]) * int(num2[j])
            result[i+j+1] += result[i+j] // 10
            result[i+j] %= 10
        result_str = ''.join(map(str, result[::-1])).lstrip('0')

    return result_str if result_str else '0'

print(multiply_strings("14","336"))

# Time Complexity : O(M*N)