from usecase import *
from external.view.taxCalculate import *

class TaxCalculateController():
    def __init__(self, useCase: ITaxCalculateUseCase, view: ITaxCalculateView):
        self.useCase = useCase
        self.view = view

    def calcTaxPrice(self, priceText: str):
        price = int(priceText)
        inputData = TaxCalculateUseCaseInputData(price)
        outputData = self.useCase.calcTaxPrice(inputData)
        self.view.display(outputData)


