def b2int(b):
    v, i, n = 0, 0, 0
    while(b != 0):
        v = v + (b % 10) * pow(2, i)
        b, i = b//10, i + 1
    return v
def calculator(d, w):
    for p in range(len(d[0])):
        c = sum(1 for l in d if l[p] == '1')
        if w: b = '1' if c >= len(d) - c else '0'
        else: b = '1' if c < len(d) - c else '0'
        d = [i for i in d if i[p] == b]
        if len(d) == 1: return int(d[0])
def main():
    with open("input") as f: d = [i.strip() for i in f.readlines()]
    oxygen_rate, CO2_rate = calculator(d, 1), calculator(d, 0)
    print(f"Oxygen rate: {oxygen_rate}, CO2 rate: {CO2_rate}\nFinal answer: {b2int(oxygen_rate) * b2int(CO2_rate)}")
if __name__=="__main__": main()
