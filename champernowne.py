def test(n: int) -> int:
    
    nString = str(n)
    x = int(nString[0])
    count = 1
    i = 1
    while(i < len(nString)):
        t = int(nString[i])
        while(len(str(t)) < len(str(x)) and i < len(nString) - 1):
            i += 1
            t = t * 10 + int(nString[i])
        if t == x + 1:
            x = t
            count += 1
        else:
            if i < len(nString) - 1:
                i += 1
                t = t * 10 + int(nString[i])
            if t == x + 1:
                x = t
                count += 1
            else:
                return -1
        i += 1
                
    return count


print(test(1234567891011))