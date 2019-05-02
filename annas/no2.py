import re

f=open('Indonesia.txt', 'r', encoding='latin1')
teks=f.read()
f.close()
p=r'di\w+'
strings = re.findall(p, teks)
print(strings)
