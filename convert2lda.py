import sys
from operator import itemgetter

keep_event=False
t_score=0.00
t_num=10
inc_domain=True

def proc(ls_t):
  #print ls_t
  rc=[]
  domains=[]
  for t in ls_t:
    n,v=t.split('=')
    v=float(v)

    ns = n.split('.')
    if len(ns)>2:
      if ns[1]=='99' :continue  
      if ns[1]=='1' :continue  
    if n.startswith('9') or n.startswith('11'):
    #if n.startswith('11'):
      #print '.'.join(n.split('.')[1:]),
      pass
    #elif n.startswith('9.'):
      #domains.append(n[2:])
    else:
      if keep_event:
        #rc.append(ns[0]+'.'+ '.'.join(n.split('.')[2:]))
        pass
      else:
        #rc.append( '.'.join(n.split('.')[2:]))
        rc.append( (n,v))
  sorted_rc= sorted(rc,key=itemgetter(1), reverse=True)
  top_sorted_rc=[]
  for t in sorted_rc:
    #top_sorted_rc.append(t[0])
    top_sorted_rc.append('.'.join(t[0].split('.')[2:]))
    #if len(top_sorted_rc)>=t_num or t[1]<t_score:
    if len(top_sorted_rc)>=t_num :
      break
  return sorted_rc,top_sorted_rc,domains

for l in sys.stdin:
  l=l.strip()
  #print l
  #c,t,fs=l.split('\t')
  c,t,fs=l.split('\t')
  #ls=[]
  l_topics,top_l_topics,domains=proc(fs.split(';'))
  #if l_topics:
    #print c+'\t'+' '.join(set(l_topics))
    #print c+'\t',l_topics
  if top_l_topics:
    print c+'\t'+' '.join(set(top_l_topics))+' '+' '.join(domains)
    #print c+'\t',top_l_topics
  #print
  #if newline:print 
