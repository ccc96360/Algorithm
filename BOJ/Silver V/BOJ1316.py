#BOJ1316 그룹 단어 체커 20210124
NOT_EXIST = 0
CONTINUE = 1
EXIST = 2
def main():
    res = 0
    for _ in range(int(input())):
        dic = {chr(i) : NOT_EXIST for i in range(ord("a"), ord("z")+1)}
        word = input()
        prev = word[0]
        dic[prev] = CONTINUE
        for i in range(1,len(word)):
            s = word[i]
            if dic[s] == NOT_EXIST:
                dic[s] = CONTINUE
                dic[prev] = EXIST
                prev = s
            elif dic[s] == CONTINUE:
                if prev != s:
                    res -= 1
                    break
            elif dic[s] == EXIST:
                res -= 1
                break
        res += 1
    print(res)
if __name__ == '__main__':
    main()