class TaxCalculateUseCaseOutputData:
    __price: int = 0

    # @type_definition(int)
    def __init__(self, price):
        print("TaxCalculateUseCaseOutputData")
        self.__price = price

    def getPrice(self):
        return self.__price


