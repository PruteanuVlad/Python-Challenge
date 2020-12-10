import zipfile

path = 'C:\\Users\\vlad.pruteanu\\Documents\\GitHub\\Python-Challenge\\channel\\100.txt'
f=open(path, "r")

archive = zipfile.ZipFile(r'C:\\Users\\vlad.pruteanu\\Documents\\GitHub\\Python-Challenge\\channel.zip', 'r')

nothing="[90052]"
i=0
while 1:
    path = 'C:\\Users\\vlad.pruteanu\\Documents\\GitHub\\Python-Challenge\\channel\\'+str(nothing)[1:-1]+'.txt'
    archive = zipfile.ZipFile(r'C:\\Users\\vlad.pruteanu\\Documents\\GitHub\\Python-Challenge\\channel.zip', 'r')
    try:
        print((archive.getinfo(str(str(nothing)[1:-1])+'.txt').comment.decode("utf-8")),end="")
    except:
        pass
    f=open(path, "r")
    x=f.read()
    #print(x)
    nothing=[int(s) for s in x.strip().split() if s.isdigit()]