# I'm pretty sure there's a better way to do this, if I like make a list containing all the vowels and check against that?

def anti_vowel(text):
    char = 0
    no_vowel = []
    for x in text:
        y = x.lower()
        if y != 'a' and y != 'e' and y != 'i' and y != 'o' and y != 'u':
            no_vowel.append(text[char])
            char += 1
        elif x:
            char += 1
    return ''.join(no_vowel)
