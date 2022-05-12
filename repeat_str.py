def non_repeating_char(str1):
    char_order = []
    ctr = {}
    for i in str1:
        if i in ctr:
            ctr[i] += 1
        else:
            ctr[i] = 1
            char_order.append(i)
    for i in char_order:
        if ctr[i] == 1:
            return i
    return None


print(non_repeating_char('abcabcdef'))
print(non_repeating_char('aabbcc'))
