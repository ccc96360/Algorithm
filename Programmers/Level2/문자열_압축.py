def solution(s):
    n = len(s)
    answer = n
    for i in range(1, n+1):
        front = s[:i]
        cnt = 1
        idx = i
        li = []
        for idx in range(i, n, i):
            curStr = s[idx:idx+i]
            if front == curStr:
                cnt += 1
            else:
                tmp = (str(cnt) + front) if cnt > 1 else front
                li.append(tmp)
                cnt = 1
                front = curStr
        li.append((str(cnt) + front) if cnt > 1 else front)
        res = "".join(li)
        answer = min(answer, len(res))
    return answer

def main():
    s = "xababcdcdababcdcd"
    print(solution(s))
if __name__ == '__main__':
    main()