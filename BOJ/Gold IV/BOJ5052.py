#BOJ5052 전화번호 목록 20210331
import sys
input = sys.stdin.readline

class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        currentNode = self.head
        for s in string:
            if s not in currentNode.children:
                currentNode.children[s] = Node(s)
            currentNode = currentNode.children[s]
        currentNode.data = string
    
    def fullSearch(self, nextNode = None):
        ret = True
        currentNode = self.head if not nextNode else nextNode
        if currentNode.data and currentNode.children:
            return False
        for child in currentNode.children.values():
            if not self.fullSearch(child):
                return False
        return ret

def main():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        trie.insert(input().rstrip())
    print("YES" if trie.fullSearch() else "NO")
           
if __name__ == '__main__':
    for _ in range(int(input())):
        main()