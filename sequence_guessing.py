import random

def sequenceGuessing():
    k = random.randrange(2, 100001)
    print(k)
    num = 0
    arr = [num]
    for _ in range(k - 2):
        num += random.choice([1, 2])
        arr.append(num)
    arr.append(100000)
    
    while True:
        guess = int(input())
        if guess in arr:
            print('index:', arr.index(guess) + 1)
            break
        if guess == -1:
            for n in arr:
                print(n)
            break
        else:
            print(-1)
            

if __name__ == '__main__':
    sequenceGuessing()
    
    
