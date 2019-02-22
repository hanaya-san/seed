import * as readline from 'readline';
import * as process from 'process';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', (input: string) => {
    const price = Number(input);
    const taxPrice = Math.round(price * 1.08);
    console.log(`税込価格:${taxPrice}`);
});
