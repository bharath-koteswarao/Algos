import heapq as hp

if __name__ == "__main__":
    heap = []
    tc = input().split(" ")
    tc = int(tc[0])
    for i in range(tc):
        inp = input().split(" ")
        flag = int(inp[0])
        if flag is 1:
            number = int(inp[1])
            heap.append(number)
            hp.heapify(heap)
        elif flag is 2:
            number = int(inp[1])
            heap.remove(number)
        else:
            print(heap[0])

