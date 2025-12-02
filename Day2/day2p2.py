total_invalid = 0

def is_repeated_pattern(n):
    return n in (n + n)[1:-1]

with open('document.txt', 'r') as df:
    ranges = df.read().strip().split(',')

    for r in ranges:
        start, end = map(int,r.split('-'))

        for num in range(start,end+1):
            num_str = str(num)
            if is_repeated_pattern(num_str) == True:
                total_invalid += num
print(total_invalid)
