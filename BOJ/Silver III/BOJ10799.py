#BOJ10799 쇠 막대기 20210218
import sys
input = sys.stdin.readline

def main():
    str_ = input().rstrip()
    iron = cnt = 0
    before = ""
    for s in str_:
        if s == "(":
            iron += 1
        else:
            iron -= 1
            cnt += iron if before == "(" else 1
        before = s
    print(cnt)
if __name__ == '__main__':
    main()