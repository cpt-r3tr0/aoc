import re
from dataclasses import dataclass
from functools import lru_cache

@dataclass(frozen=True)
class Connection:
    ins: tuple[str, str]  # Changed to tuple for immutability
    op: str
    out: str

    def __str__(self) -> str:
        return f"{self.out} = {self.ins[0]} {self.op} {self.ins[1]}"

operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2,
}

def solve_puzzle_p1(filename: str) -> int:
    # Read file once and store content
    with open(filename) as f:
        data = f.read()

    # Parse initial values
    init = {k: int(v) for k, v in re.findall(r"(.{3}): ([01])", data)}
    
    # Parse wire map
    wire_map = {}
    for line in data.split("\n\n")[1].splitlines():
        in1, op, in2, _, out = line.strip().split()
        wire_map[out] = Connection(ins=(in1, in2), op=op, out=out)

    @lru_cache(maxsize=None)
    def evaluate_wire(w: str) -> int:
        """Evaluates the value of a wire with memoization."""
        if w in init:
            return init[w]
        conn = wire_map[w]
        return operations[conn.op](
            evaluate_wire(conn.ins[0]), 
            evaluate_wire(conn.ins[1])
        )

    # Get all z-wires, sort them, and evaluate
    z_wires = sorted(
        (w for w in wire_map if w.startswith('z')), 
        reverse=True
    )
    result = ''.join(str(evaluate_wire(w)) for w in z_wires)
    
    return int(result, 2)

if __name__ == "__main__":
    for filename in ["example.txt", "day24_input.txt"]:
        print(f'Solution for {filename} is: {solve_puzzle_p1(filename)}')
