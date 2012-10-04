
import sys

#Topic 15th: 0.00234310879
fn_ranking=sys.argv[1]
fn_topics=sys.argv[2]


lw=[]
top=20
x_kw={}
last_topic=''
for l in open(fn_topics,'r'):
  l = l.strip()
  if l.startswith('Topic'):
    if not last_topic:
      last_topic=l
    if lw:
      x_kw[last_topic]=','.join(lw[:top])
      last_topic=l
    lw=[]
  else:
    lw.append(l.split(' ')[0])
if lw: x_kw[last_topic]=','.join(lw[:top])

for l in open(fn_ranking,'r'):
  l = l.strip()
  p1,p2=l.split(':')
  topic_name=p1.strip()
  score=float(p2.strip())
  print topic_name,score
  print x_kw[topic_name+':']
  print
