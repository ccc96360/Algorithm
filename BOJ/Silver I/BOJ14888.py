#BOJ14888 연산자 끼워넣기 20210304
import sys
from itertools import permutations
input = sys.stdin.readline

def calc(nums, operators):
    ret = nums[0]
    n = len(operators)
    for i in range(n):
        o = operators[i]
        operand = nums[i+1]
        exp = ""
        if o == "//" and ret < 0:
            exp = "-1 * ("+str(abs(ret))+o+str(operand)+")"
        else:
            exp = str(ret)+o+str(operand)
        ret = eval(exp)
    return ret

def main():
    n = int(input())
    nums = list(map(int,input().rstrip().split()))
    li = list(map(int, input().rstrip().split()))
    o = ["+","-","*","//"]
    li2 = []
    for i in range(4):
        for j in range(li[i]):
            li2.append(o[i])
    max_ = -1000000000
    min_ = 1000000000
    dic = set()
    for v in permutations(li2):
        if v in dic: continue
        dic.add(v)
        t = calc(nums, v)
        max_ = max(t, max_)
        min_ = min(t, min_)
    print(max_,min_,sep="\n")
if __name__ == '__main__':
    main()