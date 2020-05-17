text = "X-DSPAM-Confidence:0.8475";
pos=text.find(':')
#print(pos)
slic = text[pos+1:]
#print(slic)
val=float(slic)
print(val)
