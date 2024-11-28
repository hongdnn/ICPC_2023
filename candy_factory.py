from collections import deque


def getAdditionalCandy(k: int, arr: list[int]):
    
    # get the highest k number of candies
    arr.sort()
    pack = deque([])
    for _ in range(k):
        pack.appendleft(arr.pop())
        
    maxNum = pack[-1]
    
    # add remaining candies from arr to pack (except the highest candies at index -1)
    i = 0
    arrTotal = sum(arr)
    while i < len(pack) - 1 and arrTotal > 0:
        if pack[i] < maxNum:
            addCandies = min(maxNum - pack[i], arrTotal)
            pack[i] += addCandies
            arrTotal -= addCandies
        i += 1
    
    print(pack)
    print(arrTotal)
    
    # get the remaining candies in pack (if the number of each type of candies in packs are different)
    remain = 0
    for num in pack:
        remain += maxNum - num
    
    # if there is no candy left in arr (they already put into pack)
    if arrTotal == 0:
        return remain
    # otherwise, get all redundant candies from pack and arr, then modulo k
    else:
        remain += arrTotal
        redundant = remain % k
        print('redundant',redundant)
        ans = 0 if redundant == 0 else k - redundant
        return ans
    
        
    
    
    # maxNum = pack[-1]
    # i = 0
    # while arr:
    #     pack[i] += arr.pop()
    #     if pack[i] > maxNum:
    #         maxNum = pack[i]
    #     i += 1
    #     if i == len(pack):
    #         i = 0

    # print(pack)
    # ans = 0
    # for num in pack:

    #     ans += maxNum - num
    
    # return ans
if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    res = getAdditionalCandy(k, arr)
    print(res)    