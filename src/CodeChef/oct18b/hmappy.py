from heapq import *

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    bal = [int(__) for __ in input().strip().split()]
    cost = [int(__) for __ in input().strip().split()]
    heap = []
    for i in range(n):
        heap.append((-bal[i] * cost[i], cost[i]))
    heapify(heap)
    while k > 0:
        k -= 1
        candies, cost = heappop(heap)
        if candies == 0:
            break
        else:
            candies = abs(candies)
            candies -= cost
            heappush(heap, (-candies, cost))
    cand, cost = heappop(heap)
    print(abs(cand))
