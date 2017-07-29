import time

#input the string and the sub string
string=input("enter the string: ")
substring=input("enter the sub string to be searched: ")

def brute(text,pattern):
    for i in range(len(text)-len(pattern)+1):
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
        if j+1 == len(pattern):
            print('match found bro!')
            return 0
    print('match not found bro!')
    return 0

#time taken for searching
start=time.time()

brute(string,substring)

end=time.time()

print("----this program took %f secs to complete----"%(end-start))
