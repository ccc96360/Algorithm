from itertools import combinations

def solution(orders, course):
    answer = []
    cnts = {i : {} for i in range(2,11)}
    for v in orders:
        li = list(v)
        for i in range(2,len(v)+1):
            for case in combinations(li,i):
                case = sorted(list(case))
                s = "".join(case)
               
                if s not in cnts[i]:
                    cnts[i][s] = 1
                else:
                    cnts[i][s] += 1
    for i in course:
        li = list(cnts[i].items())
        li.sort(key = lambda x: x[1], reverse = True)
        if li:
            mx = li[0][1]
            for k, v in li:
                if v >= 2 and v == mx:
                    answer.append(k)
    
    answer.sort()
    return answer


def main():
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))
if __name__ == '__main__':
    main()