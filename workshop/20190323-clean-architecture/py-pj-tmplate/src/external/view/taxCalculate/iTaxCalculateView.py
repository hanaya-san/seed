from useCase import *
from useCase.taxCalculate import *

class ITaxCalculateView(metaclass=ABCMeta):
    @abstractmethod
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("ITaxCalculateView")
        pass


