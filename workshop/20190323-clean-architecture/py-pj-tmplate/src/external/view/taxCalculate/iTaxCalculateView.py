class ITaxCalculateView(metaclass=ABCMeta):
    @abstractmethod
    def display(self, outputData: TaxCalculateUseCaseOutputData):
        print("ITaxCalculateView")
        pass


