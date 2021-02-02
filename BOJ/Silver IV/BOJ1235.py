#BOJ1235 학생 번호 20210203 
import sys
input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    li = [input().rstrip() for _ in range(n)]
    n = len(li[0])
    res = 0
    for i in range(n):
        res += 1
        dic = {}
        flag = True
        for s in li:
            if s[-1*(i+1):] in dic:
                flag = False
                break
            else:
                dic[s[-1*(i+1):]] = 0
        if flag: break
    print(res)
if __name__ == '__main__':
    main()