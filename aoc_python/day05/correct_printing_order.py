def correct_printing_order(filename)-> int:

    with open(filename) as file:
        rule_set , updates = file.read().strip().split("\n\n")
        rules = []
        for line in rule_set.split("\n"):
            a,b = line.split("|")
            rules.append((int(a), int(b)))
        updates = [list(map(int, line.split(","))) for line in updates.split("\n")]

        # print(f'rules: {rules}\nupdates: {updates}\n\n')
        count = 0
        mid_points = 0
        for update in updates:
            # print(f'checking update {update}')
            good, mid = follows_rules(rules, update)
            if good:
                # print(f'calling the function follows_rules with rules: {rules} and update: {update}')
                # print(f'update: {update} follows rules')
                count += 1
                mid_points += mid
        print(f'count: {count} mid_points: {mid_points}')
        return count


def follows_rules(rules, update):
    # print(f'checking if update {update} follows rules {rules}')
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    for a,b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            # print(f'rule {a} {b} not followed')
            return False, 0
    return True, update[len(update)//2]

if __name__ == "__main__":
    filename = "day05_input.txt"
    example = "test.txt"
    
    print(f'Part 1 example input : {correct_printing_order(example)}')
    print(f'Part 1 actual input : {correct_printing_order(filename)}')