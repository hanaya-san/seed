import * as readline from 'readline';
import * as process from 'process';

class TaxEntity {
    private readonly taxRate: number = 0.08;

    public calcTaxPrice(price: number): number {
        const p = this.taxRate + 1;

        return Math.round(price * p);
    }
}

class TaxCalculateUseCaseInputData {
    public readonly price: number;

    constructor(price: number) {
        this.price = price;
    }
}

class TaxCalculateUseCaseOutputData {
    public readonly price: number;

    constructor(price: number) {
        this.price = price;
    }
}

interface ITaxCalculateUseCase {
    calcTaxPrice(inputData: TaxCalculateUseCaseInputData): TaxCalculateUseCaseOutputData;
}

class TaxCalculateUseCase implements ITaxCalculateUseCase {
    public calcTaxPrice(inputData: TaxCalculateUseCaseInputData): TaxCalculateUseCaseOutputData {
        const taxEntity = new TaxEntity();
        const price = inputData.price;
        const taxPrice = taxEntity.calcTaxPrice(price);

        return new TaxCalculateUseCaseOutputData(taxPrice);
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input: string) => {
    const useCase = new TaxCalculateUseCase();
    const price = Number(input);
    const inputData = new TaxCalculateUseCaseInputData(price);
    const outputData = useCase.calcTaxPrice(inputData);
    const taxPrice = outputData.price;
    console.log(`税込価格:${taxPrice}`);
});
