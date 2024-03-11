def group_numbers(numbers, target):
    result = []
    others = []
    for i in range (len(numbers)):
        if numbers[i] % target == 0:
            result.append(numbers[i])
        else:
            others.append(numbers[i])
    return [result, others]

print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))  
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))