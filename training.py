



if __name__ == '__main__':
    n, s = map(int, input().split())
    for _ in range(n):
        minL, maxL = map(int, input().split())
        if minL <= s <= maxL:
            s += 1
            
    print(s)