import sys
from collections import deque
input = sys.stdin.readline

def step3(q):
    stack = [q.popleft()]
    while q:
        s = q.popleft()
        if not(stack[-1] == "." and s == "."):
            stack.append(s)
    return "".join(stack)

canUse = [chr(i) for i in range(ord("a"),ord("z")+1)] +  [str(i) for i in range(10)] + ["-","_","."]
def solution(new_id:str):
    #step1
    new_id = new_id.lower()
    #step2
    new_id = "".join(list(filter(lambda x: x in canUse, new_id)))
    #step3
    new_id = step3(deque(new_id))
    #step4
    if new_id != "" and new_id[0] == ".": new_id = new_id[1:]
    if new_id != "" and new_id[-1] == ".": new_id = new_id[:-1]
    #step5
    if new_id == "": new_id = "a"
    #step6
    size = len(new_id)
    if size >= 16: 
        new_id = new_id[:15]
        if new_id[-1] == ".": new_id = new_id[:-1]
    #step7
    if size <= 2:
        while size < 3:
            new_id += new_id[-1]
            size += 1
    return new_id
def main():
    print(solution(input().rstrip()))
if __name__ == '__main__':
    main()