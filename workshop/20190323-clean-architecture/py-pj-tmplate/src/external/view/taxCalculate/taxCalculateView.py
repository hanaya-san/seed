from useCase import *
from useCase.taxCalculate import *
from external.view.taxCalculate import *

class TaxCalculateView(ITaxCalculateView):
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("TaxCalculateView")
        taxPrice = outputData.getPrice()
        print('taxPrice:%d ' % taxPrice)


