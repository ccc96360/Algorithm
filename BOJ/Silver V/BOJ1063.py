#BOJ1063 킹 20210123
class Piece:
    def __init__(self, pos):
        self.x = ord(pos[0]) - ord("A")
        self.y = int(pos[1]) - 1
    def move(self, dir):
        self.prevX, self.prevY = self.x, self.y
        if dir == "R":
            self.x += 1
        elif dir == "L":
            self.x -= 1
        elif dir == "B":
            self.y -= 1
        elif dir == "T":
            self.y += 1
        elif dir == "RT":
            self.x += 1
            self.y += 1
        elif dir == "LT":
            self.x -= 1
            self.y += 1
        elif dir == "RB":
            self.x += 1
            self.y -= 1
        elif dir == "LB":
            self.x -= 1
            self.y -= 1
        if not(0 <= self.x <= 7 and 0 <= self.y <= 7):
            self.x, self.y = self.prevX, self.prevY
            return False
        return True
    def rollback(self):
        self.x, self.y = self.prevX, self.prevY
    def getPos(self):
        return (self.x, self.y)
    def __str__(self):
        return chr(self.x + 65) + str(self.y + 1)

def main():
    k, st, n = input().split(" ")
    king = Piece(k)
    stone = Piece(st)
    for _ in range(int(n)):
        dir = input()
        king.move(dir)
        if king.getPos() == stone.getPos():
            if not stone.move(dir):
                king.rollback()
    print(king, stone, sep = "\n")
if __name__ == '__main__':
    main()