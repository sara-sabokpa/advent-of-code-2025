best_combination = []
with open('document.txt') as df:
    bank_list = [line.strip() for line in df]

    for bank in bank_list:
        voltage_list = list(map(int,bank))
        best = 0
        n = len(voltage_list)
        for i in range(n-1):
            first = voltage_list[i]
            second = max(voltage_list[i+1:])
            candidate = first*10 + second
            if candidate > best:
                best = candidate
        best_combination.append(best)

total = sum(best_combination)
print(total)

       
    
