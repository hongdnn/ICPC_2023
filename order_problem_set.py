def test(n: int, arr: list):
    res = []
    for i in range(2, n+1):
        if n % i == 0:
            length = n // i
            
            check = True
            
            left, right = 0, length
            
            while left + length <= n and right + length <= n:
                maxNum = max(arr[left:left+length])
                minNum = min(arr[right:right+length])
                if maxNum > minNum:
                    check = False
                    break
                left += length
                right += length
                
            if check:
                res.append(i)
    
    print(res)
    return res            
                    
if __name__ == '__main__':
    test(6, [6,5,4,3,2,1])