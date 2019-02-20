"use strict";
exports.__esModule = true;
var readline = require("readline");
var process = require("process");
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
rl.on('line', function (input) {
    var price = Number(input);
    var taxPrice = Math.round(price * 1.08);
    console.log("\u7A0E\u8FBC\u4FA1\u683C:" + taxPrice);
});
