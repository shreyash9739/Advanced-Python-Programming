import re
text = "Welcome to Lab towards too abcto"
pattern = r'\bto\b'
p = re.findall(pattern,text)
print(p)