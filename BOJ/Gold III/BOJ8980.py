#BOJ8980 택배 20210505
import sys
input = sys.stdin.readline

def main():
    n,c = map(int, input().rstrip().split())
    m = int(input())
    li = [[] for _ in range(n+1)]
    for _ in range(m):
        s,e,box = map(int,input().rstrip().split())
        li[s].append([e,box])
    for v in li:
        v.sort(key = lambda x: (x[0],x[1]))

    truck = 0
    drop = [0] * (n+1)
    ans = 0
    for town in range(1,n+1):
        ans += drop[town]
        truck -= drop[town]
        for e,box in li[town]:
            leftSpace = c - truck
            if leftSpace >= box:
                capacity = box
            else:
                cantCarry = box - leftSpace
                
                for i in range(n,e,-1):
                    if drop[i] >= cantCarry:
                        drop[i] -= cantCarry
                        truck -= cantCarry
                        cantCarry = 0
                        break
                    else:
                        cantCarry -= drop[i]
                        truck -= drop[i]
                        drop[i] = 0
                capacity = box - cantCarry
            truck += capacity
            drop[e] += capacity
    print(ans)
if __name__ == '__main__':
    main()