def calc7(numbers):
    sum = 0
    i = 0
    double = False
    n = len(numbers)
    if n == 0: return -1
    while i < n:
        sum += numbers[i]
        if double:
            sum += numbers[i]
            double = False
        if numbers[i] == 7: double = True
        i += 1
    return sum

print(calc7([1, 2]))
print(calc7([3, 7]))
print(calc7([7, 5, 6]))
print(calc7([7, 9, 7, 9, 7, 9]))
print(calc7([]))