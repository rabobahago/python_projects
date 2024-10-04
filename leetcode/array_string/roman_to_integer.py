def romanToInt(s):
    sym_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    n = len(s)
    result = 0
    while i < n:
        if i < n - 1 and sym_val[s[i]] < sym_val[s[i + 1]]:
            result += sym_val[s[i + 1]] - sym_val[s[i]]
            i += 2
        else:
            result += sym_val[s[i]]
            i += 1
    return result
