#BOJ16637 괄호 추가하기 20210408
import sys
from itertools import combinations
input = sys.stdin.readline

def validate(nums):
    s = set()
    for v in nums:
        if v[0] in s or v[1] in s:
            return False
        else:
            s.update(v)
    return True

def calculate(li):
    if len(li) == 1: return int(li[0])
    ret = 0
    tmp = []
    for v in li:
        if v in ['*','+','-']:
            operator = v
        else:
            tmp.append(v)
        if len(tmp) == 2:
            ret = eval(operator.join(tmp))
            tmp = [str(ret)]
    
    return ret

def main():
    n = int(input())
    li = list(input().rstrip())
    number = list(combinations([i*2 for i in range(n//2+1)],2))
    number = list(filter(lambda x: abs(x[0]-x[1]) == 2, number))
    maxNum = n // 2 + 1
    maxBracket = maxNum // 2
    max_ = calculate(li)
    for bracket in range(1,maxBracket+1):
        for nums in combinations(number, bracket):
            if not validate(nums): continue
            nums = sorted(list(nums), key = lambda x: x[0])
            tmp = []
            idx = 0
            for v in nums:
                tmp.extend(li[idx:v[0]])
                tmp.append(str(calculate(li[v[0]:v[1]+1])))
                idx = v[1] + 1
            tmp.extend(li[idx:])
            max_ = max(max_, calculate(tmp))
    print(max_)
if __name__ == '__main__':
    main()