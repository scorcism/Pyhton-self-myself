def strip_remove_split(string,word):
    newstr=(string.replace(word," "))
    return newstr.strip()


this ="   me and the spacees are gone       "

n=strip_remove_split(this,"me")
print(n)

