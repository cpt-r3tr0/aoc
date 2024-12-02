def calculate_similarity_score(filename):
    left = []
    right = []
    with open(filename) as file:
        for line in file:
            numbers = [x for x in line.strip().split(' ') if x]
            left.append(int(numbers[0]))
            right.append(int(numbers[1]))
    total_score = 0
    for left_num in left:
        # Count how many times this number appears in right_numbers
        frequency = right.count(left_num)
        # Multiply the number by its frequency and add to total
        total_score += left_num * frequency

    return total_score

filename = "day1_input.txt"
result = calculate_similarity_score(filename)
print(f"The similarity score is: {result}")