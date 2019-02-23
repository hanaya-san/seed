for line in iter(sys.stdin.readline, ""):
    useCase = TaxCalculateUseCase()
    view = TaxCalculateView()
    controller = TaxCalculateController(useCase, view)
    controller.calcTaxPrice(line)
