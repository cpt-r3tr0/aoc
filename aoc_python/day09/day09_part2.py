


def disk_fragment(filename):
    data = []
    with open(filename, "r") as f:
        data = list(map(int, f.read().strip()))

    files = {}
    spaces = []
    ptr = 0
    for i, size in enumerate(data):
        if i % 2 == 0:
            files[i // 2] = (ptr, size)
        else:
            spaces.append((ptr, size))
        ptr += size

    for fid in reversed(files):
        loc, file_size = files[fid]
        space_id = 0
        while space_id < len(spaces):
            space_loc, space_size = spaces[space_id]
            if space_loc > loc:
                break
            if space_size == file_size:
                files[fid] = (space_loc, file_size)
                spaces.pop(space_id)
                break
            if space_size > file_size:
                files[fid] = (space_loc, file_size)
                spaces[space_id] = (space_loc + file_size, space_size - file_size)
                break
            space_id += 1

    part2 = 0
    for fid, (loc, size) in files.items():
        for i in range(loc, loc + size):
            part2 += fid * i
    print(f"Part 2: {part2}")



if __name__ == "__main__":
    disk_fragment("day09_input.txt")