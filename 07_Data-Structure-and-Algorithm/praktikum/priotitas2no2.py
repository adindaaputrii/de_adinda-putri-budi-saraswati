def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_rectangle(height, width, start):
    curr_num = start
    total_sum = 0
    for i in range(width):
        row = []
        for j in range(height):
            while not is_prime(curr_num):
                curr_num += 1
            row.append(curr_num)
            total_sum += curr_num
            curr_num += 1
        print(*row, sep=" ")
    print(total_sum)

# Contoh penggunaan
prime_rectangle(2, 3, 13)
print("")
prime_rectangle(5, 2, 1)
