

if __name__ == '__main__':
    file1 = open('readfile.txt')
    s = file1.read()
    print(s)
    numA, numB, numC = 0, 0, 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'A':
            numA += 1
        elif s[i] == 'B':
            numB += 1
        elif s[i] == 'C':
            numC += 1
        
        
        if numA >= 1 and numB >= 1 and numC >= 1:
            numA -= 1
            numB -= 1
            numC -= 1
        ans = max(numA, numB, numC, ans)
        # if numA == numB and numB == numC:
        #     numA = 0
        #     numB = 0
        #     numC = 0
            
    print(ans)
        
        