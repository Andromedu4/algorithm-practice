text = "aboba"

def remove_aboba(s):
    new_aboba = ''

    for i in range(1, len(s)-1):
        new_aboba += s[i]

    return new_aboba

print(remove_aboba(text))


"""

def remove_char(s):
    return s[1:-1]
1
"""