from usecase.iTaxCalculateUseCase import ITaxCalculateUseCase
from usecase.taxCalculate import *
from model import *

class TaxCalculateUseCase(ITaxCalculateUseCase):
    def calcTaxPrice(self, inputData: TaxCalculateUseCaseInputData):
        print("TaxCalculateUseCase")
        taxEntity = TaxEntity()
        price = inputData.getPrice()
        taxPrice = taxEntity.calcTaxPrice(price)
        return TaxCalculateUseCaseOutputData(taxPrice)


