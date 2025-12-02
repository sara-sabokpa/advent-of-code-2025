total_invalid = 0

with open('document.txt', 'r') as df:
    ranges = df.read().strip().split(',')

    for r in ranges:
        start, end = map(int, r.split('-'))
        for num in range(start, end+1):
            num_str = str(num)
            if len(num_str) % 2 == 0:
                half = len(num_str) // 2
                if num_str[0:half] == num_str[half:]:
                    total_invalid += num
print(total_invalid)