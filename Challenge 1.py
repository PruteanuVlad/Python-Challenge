import string
input="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
url="http://www.pythonchallenge.com/pc/def/map.html"
#for x in input:
#    if x.isalnum():
#        print(chr(97+(((ord(x)+2)%123)%97)),end="")
#    else:
#        print(x,end="")

print(input.translate(input.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")))
print("----------------------------------------------------------------------------------")
print(url.translate(url.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")))