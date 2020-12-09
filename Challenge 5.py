import pickle

with open('banner.p', 'rb') as fp:
    result = pickle.load(fp)
for x in result:
    print(x)
