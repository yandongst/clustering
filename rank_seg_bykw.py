import sys

fn_topic=sys.argv[1]
fn_stats=sys.argv[2]

x_topic={}
x_kw_probsum={}
x_kw_cnt={}

def read_topic_file(fn):
  cur_t=[]
  for l in open(fn,'r'):
    l = l .strip()
    if l.startswith('Topic'):
      if l not in x_topic:
        cur_t=[]
        x_topic[l]=cur_t
    else:
      cur_t.append(filter(None,l.split(' ')))

def read_stats_file(fn):
  first=True
  for l in open(fn,'r'):
    if first:
      first=False
      continue
    ll=l.strip().split('\t')
    kw=ll[0]
    featurecnt=float(ll[2])
    prob=float(ll[4])
    if float(prob)>0.0:
      levels=kw.split('.')
      if levels[1]=='0':
        #print kw
        if kw not in x_kw_probsum:
          x_kw_probsum[levels[2]]=prob*featurecnt
          x_kw_cnt[levels[2]]=featurecnt
        else:
          x_kw_probsum[levels[2]]+=prob*featurecnt
          x_kw_cnt[levels[2]]+=featurecnt
      #print kw,featurecnt,prob


read_topic_file(fn_topic)
read_stats_file(fn_stats)

#for k in x_kw_cnt:
  #cnt=x_kw_cnt[k]
  #probsum=x_kw_probsum[k]
  #print k,cnt,probsum, probsum/cnt
  
for k in x_topic:
  score=0
  for kw,w in x_topic[k][:10]:
    if kw in x_kw_cnt:
      score+=x_kw_probsum[kw]/x_kw_cnt[kw]*float(w)
    else:
      #print 'dont have:'+kw
      pass
  print k,score
