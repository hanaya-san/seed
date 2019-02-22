import sys

for line in iter(sys.stdin.readline, ""):
    price = int(line)
    taxPrice = int(price * 1.08)
    print('taxPrice:%d ' % taxPrice)


