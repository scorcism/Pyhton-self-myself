letter ='''Dear <|name|> 
you are selected
Date: <|date|>'''

name =input("enter your name :\n")
date =input("neter the date :\n")

letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>","date")

print(letter)

