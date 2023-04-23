f=open('myfile.txt','r')
text = f.read()
print(text)
l1 = len(text)
print(l1)
f.close()

f=open('myfile.txt','a')
f.write(" hieee i am huzefa")
f.close()

f=open('myfile.txt','r')
print(f.read())
f.close()

f=open('myfile.txt','w')
f.write('hehehhhehehe')
f.close()

f=open('myfile.txt','r')
print(f.read())
f.close()