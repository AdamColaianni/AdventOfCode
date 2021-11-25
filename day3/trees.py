def pass_across_and_down(a, d=1):
    position, empty, tree = 0, 0, 0
    with open("input") as f:
        input = f.readlines()
        for i, v in enumerate(input):
            if i % d == 0:
                # Max is 31 places but not 30 because index 0 instead 31 becuase of account for the \n newline
                while position >= 31: position -= 31
                if v[position] == ".": empty += 1
                elif v[position] == "#": tree += 1
                position += a
    return tree

def main():
    x = pass_across_and_down(3)
    print(f"You hit {x} trees")

if __name__=="__main__":
    main()
