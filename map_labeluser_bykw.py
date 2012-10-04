'''
assign user clusters according the cluster keyword list.
e.g. user has keywords 
'''

import sys

lw=[]
top=20
for l in sys.stdin:
  l = l.strip()
  if l.startswith('Topic'):
    if lw: print ','.join(lw[:top])
    print l
    lw=[]
  else:
    lw.append(l.split(' ')[0])
if lw: print ','.join(lw[:top])
