#BOJ10828 스택 20210130
import sys
input = sys.stdin.readline

class Stack:
    def __init__(self):
        self.element = []
        self.stackSize = 0

    def push(self, x):
        self.element.append(x)
        self.stackSize += 1

    def pop(self):
        if self.element:
            print(self.element.pop())
            self.stackSize -= 1
        else:
            print(-1)

    def size(self):
        print(self.stackSize)

    def empty(self):
        print(0 if self.element else 1)

    def top(self):
        if self.element:
            print(self.element[-1])
        else:
            print(-1)

    def operate(self, args):
        if len(args) == 2:
            return{
                "push" : self.push
            }[args[0]](int(args[1]))
        else:
            return{
                "pop" : self.pop,
                "size" : self.size,
                "empty" : self.empty,
                "top" : self.top,
            }[args[0]]()
def main():
    s = Stack()
    for _ in range(int(input())):
        ins = input().rsplit()
        s.operate(ins)
if __name__ == '__main__':
    main()