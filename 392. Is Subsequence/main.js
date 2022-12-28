/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function (s, t) {
    if (s == '') return true;
    if (t == '') return false;
    if (s.length > t.length) return false;

    let ind = 0
    for (let i = 0; i < t.length; i++) {
        if (s[ind] == t[i]) ind++;
        if (ind == s.length) return true;
    }

    return false;
};