import json
import csv
import codecs



"""
make a messagetextJson

"""

with codecs.open ("messagediff.json",'r','utf-8') as f:
    d=json.load(f)
    j={}
    c=0
    for i in d:
        t={}
        v=d[i]
        if v[4] is None:
            t["message"]=v[2]
            print("%s\tdefault transration!"%(i))
        else:
            c=c+1
            t["message"]=v[4]
        if v[3] is not None:
            t["description"]=v[3]
        j[i]=t
    with codecs.open ("message.json",'w','utf-8') as f:
        json.dump(j,f,ensure_ascii=False,indent=4)
    print("created json %d/%d"%(c,len(d)))
    