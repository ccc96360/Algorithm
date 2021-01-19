#BOJ9324 진짜 메시지 20210119  
def main():
    tc = int(input())
    for __ in range(tc):
        dict = {}
        mes = input()
        fixed = False; fixedS = ""
        res = "OK"
        for s in mes:
            if fixed:
                if fixedS != s:
                    res = "FAKE"
                    break
                else:
                    fixed = False 
                    continue
            if s in dict:
                dict[s] += 1
            else:
                dict[s] = 1
            if dict[s] == 3:
                dict[s] = 0
                fixed = True
                fixedS = s
        print(res if not fixed else "FAKE")
if __name__ == '__main__':
    main()