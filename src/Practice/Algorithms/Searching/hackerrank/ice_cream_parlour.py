if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        n = int(input().strip())
        input()
        costs = [int(i) for i in input().strip().split(" ")]
        dic = {}
        for ind, ele in enumerate(costs):
            if ele in dic:
                dic[ele].append(ind)
            else:
                dic[ele] = [ind]
        should_proceed = True
        for i in range(len(costs)):
            if should_proceed:
                if costs[i] < n:
                    required = n - costs[i]
                    if required in dic:
                        positions = dic[required]
                        for j in positions:
                            if j != i:
                                print(i + 1, j + 1)
                                should_proceed = False
                                break
            else:
                break
