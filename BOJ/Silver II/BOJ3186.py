#BOJ3186 소변기 20210608
import sys
input = sys.stdin.readline

USING = 1
COMPLETE = 2
def main():
    k,l,n = map(int, input().rstrip().split())
    logs = list(input().rstrip())

    status = COMPLETE
    usingTime = notUsingTime = 0
    time = 0
    ans = []
    for v in logs:
        time += 1
        if status == COMPLETE:
            if v == "1":
                usingTime += 1
                if usingTime >= k:
                    status = USING
                    usingTime = 0
            else:
                usingTime = 0
        else:
            if v == "0":
                notUsingTime += 1
                if notUsingTime >= l:
                    status = COMPLETE
                    ans.append(time)
                    notUsingTime = 0
            else:
                notUsingTime = 0

    if status == USING:
        ans.append(time + l)
    if ans:
        print(*ans, sep='\n')
    else:
        print('NIKAD')
    
if __name__ == '__main__':
    main()