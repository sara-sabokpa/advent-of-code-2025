invalid_id  = 0

def is_repeated_pattern(id):
    return id in (id+id)[1:-1]

with open('document.txt', 'r') as df:
    for data in df:
        data = data.split(',')

    for r in data:
        start, end = r.split('-', 1)
        start = int(start)
        end = int(end)

        for id in range(start,end+1):
            id = str(id)
            if is_repeated_pattern(id) == True:
                invalid_id += int(id)
print(invalid_id)
