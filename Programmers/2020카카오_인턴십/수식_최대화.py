from itertools import permutations
from copy import deepcopy
def operate(a, b, op):
    if op == "+":
        ret = a + b
    elif op == "-":
        ret = a-b
    else:
        ret = a*b
    return ret

def solution(expression):
    answer = 0
    tmp = ""
    li = []
    for v in expression:
        if v not in ["*","-","+"]:
            tmp += v
        else:
            li.append(int(tmp))
            li.append(v)
            tmp = ""
    li.append(int(tmp))
    
    for v in permutations(["+","*","-"],3):
        stack = deepcopy(li)
        for op in v:
            stack2 = []
            i = 0
            while i < len(stack):
                if stack[i] == op:
                    a = stack2.pop()
                    i += 1
                    b = stack[i]
                    stack2.append(operate(a, b, op))
                else:
                    stack2.append(stack[i])
                i += 1
            stack = deepcopy(stack2)
        answer = max(answer, abs(stack[0]))
    return answer

asd = ""
print(solution(input().rstrip()))