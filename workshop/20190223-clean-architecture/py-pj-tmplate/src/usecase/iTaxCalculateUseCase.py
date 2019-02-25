from abc import *
from usecase import taxCalculate

class ITaxCalculateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def calcTaxPrice(self, inputData):
        print("ITaxCalculateUseCase")
        pass


