def correct_printing_order(filename)-> int:

    with open(filename) as file:
        rule_set , updates = file.read().strip().split("\n\n")
        rules = []
        for line in rule_set.split("\n"):
            a,b = line.split("|")
            rules.append((int(a), int(b)))
        updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

        count = 0
        for update in updates:
  
            if follows_rules(rules, update):
                continue
            corected_update = sort_updates(rules, update)
            count += corected_update[len(corected_update)//2]

        return count

def sort_updates(rules, update):
    while True:
        sorted = True
        for i in range(len(update)-1):
            if (update[i], update[i+1]) in rules:
                update[i], update[i+1] = update[i+1], update[i]
                sorted = False
        if sorted:
            return update


def follows_rules(rules, update):
    # print(f'checking if update {update} follows rules {rules}')
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    for a,b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            # print(f'rule {a} {b} not followed')
            return False
    return True

if __name__ == "__main__":
    filename = "day05_input.txt"
    example = "test.txt"
    
    print(f'Part 2 example input : {correct_printing_order(example)}')
    print(f'Part 2 actual input : {correct_printing_order(filename)}')