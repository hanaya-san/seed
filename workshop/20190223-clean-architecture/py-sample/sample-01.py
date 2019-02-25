import sys

for line in iter(sys.stdin.readline, ""):
    price = int(line)
    taxPrice = round(price * 1.08, 0)
    print('taxPrice:%d ' % taxPrice)


