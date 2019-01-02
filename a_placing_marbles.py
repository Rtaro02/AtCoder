import re
a = input()
regex = '^(\d)(\d)(\d)'
s1 = int(re.sub(regex, r'\1', a))
s2 = int(re.sub(regex, r'\2', a))
s3 = int(re.sub(regex, r'\3', a))
i = 0
if s1 == 1:
    i += 1
if s2 == 1:
    i += 1
if s3 == 1:
    i += 1
print(i)