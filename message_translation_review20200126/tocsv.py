import json
import csv
import codecs

class DiffJson:
    diffset:dict
    def __init__(self,org_path,od_path,path):
        en=None
        before=None
        after=None
        with open (org_path,'r') as f:
            en=json.load(f)
        with open (od_path,'r') as f:
            before=json.load(f)
        with open (path,'r') as f:
            after=json.load(f)
        messages={}
        #enでインデクスを作る。
        for i in en:
            messages[i]=[en[i]["message"]]

        for i in before:
            if i not in messages:
                print("before %s is not found in en message")
            messages[i].append(before[i]["message"])
        for i in messages:
            if len(messages[i])<2:
                messages[i].append(None)

        for i in after:
            if i not in messages:
                print("after %s is not found in en message")
            messages[i].append(after[i]["message"])
        for i in messages:
            if len(messages[i])<3:
                messages[i].append(None)

        for i in en:
            if "description" not in en[i]:
                continue
            messages[i].append(en[i]["description"])
        for i in messages:
            if len(messages[i])<4:
                messages[i].append(None)

        for i in messages:
            messages[i].append(None)

        self.diffset=messages
        print(messages)
    
"""
make a messagetextJson

"""
a=DiffJson("messages.json.org","messages.json.old","messages.json.new")
with  codecs.open ("out.json",'w','utf-8') as f:
    json.dump(a.diffset,f,indent=4, ensure_ascii=False)
