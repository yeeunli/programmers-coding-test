import sys

num = int(input())

data = sorted([int(sys.stdin.readline()) for i in range(num)])


for i in data:
    print(i)