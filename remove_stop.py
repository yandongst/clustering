import sys

x=set([])
def read_stop(fn):
  sys.stderr.write('reading stopwords file:'+fn+'\n')
  for l in open(fn,'r'):
    x.add(l.strip())
  sys.stderr.write('#stopwords :'+str(len(x))+'\n')

read_stop(sys.argv[1])

for l in sys.stdin:
  l = l.strip()
  ll=[]
  for w in l.split(' '):
    if w not in x:
      ll.append(w)
      #print w,
  if not ll:
    sys.stderr.write('error:'+l+'\n')
    ll.append('0')
  print ' '.join(ll)
    #print '0'
  #print
