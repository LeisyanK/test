s = '10+2*3'
# for i, el in enumerate(s):
#     if not el.isdigit():
#
if '*' in s:
    s1 = s.index('*')
elif '/' in s:
    s1 = s.index('/')
else:
    s1 = -1

if '*' in s:
    s2 = s.index('+')
elif '/' in s:
    s2 = s.index('-')
else:
    s2 = -1
print(s1)
print(s2)
if s1 > s2:
    print(s[s2+1:s1])
    print(s[s1+1:])