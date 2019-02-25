import sys
from usecase import *
from external.view.taxCalculate import *
from adapter.controller import *

for line in iter(sys.stdin.readline, ""):
    useCase = TaxCalculateUseCase()
    view = TaxCalculateView()
    controller = TaxCalculateController(useCase, view)
    controller.calcTaxPrice(line)

sys.exit(0)
