with open("remove.txt") as f:
    content=f.read()
# it takes argument remove.txt
content =content.replace("very","#$%@#!")

with open("remove.txt","w") as f:
    f.write(content)