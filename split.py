import sys

for l in sys.stdin:
  l = l.strip()
  for w in l.split(' '):
    print w,
    if '_' in w:
      print w,
      print ' '.join(w.split('_')),
  print
