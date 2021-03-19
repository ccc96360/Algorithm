#BOJ7662 이중 우선순위 큐 20210319
import sys
import heapq as hq
input = sys.stdin.readline

class DualPriorityQ:
    def __init__(self):
        self.mnq = []
        self.mxq = []
        self.cnt= {}
    def push(self, n):
        hq.heappush(self.mnq, n)
        hq.heappush(self.mxq, -n)
        if n not in self.cnt:
            self.cnt[n] = 1
        else:
            self.cnt[n] += 1
    def pop(self,d):
        self.syncAndPop({-1 : self.mnq, 1 : self.mxq}[d],d)
    def syncAndPop(self,q,d):
        while q:
            n = hq.heappop(q) * -d
            if n not in self.cnt: continue
            self.cnt[n] -= 1
            if self.cnt[n] == 0:
                del self.cnt[n]
            break
    def operate(self, cmd, n):
        {"I" : self.push, "D" : self.pop}[cmd](n)
def main():
    for tc in range(int(input())):
        dq = DualPriorityQ()
        for __ in range(int(input())):
            cmd, n = input().rstrip().split()
            dq.operate(cmd,int(n))
        res = sorted([k for k,v in dq.cnt.items()])
        print(f"{res[-1]} {res[0]}" if res else "EMPTY")
if __name__ == '__main__':
    main()