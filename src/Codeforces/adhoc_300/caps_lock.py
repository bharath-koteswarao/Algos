if __name__ == '__main__':
    st = input().strip()
    if st.isupper() or st[1:].isupper() or len(st) == 1:
        for x in st:
            print(x.lower() if x.isupper() else x.upper(), end="")
    else:
        print(st)
