result = []

with open('document.txt') as df:
    bank_list = [line.strip() for line in df]
    
    for bank in bank_list:
        voltage_list = list(map(int,bank))
        n = len(voltage_list)
        skip_number = n - 12
        stack = []
        
        stack.append(voltage_list[0])

        for v in voltage_list[1:]:

            while stack and skip_number > 0 and v > stack[-1]:
                stack.pop() 
                skip_number -= 1
            stack.append(v)
        
        result.append(int(''.join(map(str,stack[:12]))))
total = sum(result)
print(total)
            
           