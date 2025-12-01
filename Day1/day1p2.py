arrow = 50
count = 0

with open('document.txt', 'r') as rf:

    for line in rf:
        line =line.strip()
        amount = int(line[1:])
        if line.startswith('R'):
            crosses = (arrow + amount)//100
            arrow = (arrow + amount)%100
        
        elif line.startswith('L'): 
            inverted_arrow = (100 - arrow)%100
            crosses = (inverted_arrow + amount)//100
            arrow = (arrow - amount)%100
        count += crosses
print("The password is:",count)
