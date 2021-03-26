#BOJ1620 나는야 포켓몬 마스터 이다솜 20210326
import sys
input = sys.stdin.readline

def main():
    n,m = map(int,input().rstrip().split())
    dic = {}
    li = [0] * (n+1)
    cnt = 1
    for _ in range(n):
        s = input().rstrip()
        dic[s] = cnt
        li[cnt] = s
        cnt += 1
    for _ in range(m):
        s = input().rstrip()
        try:
            num = int(s)
            print(li[num])
        except:
            print(dic[s])
if __name__ == '__main__':
    main() 