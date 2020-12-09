f=open("Challenge 3 input.txt","r")
x=f.read()
for i in range(4,len(x)-4):
    if x[i].islower() and x[i-4].islower() and x[i-3].isupper() and x[i-2].isupper() and x[i-1].isupper() and x[i+1].isupper() and x[i+2].isupper() and x[i+3].isupper() and x[i+4].islower():
        print(x[i-3]+x[i-2]+x[i-1]+x[i]+x[i+1]+x[i+2]+x[i+3]) 