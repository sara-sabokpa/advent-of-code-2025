
with open('document.txt') as df:
    output_file = df.readlines()
    output_file = [line.strip('\n') for line in output_file]


    rows = len(output_file)
    cols = len(output_file[0])
    result = 0
    neighbors = [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1), (1,0), (1,1)
    ]

    change = 1
    while change == 1:
        change = 0
        for r in range(rows):
            for c in range(cols):  
                if output_file[r][c] == '@':
                    count = 0
                    for dr, dc in neighbors:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if output_file[nr][nc] == '@':
                                count += 1
                    if count < 4:
                        change = 1
                        result += 1
                        output_file[r] = (
                            output_file[r][:c] + '.' + output_file[r][c+1:]
                        )        
print(result)

