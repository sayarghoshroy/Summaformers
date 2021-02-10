import json
import os

def clean(file):
    if 'import json' in file : return False
    file = file.split('{')
    if len(file) == 1: return False
    return '{' + '{'.join(file[1:])

files = os.listdir('json/')

data = []
for ind,file in enumerate(files):
    with open('json/'+file,'r+') as f:
        text = clean(f.read())
        if text:
            text = json.loads(text)['metadata']
            if ind == 0: print(text.keys())
            # Change this line to change which sections are retained/dropped
            for key in text.keys() - ['title','sections','references','abstractText']:
                text.pop(key)
            data.append(text)
        else:
            print("{} is bad".format(file))

with open('listofdic_longsummtest.json','w+') as f:
    json.dump(data,f,indent=4)