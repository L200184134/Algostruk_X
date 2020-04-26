import re

f = open("Indonesia.txt", "r", encoding="latin1")
teks = f.read()
f.close()
string = re.findall(r"di\w+", teks)
print(string)
