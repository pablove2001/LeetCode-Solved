/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
    let lenW = strs[0].length;
    for (let i = 1; i < strs.length; i++) lenW = Math.min(lenW, strs[i].length);

    let res = '';

    for (let i = 0; i < lenW; i++) {
        for (let j = 0; j < strs.length - 1; j++) {
            if (strs[j][i] != strs[j + 1][i]) return res;
        }
        res += strs[0][i];
    }

    return res;
};