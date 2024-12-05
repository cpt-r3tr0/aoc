import re
def process_multiplication(filename) -> int:
    with open(filename, 'r') as file:
        content = file.read()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.finditer(pattern, content)
    
    total = 0
    for match in matches:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        total += num1 * num2
        # print(f"Found multiplication: {num1} * {num2} = {num1 * num2}")
    
    return total



filename = "day3_input.txt"
result = process_multiplication(filename)
print(f"The multiplication of the numbers is: {result}")