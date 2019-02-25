import sys
from abc import *

class TaxEntity:
    __taxRate = 0.08

    # @type_definition(int)
    def calcTaxPrice(self, price):
        print("TaxEntity")
        p = self.__taxRate + 1
        return round(price * p)

class TaxCalculateUseCaseInputData:
    __price: int = 0

    # @type_definition(int)
    def __init__(self, price):
        print("TaxCalculateUseCaseInputData")
        self.__price = price

    def getPrice(self):
        return self.__price

class TaxCalculateUseCaseOutputData:
    __price: int = 0

    # @type_definition(int)
    def __init__(self, price):
        print("TaxCalculateUseCaseOutputData")
        self.__price = price

    def getPrice(self):
        return self.__price

class ITaxCalculateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def calcTaxPrice(self, inputData: TaxCalculateUseCaseInputData):
        print("ITaxCalculateUseCase")
        pass

class TaxCalculateUseCase(ITaxCalculateUseCase):
    def calcTaxPrice(self, inputData: TaxCalculateUseCaseInputData):
        print("TaxCalculateUseCase")
        taxEntity = TaxEntity()
        price = inputData.getPrice()
        taxPrice = taxEntity.calcTaxPrice(price)
        return TaxCalculateUseCaseOutputData(taxPrice)

for line in iter(sys.stdin.readline, ""):
    useCase = TaxCalculateUseCase()
    price = int(line)
    inputData = TaxCalculateUseCaseInputData(price)
    outputData = useCase.calcTaxPrice(inputData)
    taxPrice = outputData.getPrice()
    print('taxPrice:%d ' % taxPrice)

