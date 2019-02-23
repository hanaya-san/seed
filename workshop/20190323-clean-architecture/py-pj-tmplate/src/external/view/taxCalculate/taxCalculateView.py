from external.view.taxCalculate import *
from usecase.taxCalculate import *

class TaxCalculateView(ITaxCalculateView):
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("TaxCalculateView")
        taxPrice = outputData.getPrice()
        print('taxPrice:%d ' % taxPrice)


