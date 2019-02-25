import * as readline from 'readline';
import * as process from 'process';

class TaxEntity {
    private readonly taxRate: number = 0.08;

    public calcTaxPrice(price: number): number {
        const p = this.taxRate + 1;

        return Math.round(price * p);
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input: string) => {
    const taxEntity = new TaxEntity();
    const price = Number(input);
    const taxPrice = taxEntity.calcTaxPrice(price);
    console.log(`税込価格:${taxPrice}`);
});
