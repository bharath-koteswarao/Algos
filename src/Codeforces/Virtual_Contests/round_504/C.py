if __name__ == '__main__':
    pairs = []
    n, k = [int(__) for __ in input().strip().split()]
    inp = input().strip()
    st = []
    for i in range(len(inp)):
        if inp[i] == '(':
            st.append(i)
        else:
            re = st.pop()
            pairs.append((re, i))
    pairs.sort(key=lambda x: (x[0], x[1]))
    print(pairs)

