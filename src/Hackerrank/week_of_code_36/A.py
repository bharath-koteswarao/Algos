if __name__ == '__main__':
    for _ in range(int(input().strip())):
        inp = input().strip()
        if inp.startswith('hydro') and inp.endswith('ic'):
            print('non-metal acid')
        elif inp.endswith('ic'):
            print('polyatomic acid')
        else:
            print('not an acid')
