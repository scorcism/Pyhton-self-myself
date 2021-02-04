import os

def CreateIfNotExixt(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

files =os.listdir()
print(files)
CreateIfNotExixt("images")
CreateIfNotExixt("Docs")
CreateIfNotExixt("Media")
imgexten= [".jprg",".jpg","png"]
images= [file for file in files if os.path.splitext(file)[1].lower() in imgexten]
 print(images)