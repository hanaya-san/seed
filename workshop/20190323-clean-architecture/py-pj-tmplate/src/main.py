import sys
from usecase import *
from usecase.taxCalculate import * 
from external.view.taxCalculate import *

for line in iter(sys.stdin.readline, ""):
    useCase = CalculateUseCase()
    view = TaxCalculateView()
    controller = TaxCalculateController(useCase, view)
    controller.calcTaxPrice(line)
