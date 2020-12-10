import pickle

with open('banner.p', 'rb') as fp:
    result = pickle.load(fp)
for x in result:
    for y in x:
        print(y[0]*y[1],end="")
    print()
