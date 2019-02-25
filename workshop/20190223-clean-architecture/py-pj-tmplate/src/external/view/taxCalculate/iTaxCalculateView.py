from abc import *
from usecase.taxCalculate import *

class ITaxCalculateView(metaclass=ABCMeta):
    @abstractmethod
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("ITaxCalculateView")
        pass


