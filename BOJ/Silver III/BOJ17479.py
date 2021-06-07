#BOJ17479 정식당 20210607
import sys
input = sys.stdin.readline

def main():
    a,b,c = map(int, input().rstrip().split())
    normal = {}
    special = {}
    for _ in range(a):
        k,v = input().rstrip().split()
        normal[k] = int(v)
    for _ in range(b):
        k,v = input().rstrip().split()
        special[k] = int(v)
    service = set([input().rstrip() for _ in range(c)])

    normalCost = specialCost = 0
    orderService = 0
    for _ in range(int(input())):
        s = input().rstrip()
        if s in normal:
            normalCost += normal[s]
        elif s in special:
            specialCost += special[s]

        elif s in service:
            orderService += 1

    if (specialCost > 0 and normalCost < 20000) or (orderService >= 1 and normalCost + specialCost < 50000) or orderService >= 2:
        print("No")
    else:
        print("Okay")
if __name__ == '__main__':
    main()