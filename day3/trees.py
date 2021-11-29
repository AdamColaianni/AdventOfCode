def pass_across_and_down(a, d=1):
    position, empty, tree = 0, 0, 0
    with open("input") as f:
        input = [line.strip() for line in f.readlines()]
    for i, v in enumerate(input):
        if i % d == 0:
            if v[position] == ".": empty += 1
            elif v[position] == "#": tree += 1
            position = (position + a) % 31
    return tree
