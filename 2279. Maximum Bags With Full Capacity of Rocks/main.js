/**
 * @param {number[]} capacity
 * @param {number[]} rocks
 * @param {number} additionalRocks
 * @return {number}
 */
var maximumBags = function (capacity, rocks, a) {
    let res = 0;
    let arr = [];

    for (let i = 0; i < rocks.length; i++) {
        arr.push(capacity[i] - rocks[i]);
    }

    arr.sort((a, b) => a - b);

    for (let i = 0; i < arr.length; i++) {
        if (a <= 0 || arr[i] - a > 0) return res;

        a -= arr[i];
        res++;
    }

    return res;
};