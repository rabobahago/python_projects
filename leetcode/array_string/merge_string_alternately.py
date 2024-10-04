# %%
def mergeAlternately(word1, word2):
    A, B = len(word1), len(word2)
    a, b = 0, 0
    result = []
    word = 1
    while a < A and b < B:
        if word == 1:
            result.append(word1[a])
            a += 1
            word = 2
        else:
            result.append(word2[b])
            b += 1
            word = 1
    while a < A:
        result.append(word1[a])
        a += 1
    while b < B:
        result.append(word2[b])
        b += 1
    return ''.join(result)
mergeAlternately('abc', 'rsyys')
# %%