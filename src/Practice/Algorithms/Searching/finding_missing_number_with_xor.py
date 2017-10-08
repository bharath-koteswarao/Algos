if __name__ == '__main__':
    inp = [int(i) for i in input("Give Input array : ").strip().split(" ")]
    required_length = len(inp) + 1
    xor_1 = 0
    for i in range(1,required_length+1):
        xor_1 ^= i
    xor_2 = 0
    for i in inp:
        xor_2 ^= i
    print("Missing element :",xor_1^xor_2)