#BOJ1244 스위치 켜고 끄기 20210204 
import sys
input = sys.stdin.readline

def main():
    switch = lambda x : (x-1)*-1
    n = int(input().rstrip())
    li = list(map(int, input().rstrip().split(" ")))
    for _ in range(int(input())):
        s, num = map(int,input().rstrip().split(" "))
        if s == 1:
            tmp = num
            while num-1 < n:
                li[num-1] = switch(li[num-1])
                num += tmp
        elif s == 2:
            l = num - 2
            r = num
            li[num-1] = switch(li[num-1])
            while l >= 0 and r < n:
                if li[l] == li[r]:
                    li[l] = switch(li[l])
                    li[r] = switch(li[r])
                    l -= 1
                    r += 1
                else:
                    break
    for i in range(n//20 + 1):
        for j in range(20):
            if i * 20 + j == n: break
            print(li[i*20+j],end=" ")
        print("")
if __name__ == '__main__':
    main()
    