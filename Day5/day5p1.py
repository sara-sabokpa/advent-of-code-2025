with open('document.txt') as df:
    lines = [line.rstrip() for line in df if line.strip()]

    ingredient_ids = [] 
    fresh_ranges = []
    fresh_count = 0


    for line in lines:
        if '-' in line:
            fresh_ranges.append(line)
        else:
            ingredient_ids.append(int(line))


     
    for num in ingredient_ids:
        for r in fresh_ranges:
            start, end = list(map(int, r.split('-')))                   
            if start <= num <= end:
                fresh_count += 1
                break            
print(fresh_count)
