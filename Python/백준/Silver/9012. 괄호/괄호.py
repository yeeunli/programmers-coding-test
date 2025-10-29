import sys

n = int(input())
a = []

for i in range(n):
    a.append(sys.stdin.readline().rstrip())

open = '('
close = ')'

for b in a:
    cnt = 0
    tf = True

    for c in b:
        if c == open:
            cnt += 1
        elif c == close:
            cnt -= 1

        if cnt < 0:
            tf = False
            break
    if tf and cnt == 0:
        print('YES') 
    else:
        print("NO")