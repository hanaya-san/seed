class ITaxCalculateUseCase(metaclass=ABCMeta):
    @abstractmethod
    def calcTaxPrice(self, inputData: TaxCalculateUseCaseInputData):
        print("ITaxCalculateUseCase")
        pass


