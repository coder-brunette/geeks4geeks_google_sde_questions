
def sum_of_bit_diff(arr):
    n = len(arr)
    sum = 0

    for i in range(n):
        for j in range(i+1, n):
            xor_res = arr[i] ^ arr[j]
            bit_diff = bin(xor_res).count('1')
            sum += bit_diff 
    return sum * 2

print(sum_of_bit_diff([1,3, 5]))    
