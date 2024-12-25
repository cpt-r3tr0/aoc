def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2

def solve_puzzle_p2(filename):
    wires = {}
    operations = []
    highest_z = "z00"

    # Parse input
    data = open(filename).read().split("\n")
    for line in data:
        if ":" in line:
            wire, value = line.split(": ")
            wires[wire] = int(value)
        elif "->" in line:
            op1, op, op2, _, res = line.split(" ")
            operations.append((op1, op, op2, res))
            if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
                highest_z = res

    # Find suspicious wires
    wrong = set()
    for op1, op, op2, res in operations:
        # Rule 1: z-wires should use XOR except highest z
        if res[0] == "z" and op != "XOR" and res != highest_z:
            wrong.add(res)
        
        # Rule 2: XOR gates with non-standard inputs
        if (op == "XOR" and 
            res[0] not in ["x", "y", "z"] and 
            op1[0] not in ["x", "y", "z"] and 
            op2[0] not in ["x", "y", "z"]):
            wrong.add(res)
        
        # Rule 3: AND gates without x00 input
        if op == "AND" and "x00" not in [op1, op2]:
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop != "OR":
                    wrong.add(res)
        
        # Rule 4: XOR gates feeding into OR gates
        if op == "XOR":
            for subop1, subop, subop2, subres in operations:
                if (res == subop1 or res == subop2) and subop == "OR":
                    wrong.add(res)

    return ",".join(sorted(wrong))

if __name__ == "__main__":
    filename = "day24_input.txt"
    print(f'Part 2 solution: {solve_puzzle_p2(filename)}')
