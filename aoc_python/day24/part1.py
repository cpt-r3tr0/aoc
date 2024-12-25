
import re
from dataclasses import dataclass


init = {}
wire_map = {}
@dataclass
class Connection:
    ins: list[str]
    op: str
    out: str

    def __str__(self) -> str:
        return f"{self.out} = {self.ins[0]} {self.op} {self.ins[1]}"
    
    def __eq__(self, other) -> bool:
        return self.ins == other.ins and self.op == other.op


operations = {
    "OR": lambda x1, x2: x1 | x2,
    "AND": lambda x1, x2: x1 & x2,
    "XOR": lambda x1, x2: x1 ^ x2,
}


def run_wire(w: str) -> int:
    if w in init:
        return init[w]
    conn = wire_map[w]
    return operations[conn.op](run_wire(conn.ins[0]), run_wire(conn.ins[1]))


def solve_puzzle_p1(filename):
    data = ""
    global init
    global wire_map
    with open(filename, "r") as f:
        data = f.read()
    init_pairs = re.findall(r"(.{3}): ([01])", data)

    
    init = {k: int(v) for k, v in init_pairs}
    map_str = data.split("\n\n")[1].splitlines()

    wire_map = {}
    for line in map_str:
        in1, op, in2, _, out = line.strip().split(' ')
        wire_map[out] = Connection([in1, in2], op, out)
    
    result = [run_wire(w) for w in sorted([w for w in wire_map if w.startswith("z")], reverse=True)]
    return int(''.join(map(str, result)), 2)

if __name__ == "__main__":
    filename = "example.txt"
    print(f'Solution for example file is : {solve_puzzle_p1(filename)}')
    filename = "day24_input.txt"
    print(f'Solution for my file is : {solve_puzzle_p1(filename)}')

