"""
C= Create  R= Read  U= Update  D= Delete
f = open("Filename.txt", 'mode')
exit
"""
f = open("demo.txt","r")
#print(f)
a = f.read()
print(a)
f.close()