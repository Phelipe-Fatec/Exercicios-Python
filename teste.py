c = int(input())
l = []
for i in range(0, c):
    s = str(input())
    t = s.split()
    l.append(t)

for k, v in enumerate(l):
    a = sorted(v, key=len, reverse=True)
    for b in range(0, len(v)):
        print(a[b], end=' ')
    print()
