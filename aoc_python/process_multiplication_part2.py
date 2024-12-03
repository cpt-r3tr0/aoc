import re

def process_multiplication(filename) -> int:
    # Read the file content
    with open(filename, 'r') as file:
        content = file.read()
    
    # Pattern to match valid mul(number,number), do(), and don't() instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Split the content into a sequence of instructions
    total = 0
    enabled = True  # mul instructions are enabled at the start
    
    # Find all instruction positions and types
    instructions = []
    
    # Find all mul instructions
    for match in re.finditer(mul_pattern, content):
        instructions.append(('mul', match.start(), match))
    
    # Find all do() instructions
    for match in re.finditer(do_pattern, content):
        instructions.append(('do', match.start(), None))
    
    # Find all don't() instructions
    for match in re.finditer(dont_pattern, content):
        instructions.append(('dont', match.start(), None))
    
    # Sort instructions by position
    instructions.sort(key=lambda x: x[1])
    
    # Process instructions in order
    for inst_type, _, match in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            result = num1 * num2
            total += result
            # print(f"Found multiplication: {num1} * {num2} = {result}")
    
    return total


filename = "day3_input.txt"
result = process_multiplication(filename)
print(f"The total sum of all valid multiplications is: {result}")
