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


class ITaxCalculateView(metaclass=ABCMeta):
    @abstractmethod
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("ITaxCalculateView")
        pass

class TaxCalculateView(ITaxCalculateView):
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("TaxCalculateView")
        taxPrice = outputData.getPrice()
        print('taxPrice:%d ' % taxPrice)

class TaxCalculateController():
    # __useCase: iTaxCalculateUseCase = 
    def __init__(self, useCase: ITaxCalculateUseCase, view: ITaxCalculateView):
        self.useCase = useCase
        self.view = view

    def calcTaxPrice(self, priceText: str):
        price = int(priceText)
        inputData = TaxCalculateUseCaseInputData(price)
        outputData = self.useCase.calcTaxPrice(inputData)
        self.view.display(outputData)

for line in iter(sys.stdin.readline, ""):
    useCase = TaxCalculateUseCase()
    view = TaxCalculateView()
    controller = TaxCalculateController(useCase, view)
    controller.calcTaxPrice(line)


