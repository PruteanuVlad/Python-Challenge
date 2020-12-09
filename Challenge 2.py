from collections import Counter

f=open("Challenge 2 input.txt","r")
input=f.read()

c = Counter(input)
print(c.most_common()[::-1])
