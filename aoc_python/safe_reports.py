def is_safe(numbers):
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i + 1])
        if diff < 1 or diff > 3:
            return False
    is_increasing = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    is_decreasing = all(numbers[i] >= numbers[i + 1] for i in range(len(numbers) - 1))
    return is_increasing or is_decreasing

def compute_safe_reports(filename):
    safe_files = 0
    with open(filename, "r") as file:
        for line in file:
            numbers = [int(x) for x in line.split()]
            if is_safe(numbers):
                safe_files += 1
    return safe_files


filename = "day2_input.txt"
result = compute_safe_reports(filename)
print(f"The safe reports are: {result}")