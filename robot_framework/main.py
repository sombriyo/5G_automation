from itertools import permutations


def somefunc(s1, s2):
    prem = permutations(s1)
    for i in prem:
        word = ''.join(i)
        if word in s2:
            return True
    return False


s1 = "ab"
s2 = "eidbaooo"

print(somefunc(s1, s2))
