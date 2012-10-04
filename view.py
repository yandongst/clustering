import sys

lw=[]
top=100
if len(sys.argv)>1:
  top = int(sys.argv[1])
for l in sys.stdin:
  l = l.strip()
  if l.startswith('Topic'):
    if lw: print ','.join(lw[:top])
    print l
    lw=[]
  else:
    lw.append(l.split(' ')[0])
if lw: print ','.join(lw[:top])
