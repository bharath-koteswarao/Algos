if __name__ == '__main__':
    for _ in range(int(input().strip())):
        st = list(input().strip())
        l, u, d = [], [], []
        for i in range(len(st)):
            if st[i].isupper():
                u.append(i)
            elif st[i].islower():
                l.append(i)
            else:
                d.append(i)
        if len(l) > 0 and len(u) > 0 and len(d) > 0:
            print(''.join(st))
        else:
            if len(l) > 0 and len(u) > 0:
                if len(l) > 1:
                    st[l[0]] = '1'
                else:
                    st[u[0]] = '1'
            elif len(u) > 0 and len(d) > 0:
                if len(u) > 1:
                    st[u[0]] = 'a'
                else:
                    st[d[0]] = 'a'
            elif len(l) > 0 and len(d) > 0:
                if len(l) > 1:
                    st[l[0]] = 'A'
                else:
                    st[d[0]] = 'A'
            elif len(l) > 0:
                st[l[0]] = 'A'
                st[l[1]] = '1'
            elif len(u) > 0:
                st[u[0]] = 'a'
                st[u[1]] = '1'
            else:
                st[d[0]] = 'A'
                st[d[1]] = 'a'
            print(''.join(st))
