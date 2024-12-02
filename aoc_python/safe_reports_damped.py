def is_safe_report(numbers):
    # Check if adjacent numbers differ by 1-3
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < 1 or diff > 3:
            return False
    
    # Check if sequence is strictly increasing or decreasing
    is_increasing = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))
    
    return is_increasing or is_decreasing

def is_safe_with_dampener(numbers):
    # First check if it's safe without dampener
    if is_safe_report(numbers):
        return True
    
    # Try removing each number one at a time
    for i in range(len(numbers)):
        # Create new list without current number
        dampened_numbers = numbers[:i] + numbers[i+1:]
        if is_safe_report(dampened_numbers):
            return True
    
    return False

def count_safe_reports(filename):
    safe_count = 0
    
    with open(filename, 'r') as file:
        for line in file:
            # Split the line on whitespace and convert to integers
            numbers = [int(x) for x in line.strip().split()]
            if is_safe_with_dampener(numbers):
                safe_count += 1
    
    return safe_count

# Process the file
filename = "day2_input.txt"
result = count_safe_reports(filename)
print(f"Number of safe reports with Problem Dampener: {result}")
