
class TaxEntity:
    __taxRate = 0.08

    # @type_definition(int)
    def calcTaxPrice(self, price):
        print("TaxEntity")
        p = self.__taxRate + 1
        return round(price * p)

