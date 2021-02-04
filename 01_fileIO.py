#thiss will open the file sampleFILE.txt in r means read mode
#open is use to read the file

f =open('01_sampleFILE.txt', 'r')
# data=f.read()#read its content
data=f.read(5)#this will write 1st 5 eords in the file
print(data)#print its content

f.close()#close the file