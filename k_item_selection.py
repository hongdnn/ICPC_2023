def countBehavior(n: int, m: int, s: int, preSelected: list, wanted: list) -> int:
    if not preSelected and not wanted:
        return 0
    
    count = 0
    pages = {}
    deselects = {}
    totalPages = int(n / m) + 1 if n % m > 0 else int(n / m)
    firstPage = totalPages
    lastPage = 1
    for num in wanted:
        if num in preSelected:
            continue
        page = int(num / m) + 1 if num % m > 0 else int(num / m)
        firstPage = min(page, firstPage)
        lastPage = max(page, lastPage)
        if page not in pages:
            pages[page] = []
        pages[page].append(num)
        
    print(pages)
    
    for num in preSelected:
        if num in wanted:
            continue
        deselectPage = int(num / m) + 1 if num % m > 0 else int(num / m)
        firstPage = min(deselectPage, firstPage)
        lastPage = max(deselectPage, lastPage)
        if deselectPage not in deselects:
            deselects[deselectPage] = []
        deselects[deselectPage].append(num)
        
    print(deselects)
    
    if not pages and not deselects:
        return 0
    
    startPage = firstPage if firstPage - s < lastPage - s else lastPage
    
    if s != startPage:
        i = 1 if s < startPage else - 1
        while s != startPage:
            wantedItems = len(pages[s]) if s in pages else 0
            if wantedItems == m:
                count += 1
            elif wantedItems > m // 2:
                count += 1 + m - wantedItems
            else:
                deselectItems = len(deselects[s]) if s in deselects else 0
                count += wantedItems + 1 if deselectItems > m // 2 else wantedItems + deselectItems                
            if s in pages:
                del pages[s]
            if s in deselects:
                del deselects[s]
            
            s += i
            count += 1
    
    print(count)

    if pages or deselects:
        end = 0 if startPage == lastPage else totalPages + 1
        step = -1 if startPage == lastPage else 1
        for i in range(startPage, end, step):
            wantedItems = len(pages[i]) if i in pages else 0
            if wantedItems == m:
                count += 1
            elif wantedItems > m // 2:
                count += 1 + m - wantedItems
            else:
                deselectItems = len(deselects[i]) if i in deselects else 0
                count += wantedItems + 1 if deselectItems > m // 2 else wantedItems + deselectItems               
            if i in pages:
                del pages[i]
            if i in deselects:
                del deselects[i]
            if not pages and not deselects:
                break
            if i < totalPages:
                count += 1

            
    return count
    



if __name__ == '__main__':
    n, m,s,p, q = map(int, input().split())
    preSelected = []
    wanted = []
    for _ in range(p):
        preSelected.append(int(input()))
    for _ in range(q):
        wanted.append(int(input()))
    result = countBehavior(n, m ,s, preSelected, wanted)
    print('Total button clicked:', result)