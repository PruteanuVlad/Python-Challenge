from PIL import Image

im = Image.open('oxygen.png') 
pix = im.load()
i=0 
s="s"
while i<608:
    if s[len(s)-1]!=chr((pix[i,0])[0]):
        s=s+chr((pix[i,0])[0])
    i=i+1
print(s)
final=chr(105)+chr(110)+chr(116)+chr(101)+chr(103)+chr(114)+chr(105)+chr(116)+chr(121)
print(final)