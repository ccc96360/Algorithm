#BOJ18511 큰 수 구성하기 20210118  
from itertools import product

def main():
    n, k = map(int, input().split(" "))
    li = list(input().split(" "))
    max = -1; size = len(str(n))
    while True:
        t = list(product(li,repeat=size))
        for i in t:
            tmp = int("".join(i))
            if n >= tmp:
                if max < tmp:
                    max = tmp
        if max == -1: size -= 1
        else: break
    print(max)
if __name__ == '__main__':
    main()
    