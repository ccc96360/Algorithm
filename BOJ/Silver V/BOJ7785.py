#BOJ7785 회사에 있는 사람 20210129
import sys
input = sys.stdin.readline

def main():
    dic = {}
    for _ in range(int(input())):
        s, stat = input().rstrip().split(" ")
        dic[s] = stat
    li = []
    for key, value in dic.items():
        if value == "enter": li.append(key)
    li.sort(reverse=True)
    for s in li: print(s)
if __name__ == '__main__':
    main()