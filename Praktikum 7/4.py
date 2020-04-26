import re

f = open("KEI.html", "r", encoding="latin1")
teks = f.read()
f.close()

pola =  r'(\w+)</a></td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>\d\.\d\d</td>\
<td>(\d.\d\d)'

data = re.findall(pola, teks)
isi = []
for i in data:
    isi.append((i[0], float(i[1])))
print(isi)
