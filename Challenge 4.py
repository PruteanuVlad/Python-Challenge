import urllib.request
nothing=12345

while 1:
    url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(nothing)[1:-2]
    fhand = urllib.request.urlopen(url)
    for line in fhand:
        print(line.decode().strip(),end=" ")
        nothing=[int(s) for s in line.decode().strip().split() if s.isdigit()]
        print(url,end="")
        print(str(nothing)[1:-1])
