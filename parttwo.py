def binary2int(binary):
    int_val, i, n = 0, 0, 0
    while(binary != 0):
        a = binary % 10
        int_val = int_val + a * pow(2, i)
        binary = binary//10
        i += 1
    return int_val

def calculator(data, oc):
    for pos in range(len(data[0])):
        count = sum(1 for line in data if line[pos] == '1')
        if oc: bit = '1' if count >= len(data) - count else '0'
        else: bit = '1' if count < len(data) - count else '0'
        data = [i for i in data if i[pos] == bit]
        if len(data) == 1: return int(data[0])

def main():
    with open("input") as f:
        data = [i.strip() for i in f.readlines()]

    oxygen_rate = calculator(data, 1)
    CO2_rate = calculator(data, 0)

    print(f"Oxygen rate: {oxygen_rate}, CO2 rate: {CO2_rate}")
    print(f"Final answer: {binary2int(oxygen_rate) * binary2int(CO2_rate)}")

if __name__=="__main__":
    main()
