/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function (num) {
    const symbol = [['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'], ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'], ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'], ['', 'M', 'MM', 'MMM']];

    let res = '';

    for (let i = 3; i > -1; i--) {
        res += symbol[i][parseInt(num / 10 ** i)];
        num = num % 10 ** i;
    }

    return res;
};