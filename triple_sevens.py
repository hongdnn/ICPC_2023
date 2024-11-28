if __name__ == '__main__':
    length = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr3 = list(map(int, input().split()))
        
    if 7 in arr1 and 7 in arr2 and 7 in arr3:
        print(777)
    else:
        print(0)