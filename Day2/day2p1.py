invalid_id  = 0

with open('document.txt', 'r') as df:
    for data in df:
        data = data.split(',')

    for r in data:
        start, end = r.split('-', 1)
        start = int(start)
        end = int(end)

        for id in range(start,end+1):
            id = str(id)
            if len(id) % 2 == 0:
                half = len(id) // 2
                first_part = id[0:half]
                second_part = id[half:]
                if first_part == second_part:
                    invalid_id += int(id)
print(invalid_id)
