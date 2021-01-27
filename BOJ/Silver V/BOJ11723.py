#BOJ11723 집합 20210127
import sys
class Set:
    def __init__(self ):
        self.element = [False] * 21
    def add(self, n):
        self.element[n] = True
    def remove(self, n):
        self.element[n] = False
    def check(self, n):
        print(1) if self.element[n] else print(0)
    def toggle(self, n):
        self.element[n] = not self.element[n]
    def all(self):
        self.element = [True] * 21
    def empty(self):
        self.element = [False] * 21
    def operate(self, args):
        if len(args) == 2:
            return {
                "add" : self.add,
                "remove" : self.remove,
                "check" : self.check,
                "toggle" : self.toggle
            }[args[0]](int(args[1]))
        else:
            return{
                "all" : self.all,
                "empty" : self.empty
            }[args[0]]()
def main():
    mSet = Set()
    for _ in range(int(input())):
        ins = sys.stdin.readline().rsplit()
        mSet.operate(ins)
if __name__ == '__main__':
    main()