class TaxCalculateUseCaseInputData:
    __price: int = 0

    # @type_definition(int)
    def __init__(self, price):
        print("TaxCalculateUseCaseInputData")
        self.__price = price

    def getPrice(self):
        return self.__price


