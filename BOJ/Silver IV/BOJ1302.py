#BOJ1302 베스트셀러 20210205
import sys
input = sys.stdin.readline

def main():
    dic = {}
    for _ in range(int(input().rstrip())):
        s = input().rstrip()
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    dic = sorted(dic.items(), key = lambda x: (-x[1],x[0]))
    print(dic[0][0])
if __name__ == '__main__':
    main()