arrow = 50
count = 0

with open('document.txt', 'r') as rf:

    for line in rf:
        line =line.strip()
        amount = int(line[1:])
        if line.startswith('R'):
            arrow = (arrow + amount)%100
        elif line.startswith('L'): 
            arrow = (arrow - amount)%100
        if arrow == 0:
            count += 1
print("The password is:",count)




