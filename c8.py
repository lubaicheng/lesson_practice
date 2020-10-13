import re

s = 'life is short,i use python, i love python'
# r = re.match('\d',s)
# print(r.span())
r = re.search('life(.*)python(.*)python',s)
print(r.groups())