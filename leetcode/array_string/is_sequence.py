# %%
def is_sequence(s, t):
    S, T = len(s), len(t)
    if s == '': return True
    if S > T: return False
    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S - 1:
                return True
            j += 1
    return False
s = "abc"
t = "ahbgdc"
is_sequence(s, t)
# %%
