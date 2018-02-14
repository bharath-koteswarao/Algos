if __name__ == '__main__':
    dic = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }
    for _ in range(int(input().strip())):
        n = int(input().strip())
        if n in dic:
            print(dic[n])
        else:
            a = n % 10
            p = (n // 10) * 10
            print(dic[p] + "-" + dic[a])
