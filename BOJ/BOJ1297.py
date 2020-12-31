import math

def main():
    d,h,w = map(int, input().split(' '))
    rw = math.sqrt((w**2 * d**2)/(w**2 + h**2))
    rh = rw*h/w
    print(math.floor(rh), math.floor(rw))
      
if __name__ == "__main__":
    main()