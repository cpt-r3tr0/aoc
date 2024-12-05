def compute_total_distance(filename):
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            numbers = [x for x in line.strip().split(' ') if x]
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    left.sort()
    right.sort()
    
    total_diff = sum(abs(l - r) for l, r in zip(left, right))
    
    return total_diff



filename = 'day1_input.txt'
result = compute_total_distance(filename)
print(f'Result: {result}')