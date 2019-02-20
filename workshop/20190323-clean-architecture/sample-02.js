"use strict";
exports.__esModule = true;
var readline = require("readline");
var process = require("process");
var TaxEntity = /** @class */ (function () {
    function TaxEntity() {
        this.taxRate = 0.08;
    }
    TaxEntity.prototype.calcTaxPrice = function (price) {
        var p = this.taxRate + 1;
        return Math.round(price * p);
    };
    return TaxEntity;
}());
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function (input) {
    var taxEntity = new TaxEntity();
    var price = Number(input);
    var taxPrice = taxEntity.calcTaxPrice(price);
    console.log("\u7A0E\u8FBC\u4FA1\u683C:" + taxPrice);
});
