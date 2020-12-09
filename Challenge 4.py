import urllib.request
nothing="[8022]"
i=0
while 1:
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing)[1:-1]
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        print(line.decode().strip(),end=" ")
        print(i,end=" ")
        print(str(nothing)[1:-1])
        nothing=[int(s) for s in line.decode().strip().split() if s.isdigit()]
        if str(nothing)[1:-1]=="72758":
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
        #print(url,end="")
        i=i+1

