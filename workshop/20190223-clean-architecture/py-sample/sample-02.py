import sys

class TaxEntity:
    __taxRate = 0.08

    def calcTaxPrice(self, price):
        p = self.__taxRate + 1

        return round(price * p)

for line in iter(sys.stdin.readline, ""):
    taxEntity = TaxEntity()
    price = int(line)
    taxPrice = taxEntity.calcTaxPrice(price)
    print('taxPrice:%d ' % taxPrice)

