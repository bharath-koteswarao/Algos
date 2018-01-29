def cin():
    return input().split(' ')

if __name__ == '__main__':
    n, m = cin()
    n = int(n)
    m = int(m)
    d = {}
    for i in range(n):
        name, ip = cin()
        name = " #" + name
        d[ip] = name

    for i in range(m):
        server, ip = cin()
        print(server + " " + ip + d[ip[:-1]])
