#BOJ2818 숙제하기 싫을 때 20210118
class Dice:
    def __init__(self):
        self.cur = 1
        self.left = 4
        self.right = 3
        self.down = 2
        self.up = 5
        self.rev = 6
    def moveRight(self):
        tmp = self.cur
        self.cur, self.left, self.rev, self.right = self.left, self.rev, self.right, tmp
    def moveLeft(self):
        tmp = self.cur
        self.cur, self.right,self.rev, self.left = self.right, self.rev, self.left, tmp
    def moveDown(self):
        tmp = self.cur
        self.cur, self.up, self.rev, self.down = self.up, self.rev, self.down, tmp
        
def main():
    r,c = map(int, input().split(" "))
    dice = Dice()
    res = 0
    for i in range(r):
        sum = dice.left + dice.cur + dice.right + dice.rev
        res += sum * (c//4)
        for j in range(c%4):
            res += dice.cur
            if i % 2 == 0 and j != c%4 - 1:
                dice.moveRight()
            elif j != c%4 - 1:
                dice.moveLeft()
        dice.moveDown()

    print(res)
if __name__ == '__main__':
    main()